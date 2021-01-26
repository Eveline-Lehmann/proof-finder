#-------------------------------------------------------
# Programm to test derivability of modal formulas in S4
#
# (C) 2020 Eveline Lehmann, Bern, Switzerland
# Released under GNU Public License (GPL)
# email eveline.lehmann@inf.unibe.ch
#-------------------------------------------------------

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from graph import *

""" The variable prooftree records the derivation process in scK."""
prooftree = ProofTree()

""" Checks, whether a formula has the correct form
    @formula: a list that indicates in index 0 the arity, in index 1 the operator if it exists and
    a char otherwise, and in the remaining indices lists that represent formulas of this form """
def is_welldefined(formula):
    try:
        assert type(formula) == tuple
        if len(formula) != formula[0]+2:
            return False
        elif formula[0]==0:
            return type(formula[1]) == str
        elif formula[0]==1:
            return (formula[1] in ['-','box','dia']) and is_welldefined(formula[2])
        elif formula[0]==2:
            return (formula[1] in ['+' ,'*', '->']) and is_welldefined(formula[2]) and is_welldefined(formula[3])
        else:
            return False
    except AssertionError:
        print("formula must be given as a tuple of 2 (in case of an atom),\n"+
              "3 (in case of a negation or a modal) or 4 (in case of a binary operator) elements,\n"+
              "such that \n at index 0: 0 if atom, the arity of the operator otherwise"+
            "\n at index 1: the operation symbol '-', '+', '*', '->', 'box', 'dia' or a string in case of an atom"+
              "\n at index 2: another tuple according to these rules, representing the first argument of the operation "+
              "\n at index 3: another tuple according to these rules, representing the second argument of the operation")
    

""" Function that checks, whether some formula is derivable within s4 (as presented by Hererding Alain, Sequent Calculi
    for Proof Search in Some Modal Logics, PhD thesis University of Bern, Definition 5.6.15). It uses a two-sided sequent calculi
    that takes a formula in any form that corresponds to what is well-defined according to the function above. The proof
    can be recorded into a latex-file, if recorded = True.
    The given formula is converted into nnf and then is given to the function derivable(...) as part of the right sequent.
    If the proof is recorded, the prooftree is newly initialized with a node containing the original formula as root.
    @param formula: a formula given as described in the funktion is_welldefined(formula) above.
    @param recorded: flag to chose, whether the deriving process will be recorded as a prooftree."""
def derivable(formula, recorded=False, in_nnf=False):
    """ Function to check whether some formula is derivable in scK."""
    global prooftree
    current_node = None
    if recorded:
        prooftree = ProofTree()
        s1 = Sequent()
        s1.set_sequent([],[formula])
        n1 = Node(s1)
        prooftree.set_root(n1)
        current_node = n1
    left = []
    if not in_nnf:
        formula = nnf(formula)
    right = [formula]
    if recorded and right[0] != formula:
        s2 = Sequent()
        s2.set_sequent(left,right)
        n2 = Node(s2)
        n1.add_child(n2)
        n2.set_rule('nnf')
        current_node = n2
    history = set()
    return derive(history, left, right, recorded, current_node)

""" Function that checks, whether some sequent is derivable within scK (see comment above).
    The derivation starts with as many Or-rules as possible. If no Or left as main operator in
    any formula of the right sequent, Diamond-rules are applied as many as possible. If no more Diamonds
    left on the right sequent, then one And-Rule is applied if possible and hence, the sequent breaks down
    into two parts. For each of them the process starts from begining. If finally no more Or-, Diamond- or
    And-Rule can be applied, the Box-Rule is applied recursively (see comment there).
    Returns True, if the sequent left -> right is scK-derivable.    
    @param left: the left sequent of a two-sided sequent (list of tuples)
    @param right: the right sequent of a two-sided sequent (list of tuples)
    @param recorded: flag. If True, a proofgraph is built during deriving process.
    @param current_node: if recorded, denotes the current node of the proofgraph."""
