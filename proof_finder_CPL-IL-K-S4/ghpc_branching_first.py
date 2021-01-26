#-------------------------------------------------------
# Programm to test derivability of modal formulas in IL
#
# (C) 2020 Eveline Lehmann, Bern, Switzerland
# Released under GNU Public License (GPL)
# email eveline.lehmann@inf.unibe.ch
#-------------------------------------------------------

from graph import *
from random import randint

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
            return formula[1]=='-' and is_welldefined(formula[2])
        elif formula[0]==2:
            return (formula[1] in ['+' ,'*', '->']) and is_welldefined(formula[2]) and is_welldefined(formula[3])
        else:
            return False
    except AssertionError:
        print("formula must be given as a tuple of 2 (in case of an atom),\n"+
              "3 (in case of a negation or a modal) or 4 (in case of a binary operator) elements,\n"+
              "such that \n at index 0: 0 if atom, the arity of the operator otherwise"+
            "\n at index 1: the operation symbol '-', '+', '*', '->' or a string in case of an atom"+
              "\n at index 2: another tuple according to these rules, representing the first argument of the operation "+
              "\n at index 3: another tuple according to these rules, representing the second argument of the operation")
    

""" Function that checks, whether some formula is derivable within ghpc (as presented by Dickhoff Roy, Contraction-free Sequent
    Calculi for Intuitionistic Logic, in: The Journal of Symbolic Logic, Volume 57, 1992, p.795-807, here p.801).
    It uses a two-sided sequent calculi that takes a formula in any form that corresponds to what is well-defined according
    to the function above. The proof can be recorded into a latex-file, if recorded = True.
    The given formula is converted into a normal form (negations and T-symbols are removed) and then is given to the function
    derivable(...) as part of the right sequent.
    If the proof is recorded, the prooftree is newly initialized with a node containing the original formula as root.
    @param formula: a formula given as described in the funktion is_welldefined(formula) above.
    @param recorded: flag to chose, whether the deriving process will be recorded as a prooftree."""
def derivable(formula, recorded=False, in_nf=False):
    """ Function to check whether some formula is derivable in scK."""
    if not is_welldefined(formula):
        print("This formula has no IL syntax and hence is not derivable in IL")
        return False
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
    if not in_nf:
        formula = remove_T_and_neg(formula)
    right = [formula]
    if recorded and right[0] != formula:
        s2 = Sequent()
        s2.set_sequent(left,right)
        n2 = Node(s2)
        n1.add_child(n2)
        n2.set_rule('nf')
        current_node = n2
    history = []
    return derive(left, right, history, recorded, current_node)

""" Function that checks, whether some sequent is derivable within ghpc (see comment above).
    The derivation starts with as many rules that need no branching or backtracking. So there
    is a double while-loop where the rules are applied until no more such rule is applicable.
    Then a randomly choden branching rule is applied if there is one. Finally, if no other rules
    than those, that may need backtracking are applicable, the backtracking right-implication
    rule is applied with all the machinery needed, to backtrack if necessary. If at the end
    not even a backtracking rule is applicable it remains to test, whether the final sequent
    is an axiom and hence the original formula is derivable.
    Returns True, if the sequent left -> right is ghpc-derivable.    
    @param left: the left sequent of a two-sided sequent (list of tuples).
    @param right: the right sequent of a two-sided sequent (list of tuples).
    @param history: prevents endless loops in backtracking part.
    @param recorded: flag. If True, a proofgraph is built during deriving process.
    @param current_node: if recorded, denotes the current node of the proofgraph."""
