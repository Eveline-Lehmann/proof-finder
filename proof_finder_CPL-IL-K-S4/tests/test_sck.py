import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest

from scK import *
from pigeonHole import generate_ph

def generate_valid_formulas():
    formula1 = (2, '+', (0, 'p'), (1, '-', (0, 'p')))
    formula2 = (2, '+', (2, '*', (0, 'p'), (0, 'q')), (1, '-', (2, '*', (0, 'p'), (0, 'q'))))
    formula3 = (2, '+', (2, '*', (0, 'p'), (0, 'q')), (1, '-', (2, '*', (0, 'q'), (0, 'p'))))    
    formula4 = (2, '+', (2, '+', (0, 'q'), (1, '-', (0, 'p'))), (0, 'p'))
    formula5 = (2, '+', (1, 'dia',(0,'p')),(1,'box',(1, '-',(0,'p'))))
    formula6 = (2, '+',(2,'+',(2, '+', (1, 'dia',(0,'p')),(1,'box',(1, '-',(0,'q')))),(1,'box',(1, '-',(0,'r')))),(1,'box',(1, '-',(0,'p'))))
    formula7 = (2, '->',(2, '*', (1, 'box',(0,'p')),(1, 'box',(0,'q'))), (1, 'box',(2, '*',(0,'p'),(0,'q'))))
    formula8 = (2, '->', (1, 'box',(2, '->',(0,'p'),(0,'q'))),(2, '->',(1,'box',(0,'p')),(1, 'box',(0,'q'))))
    formula9 = (2, '->', (2, '*', (1, 'box',(0, 'p')),(1, 'dia',(0,'q'))),(1, 'dia', (2, '*', (0,'p'),(0,'q'))))
    formula10 = (2, '->', (2, '*',(1, 'box',(1,'dia',(0,'p'))),(1, 'box', (1, 'box',(0,'q')))),(1, 'box',(1, 'dia',(2, '*',(0,'p'),(0,'q')))))
    axiom1 = (2, '->', (0, 'F'),(0, 'A'))
    axiom2 = (2, '->', (0, 'A'),(0, 'T'))
    axiom1 = (2, '->', (2, '*', (0,'p'),(1, '-', (0,'p'))),(0, 'A'))
    axiom2 = (2, '->', (0, 'A'),(2, '+',(0,'p'),(1, '-',(0,'p'))))
    axiom3 = (2, '->', (0,'A'),(0,'A'))
    axiom4 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(0,'a'),(0,'c'))))
    axiom5 = (2,'->',(2,'->',(0,'a'),(2,'->',(0,'b'),(0,'c'))),(2,'->',(2,'*',(0,'a'),(0,'b')),(0,'c')))
    axiom6 = (2,'->',(2,'->',(2,'*',(0,'a'),(0,'b')),(0,'c')),(2,'->',(0,'a'),(2,'->',(0,'b'),(0,'c'))))
    axiom7 = (2,'->',(0,'a'),(2,'+',(0,'a'),(0,'b')))
    axiom8 = (2,'->',(0,'b'),(2,'+',(0,'a'),(0,'b')))
    axiom9 = (2,'->',(2,'->',(0,'a'),(0,'c')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(2,'+',(0,'a'),(0,'b')),(0,'c'))))
    axiom10 = (2,'->',(2,'*',(0,'a'),(0,'b')),(0,'a'))
    axiom11 = (2,'->',(2,'*',(0,'a'),(0,'b')),(0,'b'))
    axiom12 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'a'),(0,'c')),(2,'->',(0,'a'),(2,'*',(0,'a'),(0,'b')))))
    axiom13 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(1,'-',(0,'b')),(1,'-',(0,'a'))))
    axiom14 = (2,'->',(0,'a'),(2,'->',(1,'-',(0,'a')),(0,'b')))
    axiom15 = (2,'->',(2,'->',(0,'a'),(2,'*',(0,'a'),(1,'-',(0,'a')))),(1,'-',(0,'a')))
    axiom16 = (2,'+',(0,'a'),(1,'-',(0,'a')))
    ph3 = generate_ph(3,True)
    ph4 = generate_ph(4, True)
    ph5 = generate_ph(5, True)
    ph6 = generate_ph(6, True)
   
    formulas = list()
    formulas.append(formula1)
    formulas.append(formula2)
    formulas.append(formula3)
    formulas.append(formula4)
    formulas.append(formula5)
    formulas.append(formula6)
    formulas.append(formula7)
    formulas.append(formula8)
    formulas.append(formula9)
    formulas.append(formula10)
    formulas.append(axiom1)
    formulas.append(axiom2)
    formulas.append(axiom3)
    formulas.append(axiom4)
    formulas.append(axiom5)
    formulas.append(axiom6)
    formulas.append(axiom7)
    formulas.append(axiom8)
    formulas.append(axiom9)
    formulas.append(axiom10)
    formulas.append(axiom11)
    formulas.append(axiom12)
    formulas.append(axiom13)
    formulas.append(axiom14)
    formulas.append(axiom15)
    formulas.append(axiom16)
    #formulas.append(ph3)
    #formulas.append(ph4)
    #formulas.append(ph5)
    #formulas.append(ph6)
    return formulas
    