def derive(history, left, right, recorded=False, current_node=None):
    """ Function to check whether the sequent left -> right is derivable in scK."""
    global prooftree
    if isAxiom(right):
        history = set()
        if recorded:
            s = Sequent()
            n = Node(s)
            if axiomTrue(right):
                n.set_rule('T')
            else:
                n.set_rule('id')
            current_node.add_child(n)
        return True
    else:
        appended = True
        # OR-rule
        while appended:
            appended, right = ruleOr(right)
            if recorded and appended:
                s = Sequent()
                s.set_sequent(left, right)
                n = Node(s)
                n.set_rule('$\lor$')
                current_node.add_child(n)
                current_node = n
        
        # Diamond-rule
        i = findIdxNextDia(right)
        while i>=0:
            if right[i] not in left:   # (diamond, new) (Heuerding p.135)
                left.append(right[i])
                rule = "$\Diamond$,new"
                history = set()
            else:
                rule = "$\Diamond$,dup"
            right.append(right[i][2])               
            right.remove(right[i])     # both diamond rules (ibid)
            if recorded:
                s = Sequent()
                s.set_sequent(left, right)
                n = Node(s)
                n.set_rule(rule)
                current_node.add_child(n)
                current_node = n
            i = findIdxNextDia(right)
                        
        # AND-rule
        copy_right = right[:]        # A copy is needed since right will be manipulated within for-loop
        for formula in copy_right:
            if formula[1]=='*':
                lleft = left[:]
                rleft = left[:]
                right.remove(formula)
                rright = right+[formula[2]]
                lright = right+[formula[3]]
                if recorded:
                    s1 = Sequent()
                    s1.set_sequent(lleft,lright)
                    n1 = Node(s1)
                    current_node.add_child(n1)
                    s2 = Sequent()
                    s2.set_sequent(rleft,rright)
                    n2 = Node(s2)
                    current_node.add_child(n2)
                    n1.set_rule('$\land$')
                    n2.set_rule('$\land$')
                    answer1 = derive(history, lleft, lright, recorded, n1)
                    answer2 = derive(history, rleft, rright, recorded, n2)
                else:
                    answer1 = derive(history, lleft, lright)
                    answer2 = derive(history, rleft, rright)                    
                return answer1 and answer2

        if isAxiom(right):
            history = set()
            if recorded:
                s = Sequent()
                n = Node(s)
                if axiomTrue(right):
                    n.set_rule('T')
                else:
                    n.set_rule('id')
                current_node.add_child(n)
            return True
        
        # Box-rule: not invertable, hence prepare backtracking
        number_of_boxes, right = countReorderBoxes(right)
        idx = 0
            
        while idx < number_of_boxes:
            if right[idx] in history:
                idx += 1
                continue
            copy_left=left[:]            
           
            r  = ruleBox(copy_left, right[idx])
            history.add(right[idx])
            idx += 1

            n = None    # Dummy-Variable for derive(...)
            if recorded:
                s = Sequent()
                s.set_sequent(copy_left,r)
                n = Node(s)
                current_node.add_child(n)
            
            is_derivable = derive(history, copy_left,r, recorded, n)
            if is_derivable:
                if recorded:
                    n.set_rule('$\Box$')
                return True
            elif recorded:
                current_node.remove_child(n)
        return False    
    
    
def isAxiom(right):
    """ Returns True if right is an axiom."""
    return axiomTrue(right) or axiomID(right)

def axiomTrue(right):
    """ Returns True, if right contains the constant T."""
    for elem in right:
        if elem[0]==0 and elem[1]=='T':
            return True
    return False

def axiomID(right):
    """ Returns True, if right contains a positive and a negative occurence of the same formula."""
    negatives = [form[2] for form in right if form[0]==1 and form[1]=='-']
    for elem in right:
        if elem in negatives:
            return True
    return False

def ruleOr(right):
    """ Replaces the first occurence of s+t,... in right by s,t,... . If no + in right then ruleOr(...)[0]=False."""
    for formula in right:
        if formula[1]=='+':
            right.remove(formula)
            right.append(formula[2])
            right.append(formula[3])
            return True, right
    return False, right