def derive(left, right, history, recorded=False, current_node=None):
    """ Function to check whether the sequent left -> right is derivable in scK."""
    global prooftree
    if isAxiom(left, right):
        history = []
        if recorded:
            s = Sequent()
            n = Node(s)
            if axiomF(left):
                n.set_rule('$f\\Rightarrow^\\ast$')
            else:
                n.set_rule('$Axiom^\\ast$')
            current_node.add_child(n)
        return True
    
    else:
        appended2 = True
        while appended2:
            appended2 = False
            appended = True
            while appended:
                appended, left =ruleAnd(left)
                if appended and recorded:
                    s = Sequent()
                    s.set_sequent(left, right)
                    n = Node(s)
                    n.set_rule('$\\land\\Rightarrow^\\ast$')
                    current_node.add_child(n)
                    current_node = n
                appended2 = appended2 or appended
            appended = True
            while appended:
                appended, right = ruleOr(right)
                if appended and recorded:
                    s = Sequent()
                    s.set_sequent(left, right)
                    n = Node(s)
                    n.set_rule('$\\Rightarrow\\lor^\\ast$')
                    current_node.add_child(n)
                    current_node = n
                appended2 = appended2 or appended
            appended = True
            considered = []
            while appended:
                appended, left, right, branch_imp, rule = ruleRImp(left, right, considered)
                if appended and recorded:
                    s = Sequent()
                    s.set_sequent(left, right)
                    n = Node(s)
                    n.set_rule('$\\rightarrow\\Rightarrow^\\ast_'+rule+'$')
                    current_node.add_child(n)
                    current_node = n                
                appended2 = appended2 or appended
            
        """ The following lines treats those rules, that either need a branching or that are not invertable
            which then needs a possibility to bachtrack. Branching comes before backtracking. """
        # the variable branching indicates, whether a branching rule can be applied
        branchings, left, right, formula = choseBranch(left, right)
        if branchings:
            if formula[0] == 0:
                lright, rright = branchAnd(right, formula[1])
                if recorded:
                    s1 = Sequent()
                    s1.set_sequent(left,lright)
                    n1 = Node(s1)
                    current_node.add_child(n1)
                    s2 = Sequent()
                    s2.set_sequent(left,rright)
                    n2 = Node(s2)
                    current_node.add_child(n2)
                    n1.set_rule('$\\Rightarrow\\land^\\ast$')
                    n2.set_rule('$\\Rightarrow\\land^\\ast$')
                    answer1 = derive(left[:],lright,history, recorded, n1)
                    answer2 = derive(left[:],rright, history, recorded, n2)
                else:
                    answer1 = derive(left[:],lright,history)
                    answer2 = derive(left[:],rright, history)
                return answer1 and answer2
 
            elif formula[0] == 1:
                lleft, rleft = branchOr(left, formula[1])
                if recorded:
                    s1 = Sequent()
                    s1.set_sequent(lleft,right)
                    n1 = Node(s1)
                    current_node.add_child(n1)
                    s2 = Sequent()
                    s2.set_sequent(rleft,right)
                    n2 = Node(s2)
                    current_node.add_child(n2)
                    n1.set_rule('$\\lor\\Rightarrow^\\ast$')
                    n2.set_rule('$\\lor\\Rightarrow^\\ast$')
                    answer1 = derive(lleft, right[:],history, recorded, n1)
                    answer2 = derive(rleft, right[:], history, recorded, n2)
                else:
                    answer1 = derive(lleft, right[:],history)
                    answer2 = derive(rleft, right[:], history)
                return answer1 and answer2

            else:
                lleft, lright, rleft = branchImp(left, right, formula[1])
                if recorded:
                    s1 = Sequent()
                    s1.set_sequent(lleft,lright)
                    n1 = Node(s1)
                    current_node.add_child(n1)
                    s2 = Sequent()
                    s2.set_sequent(rleft,right)
                    n2 = Node(s2)
                    current_node.add_child(n2)
                    n1.set_rule('$\\rightarrow\\Rightarrow^\\ast_4$')
                    n2.set_rule('$\\rightarrow\\Rightarrow^\\ast_4$')
                    answer1 = derive(lleft, lright,history, recorded, n1)
                    answer2 = derive(rleft, right[:],history, recorded, n2)
                else:
                    answer1 = derive(lleft, lright,history)
                    answer2 = derive(rleft, right[:],history)
                return answer1 and answer2
            
        else:  # and hence no branching rule can be applied
            rightImps = find_rightImps(right)
            number = len(rightImps)
            i=0
            while i<number:
                if right[i] in history:
                    i += 1
                    continue
                left2 = left[:]
                left2.append(rightImps[i][2])
                history.append(right[i])
                n = None
                if recorded:
                    s = Sequent()
                    s.set_sequent(left2, [rightImps[i][3]])
                    n=Node(s)
                    current_node.add_child(n)
                is_derivable = derive(left2, [rightImps[i][3]], history, recorded, n)
                if is_derivable:
                    if recorded:
                        n.set_rule('$\\Rightarrow\\rightarrow^\\ast$')
                    return True
                elif recorded:
                    current_node.remove_child(n)
                i += 1
                                
            if isAxiom(left, right):
                history = []
                if recorded:
                    s = Sequent()
                    n = Node(s)
                    if axiomF(left):
                        n.set_rule('$f\\Rightarrow^\\ast$')
                    else:
                        n.set_rule('$Axiom^\\ast$')
                    current_node.add_child(n)
                return True
            return False
 
