import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest

import scK, s4, cpc_uc as cl
from parsingString import *

def generate_formulas():
    f1 = 'F->a'
    f2 = 'a->T'
    f3 = 'a->a'
    f4 = '(a->b)->((b->c)->(a->c))'
    f5 = '(a->(b->c))->((a*b)->c)'
    f6 = '((a*b)->c)->(a->(b->c))'
    f7 = 'a->(a+b)'
    f8 = 'b->(a+b)'
    
    formulas = list()
    formulas.append(f1)
    formulas.append(f2)
    formulas.append(f3)
    formulas.append(f4)
    formulas.append(f5)
    formulas.append(f6)
    formulas.append(f7)
    formulas.append(f8)
    return formulas

class myTests(unittest.TestCase):
    formulas = generate_formulas()
    
    def testWellDefined(self):
        for elem in self.formulas:
            self.assertTrue(cl.is_welldefined(string2formula(elem)))


    def testIsDerivable(self):
        for elem in self.formulas:
            self.assertTrue(cl.derivable(string2formula(elem)))

        
if __name__=="__main__":
    unittest.main()