def generate_nonvalid_formulas():
    formula1 = (2, '->', (2, '->', (0, 'p0'),(1, '-',(0,'p1'))), (2, '+', (1, '-', (0, 'p0')),(0, 'p1')))
    formula2 = (2, '+', (0, 'p'), (0, 'q'))
    formula3 = (2, '+', (0, 'q'), (0, 'p'))
    formula4 = (2, '*', (2, '+', (0, 'q'), (1, '-', (0, 'p'))), (1, '-', (0, 'p')))
    formula5 = (2, '*', (1, '-', (0, 'p')), (2, '+', (0, 'q'), (1, '-',(0, 'p'))))
    formula6 = (0, 'p')
    formula7 = (1, '-', (0, 'p'))
    formula8 = (1, '-', (1, '-',(0, 'p')))
    formula9 = (2, '->', (0, 'p0'),(1, '-',(0,'p1')))
    formula10 = (2, '+', (1, '-', (0, 'p0')),(0, 'p1'))
    ph3 = generate_ph(3, False)
    ph4 = generate_ph(4, False)
    ph5 = generate_ph(5, False)

    formulas = list()
    formulas.append(formula1)
    formulas.append(formula2)
    formulas.append(formula3)
    formulas.append(formula4)
    formulas.append(formula5)
    formulas.append(formula6)
    formulas.append(formula7)
    formulas.append(formula8)
    formulas.append(formula9)
    formulas.append(formula10)
#    formulas.append(ph3)
#    formulas.append(ph4)
#    formulas.append(ph5)
    return formulas

def generate_rubbish():
    rubb1 = (2, ' ', (2, '+', (0, 'q'), (1, '-', (0, 'p'))), (1, '-', (0, 'p'))) # wrong op
    rubb2 = (2, '*', (2, '+', (1, '-', (0, 'p'))), (1, '-', (0, 'p'))) #not enough arguments
    rubb3 = (2, '*', (2, '+', (0, 'q'), (1, '-', (0, 'p')), (0,'p')), (1, '-', (0, 'p'))) #too many arguments
    
    rubbish = list()
    rubbish.append(rubb1)
    rubbish.append(rubb2)
    rubbish.append(rubb3)
    
    return rubbish
    

class myTests(unittest.TestCase):
    formulas = generate_valid_formulas()
    nvFormulas = generate_nonvalid_formulas()
    rubbish = generate_rubbish()
    
    def testWellDefined(self):
        for elem in self.formulas:
            self.assertTrue(is_welldefined(elem))
        for elem in self.nvFormulas:
            self.assertTrue(is_welldefined(elem))        
        for elem in self.rubbish:
            self.assertFalse(is_welldefined(elem))
            
    def testAxiomTrue(self):
        formulas1 = [(2, '->', (0, 'F'),(0, 'A')), (2, '->', (0, 'A'),(0, 'T')), (0,'T')]
        self.assertTrue(axiomTrue(formulas1))
        formulas2 = [(2, '->', (0, 'F'),(0, 'A')), (2, '->', (0, 'A'),(0, 'T'))]
        self.assertFalse(axiomTrue(formulas2))
        
    def testAxiomID(self):
        formulas1 = [(2, '->', (0, 'F'),(0, 'A')), (2, '->', (0, 'A'),(0, 'T')), (1,'-',(2, '->', (0, 'A'),(0, 'T')))]
        self.assertTrue(axiomID(formulas1))
        formulas2 = [(2, '->', (0, 'F'),(0, 'A')), (2, '->', (0, 'A'),(0, 'T')), (0,'T')]
        self.assertFalse(axiomID(formulas2))

    def testRuleOr(self):
        left1 = [(2, '->', (0, 'F'),(0, 'A')), (2, '->', (0, 'A'),(0, 'T')), (1,'-',(2, '->', (0, 'A'),(0, 'T')))]
        right1 = [(2, '+', (0,'a'),(0,'b')), (2, '->', (0, 'F'),(0, 'A'))]
        right1_new = [(2, '->', (0, 'F'),(0, 'A')),(0,'a'),(0,'b')]
        self.assertEqual(ruleOr(right1), (True, right1_new))
         

    def testIsDerivable(self):
        for elem in self.formulas:
            self.assertTrue(derivable(elem, False))
        for elem in self.nvFormulas:
            self.assertFalse(derivable(elem, False))    
    
    def testNNF(self):
        axiom4 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(0,'a'),(0,'c'))))
        nnf_axiom4 = (2, '+', (2, '*', (0, 'a'), (1, '-', (0, 'b'))), (2, '+', (2, '*', (0, 'b'), (1, '-', (0, 'c'))), (2, '+', (1, '-', (0, 'a')), (0, 'c'))))
        self.assertEqual(nnf(axiom4), nnf_axiom4)
        formula1 = (2, '->', (2, '->', (0, 'p'),(1, '-',(0,'q'))), (2, '+', (1, '-', (0, 'p')),(0, 'q')))
        nnf_f1 = (2, '+',(2, '*',(0,'p'),(0, 'q')),(2, '+',(1, '-',(0, 'p')),(0, 'q')))
        self.assertEqual(nnf(formula1),nnf_f1)
        formula2 = (1, 'dia', (2, '+', (0,'a'),(0,'b')))
        self.assertEqual(nnf(formula2),formula2)
        formula3 = (2,'->',(2,'->',(1,'dia',(0,'a')),(0,'b')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(0,'a'),(0,'c'))))
        nnf_formula3 = (2, '+', (2, '*', (1,'dia',(0, 'a')), (1, '-', (0, 'b'))), (2, '+', (2, '*', (0, 'b'), (1, '-', (0, 'c'))), (2, '+', (1, '-', (0, 'a')), (0, 'c'))))
        self.assertEqual(nnf(formula3), nnf_formula3)        
        
if __name__=="__main__":
    unittest.main()

