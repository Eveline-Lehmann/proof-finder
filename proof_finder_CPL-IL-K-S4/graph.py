#-------------------------------------------------------
# Programm to represent scK-proofs in a ProofTree
#
# (C) 2020 Eveline Lehmann, Bern, Switzerland
# Released under GNU Public License (GPL)
# email eveline.lehmann@inf.unibe.ch
#-------------------------------------------------------

import os

""" A Sequent is a list of two lists, each of them containing several formulas given as tuples.
    This for of sequence corresponds to the one used in scK-recorded_graph (see is_welldefined(...) there).
    A sequent has the usual getters and setters and a self-representation as string in latex-code."""
class Sequent:
    """ Two-sided sequent based on two lists of tupels."""
    def __init__(self):
        self.__sequent = [[],[]]
        self.__string = ""
        
    def set_sequent(self, left, right):
        self.__sequent = [left, right]
        self.update_string()
        
    def get_sequent(self):
        return self.__sequent
    
    def get_string(self):
        return self.__string
    
    def update_string(self):
        """ Generates a string from left,right to latex(left)latex($\supset$)latex(right)."""
        def op2string(op):
            if op == '-':
                return '$\\neg$'
            elif op == '+':
                return '$\lor$'
            elif op == '*':
                return '$\land$'
            elif op == '->':
                return '$\\to$'
            elif op == 'box':
                return '$\Box$'
            elif op == 'dia':
                return '$\Diamond$'
            else:
                return '...'
                
        def string2(old, form):
            if not form:
                return ""
            if form[0] == 0:
                return old + form[1]
            elif form[0] == 1:
                return old + op2string(form[1]) + ' ' + string2('',form[2])
            elif form[0] == 2:
                return old + '('+string2('',form[2]) + ' '+ op2string(form[1]) + ' ' + string2('',form[3])+')'
            else:
                return ""

        def sequent2string(formula_list):
            if not formula_list:
                return ''
            else:
                result = string2('',formula_list[0])
                for i in range(1,len(formula_list)):
                    result = result + ','+ string2('',formula_list[i])
                return result
        
        if self.__sequent[0] or self.__sequent[1]:
            self.__string = sequent2string(self.__sequent[0]) + " $\supset $ " + sequent2string(self.__sequent[1])
        else:
            self.__string = ''
        
    
""" Represents a node that contains a sequent named __formula according to Sequent, a rule, representing the rule that was needed to
    achieve this node, a parent Node and a list of nodes denotes as children. Its string representation is the string-representation
    of its formula. """
class Node:
    """ Class that represents a node in a prooftree. Contains a sequent and a list of its children nodes."""
    def __init__(self, sequent = None):
        self.__sequent = sequent
        self.__rule = ""
        self.__parent = None
        self.__children = []
        
    def set_sequent(self, sequent):
        self.__sequent = sequent
        
    def get_sequent(self):
        return self.__sequent
    
    def set_rule(self, rule):
        self.__rule = rule
        
    def get_rule(self):
        return self.__rule
    
    def add_child(self, child):
        self.__children.append(child)
        
    def remove_child(self, child):
        if child in self.__children:
            self.__children.remove(child)
        
    def set_children(self, children):
        self.__children.extend(children)
        
    def get_children(self):
        return self.__children
    
    def get_number_of_children(self):
        return len(self.__children)
    
    def is_leaf(self):
        return len(self.__children) == 0
    
    def to_string(self):
        return self.__sequent.to_string()

""" Class that represents a ProofTree in scK (see derivable in scK_recorded_graph). Contains a
    function to_file(), which generates a latex-file of the prooftree. Please check, that the
    corresponding files picture_before and picture-after are available in the current directory."""
class ProofTree:
    """ Class that represents a ProofTree in scK."""
    def __init__(self, root = None):
        self.__root = root
        self.__length = 0
        
    def set_root(self, root):
        self.__root = root
        
    def get_root(self):
        return self.__root
    
    def is_root(self, node):
        return self.__root == node
    
    def to_string(self):
        result = self.__root.to_string()
        current_node = self.__root
        current_sibling = None
        while not current_node.is_leaf():
            pass
        
    def to_file(self, filename = 'proof_to_picture.tex', directory = '.'):
        """ Generates a latex-file named [filename].tex in directory proof containing a bussproofs representation of the prooftree."""        
        filename1 = filename.split('.',1)[0]
        filename = filename1+'.tex'
        before = open('text_intro', 'r')
        after = open('text_end', 'r')

        if not os.path.isdir('./proof'): 
            os.mkdir('proof')
        os.chdir("./proof")  # change to (new) directory proof
        
        picture = open(filename,'w')
        
        for line in before.readlines():
            picture.write(line)
        
        # generate a latex string by using bussproofs syntax and scanning the prooftree
        result = "" 
        stack = [[self.__root,self.__root.get_number_of_children(),False]]
        while stack:
            current = stack[-1]
            wrapper_list = [r"\AxiomC{",r"\UnaryInfC{",r"\BinaryInfC{"]
            wrapper = wrapper_list[current[0].get_number_of_children()]
            if not current[2]:
                result = wrapper + current[0].get_sequent().get_string() +"}"+  "\n\RightLabel{("+current[0].get_rule()+")}"+  '\n'+ result
                current[2] = True
            if current[1]:
                current[1] -= 1
                child = current[0].get_children()[current[1]]
                stack.append([child,child.get_number_of_children(), False])
            else:
                stack.pop()
       
        picture.write(result)
        
        for line in after.readlines():
            picture.write(line)
            
        os.chdir("..")   # change again to parent directory    