def choseBranch(left, right):
    """ Choses the formula used for branch randomly and indicates, if there are any such formulas."""
    branch_formulas = []
    for formula in right:
        if formula[1] == '*':
            branch_formulas.append((0,formula))
    for formula in left:
        if formula[1] == '+':
            branch_formulas.append((1,formula))
        elif formula[1] == '->' and formula[2][1] == '->':
            branch_formulas.append((2,formula))
    number = len(branch_formulas)
    if number > 0:
        index = randint(0, number-1)
        formula = branch_formulas[index]
        if formula[0]==0:
            right.remove(formula[1])
        else:
            left.remove(formula[1])
        return True, left, right, formula
    return False, left, right, ()

def find_rightImps(right):
    """ The rule right implication is not invertable, hence all implications on the right side are collected and returned for further processing."""
    rightImps=[]
    for form in right:
        if form[1]=='->':
            rightImps.append(form)
    return rightImps
    
def isAxiom(left, right):
    """ Returns True, if left contains the constant F."""
    return axiomF(left) or axiomID(left,right)

def axiomF(left):
    """ Returns True, if right contains the constant T."""
    for elem in left:
        if elem[0]==0 and elem[1]=='F':
            return True
    return False

def axiomID(left, right):
    """ Returns True, if left and right contains the same formula."""
    for elem in left:
        if elem in right:
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

def ruleAnd(left):
    """ Replaces the first occurence of s*t,... in left by s,t,... . If no + in right then ruleOr(...)[0]=False."""
    for formula in left:
        if formula[1]=='*':
            left.remove(formula)
            left.append(formula[2])
            left.append(formula[3])
            return True, left
    return False, left

def ruleRImp(left, right,considered):
    """ Replaces the first occurence of s->t,... in left by something that depends on the structure of s."""
    for formula in left:
        if formula[1]=='->':
            if not formula in considered:
                if formula[2][0]==0 and formula[2] in left:
                    left.remove(formula)
                    left.append(formula[3])
                    rule = '1'
                    return True, left, right, considered, rule
                if formula[2][1] == '*':
                    left.remove(formula)
                    left.append((2,'->',formula[2][2],(2,'->',formula[2][3],formula[3])))
                    rule = '2'
                    return True, left, right,considered, rule
                if formula[2][1] == '+':
                    left.remove(formula)
                    left.append((2,'->',formula[2][2],formula[3]))
                    left.append((2,'->',formula[2][3],formula[3]))
                    rule = '3'
                    return True, left, right,considered, rule
            else:
                considered.append(formula)
                return True, left, right, considered, ''        
    return False, left, right,considered, ''

def branchAnd(right, formula):
    """ Makes the necessary modifications to the left and right sequent before appling an and-branch."""
    lright = right[:]
    rright = right[:]
    lright.append(formula[2])
    rright.append(formula[3])
    return lright, rright

def branchOr(left, formula):
    """ Makes the necessary modifications to the left and right sequent before appling an or-branch."""
    lleft = left[:]
    rleft = left[:]
    lleft.append(formula[2])
    rleft.append(formula[3])
    return lleft, rleft

def branchImp(left, right, formula):
    """ Makes the necessary modifications to the left and right sequent before appling an imp-branch."""
    lleft = left[:]
    lright = right[:]
    rleft = left[:]
    lleft.append((2,'->',formula[2][3],formula[3]))
    lright.append(formula[2])
    rleft.append(formula[3])
    return lleft, lright, rleft

def is_atom(formula):
    """ True, if formula is atomic."""
    return formula[0]==0

def remove_T_and_neg(formula):
    """ Transforms a formula that contains the constant T or negation into a formula in IL-syntax."""
    if formula[0]==0:
        if formula[1]=='T':
            return (2,'->',(0,'F'),(0,'F'))
        else:
            return formula
    elif formula[0]==1:
        if formula[1]=='-':
            return (2,'->',remove_T_and_neg(formula[2]),(0,'F'))
        else:
            print("Not well-defined formula for intuitionistic logic")
    elif formula[0]==2:
        return (2,formula[1],remove_T_and_neg(formula[2]),remove_T_and_neg(formula[3]))
        
def print_prooftree(filename = 'proof'):
    """ Generates a latex-file filename.tex in a separate directory proof, that contains a representation of the proof."""
    global prooftree
    prooftree.to_file(filename)


