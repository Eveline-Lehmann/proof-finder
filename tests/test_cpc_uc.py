import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest

from cpc_uc import *
from pigeonHole import generate_ph

def generate_valid_formulas():
    formula1 = (2, '+', (0, 'p'), (1, '-', (0, 'p')))
    formula2 = (2, '+', (2, '*', (0, 'p'), (0, 'q')), (1, '-', (2, '*', (0, 'p'), (0, 'q'))))
    formula3 = (2, '+', (2, '*', (0, 'p'), (0, 'q')), (1, '-', (2, '*', (0, 'q'), (0, 'p'))))    
    formula4 = (2, '+', (2, '+', (0, 'q'), (1, '-', (0, 'p'))), (0, 'p'))
    axiom1 = (2, '->', (0, 'F'),(0, 'A'))
    axiom2 = (2, '->', (0, 'A'),(0, 'T'))
    axiom3 = (2, '->', (2, '*', (0,'p'),(1, '-', (0,'p'))),(0, 'A'))
    axiom4 = (2, '->', (0, 'A'),(2, '+',(0,'p'),(1, '-',(0,'p'))))
    axiom5 = (2, '->', (0,'A'),(0,'A'))
    axiom6 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(0,'a'),(0,'c'))))
    axiom7 = (2,'->',(2,'->',(0,'a'),(2,'->',(0,'b'),(0,'c'))),(2,'->',(2,'*',(0,'a'),(0,'b')),(0,'c')))
    axiom8 = (2,'->',(2,'->',(2,'*',(0,'a'),(0,'b')),(0,'c')),(2,'->',(0,'a'),(2,'->',(0,'b'),(0,'c'))))
    axiom9 = (2,'->',(0,'a'),(2,'+',(0,'a'),(0,'b')))
    axiom10 = (2,'->',(0,'b'),(2,'+',(0,'a'),(0,'b')))
    axiom11 = (2,'->',(2,'->',(0,'a'),(0,'c')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(2,'+',(0,'a'),(0,'b')),(0,'c'))))
    axiom12 = (2,'->',(2,'*',(0,'a'),(0,'b')),(0,'a'))
    axiom13 = (2,'->',(2,'*',(0,'a'),(0,'b')),(0,'b'))
    axiom14 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'a'),(0,'c')),(2,'->',(0,'a'),(2,'*',(0,'a'),(0,'b')))))
    axiom15 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(1,'-',(0,'b')),(1,'-',(0,'a'))))
    axiom16 = (2,'->',(0,'a'),(2,'->',(1,'-',(0,'a')),(0,'b')))
    axiom17 = (2,'->',(2,'->',(0,'a'),(2,'*',(0,'a'),(1,'-',(0,'a')))),(1,'-',(0,'a')))
    axiom18 = (2,'+',(0,'a'),(1,'-',(0,'a')))
    ph3 = generate_ph(3,True)
    ph4 = generate_ph(4, True)
    ph5 = generate_ph(5, True)
    ph6 = generate_ph(6, True)
   
    formulas = list()
    formulas.append(formula1)
    formulas.append(formula2)
    formulas.append(formula3)
    formulas.append(formula4)
    #formulas.append(axiom1)
    #formulas.append(axiom2)
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
    formulas.append(axiom17)
    formulas.append(axiom18)
    formulas.append(ph3)
    formulas.append(ph4)
 #   formulas.append(ph5)
 #   formulas.append(ph6)
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
    formulas.append(ph3)
    formulas.append(ph4)
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
    
    def testIsDerivable(self):
        for elem in self.formulas:
            self.assertTrue(derivable(elem))
        for elem in self.nvFormulas:
            self.assertFalse(derivable(elem))
            
    def testCPCprovable(self):
        gamma = {(0, 'p')}
        delta = {(0, 'p')}
        self.assertTrue(cpc_provable_uc(gamma, delta))
        gamma = {(2,'*',(0, 'p'),(0, 'q'))}
        delta = {(2, '+', (0, 'p'), (0, 'r'))}
        self.assertTrue(cpc_provable_uc(gamma, delta))
        gamma = set()
        delta = cf((2, '->', (2, '->', (0, 'p0'),(1, '-',(0,'p1'))), (2, '+', (1, '-', (0, 'p0')),(0, 'p1'))))
        delta1 = {delta}
        self.assertFalse(cpc_provable_uc(gamma, delta1))
        
        
    def testMaxLabel(self):
        gamma_b = {(0, 3),(2, 5), (3, 1),(2,6)}
        delta_b = {(1, 3),(4, 5), (3, 1),(2,6)}        
        gamma_a = {(6, 3),(2, 5), (3, 1),(2,6)}
        delta_a = {(2, 3),(2, 5), (5, 1),(2,6)}
        self.assertEqual(maxLabel(gamma_b, delta_b, gamma_a, delta_a),6)
        
if __name__=="__main__":
    unittest.main()
