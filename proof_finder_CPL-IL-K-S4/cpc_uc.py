#-------------------------------------------------------
# Programm to test derivability of modal formulas in CL
#
# (C) 2020 Eveline Lehmann, Bern, Switzerland
# Released under GNU Public License (GPL)
# email eveline.lehmann@inf.unibe.ch
#-------------------------------------------------------

from graph import *


""" The variable prooftree records the derivation process in scK."""
prooftree = ProofTree()

def get_prooftree():
    global prooftree
    return prooftree

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    
    return helper

""" Checks the validity of a formula. The formula may be given with the logical operators +, *, -> and negation. """
def derivable(formula, recorded=False):
    form  = cf(formula)
    return cpc_provable_uc(set(),{form},recorded)

""" Checks validity of a sequent. The procedure follows the proof search algorithm with use-check presented
    in the phd-thesis of Peppo Brambilla p.34. """
def cpc_provable_uc(gamma, delta, recorded=False):
    global prooftree
    gamma1 = {(0,a) for a in gamma}  # 0 indicates branching depth. See function branch
    delta1 = {(0,a) for a in delta}  # dito
    if recorded:
        prooftree = ProofTree()
        s1 = Sequent()
        l_gamma = list(gamma)
        l_delta = list(delta)
        s1.set_sequent(l_gamma,l_delta)
        n1 = Node(s1)
        prooftree.set_root(n1)
        current_node = n1
        labels = classify(gamma1, delta1, set(), set(), set(), set(), True, recorded, current_node)
    else:
        labels = classify(gamma1, delta1, set(), set(), set(), set(), True)
    return not len(labels)==0

""" classifies formulas whether they are treated as conjunctions, disjunctions, negations or atomic and treats them
    accordingly depending whether they are in the left or right part of the sequent.
    The boolean flag is used to switch between the two sides. """
@call_counter
def classify(gamma_c1, delta_c1, gamma_b1, delta_b1, gamma_a1, delta_a1, flag,recorded=False, current_node = None):
    global prooftree
    gamma_c = gamma_c1.copy()
    delta_c = delta_c1.copy()
    gamma_b = gamma_b1.copy()
    delta_b = delta_b1.copy()  
    gamma_a = gamma_a1.copy()
    delta_a = delta_a1.copy()
    lengc = len(gamma_c)
    lendc = len(delta_c)
    new = False
    if lengc + lendc>0:
        if (flag and lengc>0) or lendc == 0:
            a = gamma_c.pop()
            if a[1][0]==1 and a[1][1]=='-':  # a = -b
                delta_c.add((a[0],a[1][2]))
                new = True
                rule = '$\\neg\\supset$'
            elif a[1][0]==2 and a[1][1]=='*':  # a = b*c
                gamma_c.add((a[0],a[1][2]))
                gamma_c.add((a[0],a[1][3]))
                new = True
                rule = '$\\land\\supset$'
            elif a[1][0]==0:  # a is atomic
                gamma_a.add(a)
            else:             # a = b+c and needs branch
                gamma_b.add(a)
        else:
       # elif (not flag and lendc>0) or lengc == 0:    
            a = delta_c.pop()
            if a[1][0]==1 and a[1][1]=='-':  # a = -b
                gamma_c.add((a[0],a[1][2]))
                new = True
                rule = '$\\supset\\neg$'
            elif a[1][0]==2 and a[1][1]=='+': # a = b+c
                delta_c.add((a[0],a[1][2]))
                delta_c.add((a[0],a[1][3]))
                new = True
                rule = '$\\supset\\lor$'
            elif a[1][0]==0:  # a is atomic
                delta_a.add(a)  
            else:             # a = b*c and needs branch
                delta_b.add(a)
        
        if recorded and new:
            s = Sequent()
            gamma = generateList(gamma_a, gamma_b, gamma_c)
            delta = generateList(delta_a, delta_b, delta_c)
            s.set_sequent(gamma,delta)
            n = Node(s)
            n.set_rule(rule)
            current_node.add_child(n)
            current_node = n
        
        axiom, principal, rule = is_axiom(gamma_a, delta_a)
        if axiom:
            labels = set(principal) #[0], principal[1]}
            if recorded:
                s = Sequent()
                n = Node(s)
                n.set_rule(rule)
                current_node.add_child(n)
        else:
            labels = classify(gamma_c, delta_c, gamma_b, delta_b, gamma_a, delta_a, not flag, recorded, current_node)
    elif len(gamma_b | delta_b)>0:
        labels = branch(gamma_b, delta_b, gamma_a, delta_a, flag, recorded, current_node)
    else:
        labels = set()
    return labels

""" This function calculates the branches and keeps track of the formulas used to deduce an axiom.
    This is done by carrying a list of labels that indicate at which depth of branching some formula
    was added to some of the sets. For more details see Brambilla, p. 33-36. """