def findIdxNextDia(formulas):
    """ Returns the index of the first occurence of a diamond formula in a list of formulas. Returns -1 if there is no such formula."""
    for i in range(len(formulas)):
        if formulas[i][1] == 'dia':
            return i
    return -1
        
def ruleBox(left, fright):
    """ From dia f1... dia fn -> box g1... box gm to -> f1,...fn,fright."""
    right = [form[2] for form in left]
    right.append(fright[2])
    return right

def countReorderBoxes(right):
    """ Counts the number of boxes within the sequent right."""
    count = 0
    for formula in right:
        if formula[1]=='box':
            right.remove(formula)
            right.insert(0,formula)
            count += 1
    return count, right
        
def nnf(formula):
    """ Converts a formula given as a well-defined list into a formula in Negation Normal Form."""
    try:
        assert is_welldefined(formula)
        formula = removeImplications(formula)
        formula = convert2NNF(formula)
        return formula
    except AssertionError:
        print("This is not a formula according to this application!")

def is_atom(formula):
    """ True, if formula is atomic."""
    return formula[0]==0

def removeImplications(formula):
    """ Replaced a -> b by -a OR b."""
    # atoms and negation on atoms remain the same
    if is_atom(formula) or (formula[0]==1 and is_atom(formula[2])):
        return formula
    # negation: keep negation and remove implications from its expression
    elif formula[0]==1:
        return (1, formula[1], removeImplications(formula[2]))
    # operations:
    elif formula[0]==2:
        # +, *: keep operation and remove implications from their expressions
        if formula[1] in ['+','*']:
            return (2, formula[1], removeImplications(formula[2]), removeImplications(formula[3]))
        # implication: convert a->b into -a+b and remove implications from a and b
        else: # Hence formula[1]=='->':
            return (2, '+', (1, '-', removeImplications(formula[2])), removeImplications(formula[3]))
    else:
        return formula

""" based on DML-script 2013 p. 78, Definition 125"""    
def convert2NNF(formula):
    """ Converts formula that may contain +,*,-,->,box,dia into negation normal form."""
    # atoms
    if formula[0]==0:
        return formula
    # negations
    elif formula[0]==1:
        if formula[1]=='-':
            # negations on atoms
            if formula[2][0] == 0:
                if formula[2][1] == 'T':
                    return (0, 'F')
                elif formula[2][1] == 'F':
                    return (0, 'T')
                else:
                    return formula
            # negations on complex formulas
            else:
                # remove double negation
                if formula[2][0]==1 and formula[2][1]=='-':
                    return convert2NNF(formula[2][2])
                # de Morgan on and
                elif formula[2][0]==2 and formula[2][1]=='+':
                    return (2, '*', convert2NNF((1, '-', formula[2][2])),convert2NNF((1, '-', formula[2][3])))
                # de Morgan on or
                elif formula[2][0]==2 and formula[2][1]=='*':
                    return (2, '+', convert2NNF((1, '-', formula[2][2])),convert2NNF((1, '-', formula[2][3])))
                elif formula[2][0]==1 and formula[2][1]=='dia':
                    return (1, 'box', convert2NNF((1, '-', formula[2][2])))
                elif formula[2][0]==1 and formula[2][1]=='box':
                    return (1, 'dia', convert2NNF((1, '-', formula[2][2])))
                else: # Hence a negation of a modal
                    return (1, '-',convert2NNF(formula[2]))
        else: # Hence some modal formula
            return (1, formula[1], convert2NNF(formula[2]))
    # or and and
    elif formula[0]==2:
        if formula[1]=='+':
            return (2, '+', convert2NNF(formula[2]), convert2NNF(formula[3]))
        elif formula[1]=='*':
            return (2, '*', convert2NNF(formula[2]), convert2NNF(formula[3]))
        
def print_prooftree(filename = 'proof'):
    """ Generates a latex-file filename.tex in a separate directory proof, that contains a representation of the proof."""
    global prooftree
    prooftree.to_file(filename)