def branch(gamma_b, delta_b, gamma_a, delta_a, flag, recorded=False, current_node=False):
    global prooftree
    n = maxLabel(gamma_b, delta_b, gamma_a, delta_a)+1
    if (flag and len(gamma_b)>0) or len(delta_b) == 0:
        a = gamma_b.pop()
        b = a[1][2]
        c = a[1][3]
        if recorded:
            s1 = Sequent()
            s1.set_sequent(generateList(gamma_b,gamma_a,{(0,b)}),generateList(delta_b,delta_a,set()))
            n1 = Node(s1)
            n1.set_rule('$\\lor\\supset$')
            current_node.add_child(n1)
            s2 = Sequent()
            s2.set_sequent(generateList(gamma_b,gamma_a,{(0,c)}),generateList(delta_b,delta_a,set()))
            n2 = Node(s2)
            n2.set_rule('$\\lor\\supset$')
            current_node.add_child(n1)
            current_node = n1
        labels1 = classify({(n, b)},set(),gamma_b, delta_b, gamma_a, delta_a, flag, recorded, current_node)
        if n in labels1:
            if recorded:
                current_node = n2
            labels2 = classify({(n, c)}, set(),gamma_b, delta_b, gamma_a, delta_a, flag, recorded, current_node)
            if n in labels2:
                labels = labels1 | labels2 | {a[0]} - {n}
            else:
                labels = labels2
        else:
            labels = labels1
    else:
        a = delta_b.pop()
        b = a[1][2]
        c = a[1][3]
        if recorded:
            s1 = Sequent()
            s1.set_sequent(generateList(gamma_b,gamma_a,set()),generateList(delta_b,delta_a,{(0,b)}))
            n1 = Node(s1)
            n1.set_rule('$\\supset\\land$')
            current_node.add_child(n1)
            s2 = Sequent()
            s1.set_sequent(generateList(gamma_b,gamma_a,set()),generateList(delta_b,delta_a,{(0,c)}))
            n2 = Node(s2)
            n2.set_rule('$\\supset\\land$')
            current_node.add_child(n1)
            current_node = n1
        labels1 = classify(set(), {(n, b)},gamma_b, delta_b, gamma_a, delta_a, flag, recorded, current_node)
        if n in labels1:
            if recorded:
                current_node = n2
            labels2 = classify(set(), {(n, c)},gamma_b, delta_b, gamma_a, delta_a, flag, recorded, current_node)
            if n in labels2:
                labels = labels1 | labels2 | {a[0]} - {n}
            else:
                labels = labels2
        else:
            labels = labels1 
    return labels



""" calculates the highest value of branching depth for all formulas occuring in one of the sets """
def maxLabel(gamma_b, delta_b, gamma_a, delta_a):
    maximum = 0
    for form in gamma_b | delta_b | gamma_a | delta_a:
        if form[0] > maximum:
            maximum = form[0]
    return maximum

""" There is only one axiom, i.e. that an atomic formula occures on both sides of a sequent.
    If there is one, the functions returns True and gives the branching depth of the two corresponding atoms """
def is_axiom(gamma_a, delta_a):
    gamma_a_list = list(gamma_a)
    delta_a_list = list(delta_a)
    for elem in delta_a_list:
        if elem[1] == (0,'T'):
            return True, [elem[0]], '$\top$'
    for  i in range(len(gamma_a)):
        for j in range(len(delta_a)):
            if gamma_a_list[i][1] == delta_a_list[j][1]:
                return True, [gamma_a_list[i][0], delta_a_list[j][0]], 'id'
    return False, [],''

def is_atom(formula):
    return formula[0]==0

""" Checks, whether a formula has the correct form
    @formula: a tuple that indicates in index 0 the arity, in index 1 the operator if it exists and
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
            return (formula[1]=='+' or formula[1]=='*' or formula[1]=='->') and is_welldefined(formula[2]) and is_welldefined(formula[3])
        else:
            return False
    except AssertionError:
        print("formula must be given as a list of 2 (in case of an atom),\n"+
              "3 (in case of a negation or a modal) or 4 (in case of a binary operator) elements,\n"+
              "such that \n at index 0: 0 if atom, the arity of the operator otherwise"+
            "\n at index 1: the operation symbol '-', '+', '*', '->' or a string in case of an atom"+
              "\n at index 2: another list according to these rules, representing the first argument of the operation "+
              "\n at index 3: another list according to these rules, representing the second argument of the operation")
    
""" converts a formula given as a well-defined tuple into a formula in
    the correct Form, i.e. without implications."""
def cf(formula):
    try:
        assert is_welldefined(formula)
        formula = removeImplications(formula)
        return formula
    except AssertionError:
        print("This is not a formula according to this application!")

def removeImplications(formula):
    if formula == (0,'F'):
        return (1,'-',(0,'T'))
    # atoms and negation on atoms remain the same
    elif is_atom(formula) or (formula[0]==1 and is_atom(formula[2])):
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
        elif formula[1]=='->':
            return (2, '+', (1, '-', removeImplications(formula[2])), removeImplications(formula[3]))
    else:
        return formula

        
def generateList(set1, set2, set3):
    liste = [a[1] for a in set1]
    liste.extend([a[1] for a in set2])
    liste.extend([a[1] for a in set3])
    return liste


def print_prooftree(filename = 'proof'):
    """ Generates a latex-file filename.tex in a separate directory proof, that contains a representation of the proof."""
    global prooftree
    prooftree.to_file(filename)