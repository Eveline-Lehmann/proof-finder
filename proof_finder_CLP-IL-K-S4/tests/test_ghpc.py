import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import unittest

from ghpc_branching_first import *
#from ghpc_backtracking_first import *
from pigeonHole import generate_ph

def generate_valid_formulas():
    a1 = (2,'->',(0,'p'),(2,'->',(0,'q'),(0,'p')))
    a2 = (2,'->',(2,'->',(0,'p'),(2,'->',(0,'q1'),(0,'q2'))),(2,'->',(2,'->',(0,'p'),(0,'q1')),(2,'->',(0,'p'),(0,'q2'))))
    a3 = (2,'->',(2,'*',(0,'p'),(0,'q')),(0,'p'))
    a4 = (2,'->',(2,'*',(0,'p'),(0,'q')),(0,'q'))
    a5 = (2,'->',(0,'p'),(2,'->',(0,'q'),(2,'*',(0,'p'),(0,'q'))))
    a6 = (2,'->',(0,'p'),(2,'+',(0,'p'),(0,'q')))
    a7 = (2,'->',(0,'q'),(2,'+',(0,'p'),(0,'q')))
    a8 = (2,'->',(2,'->',(0,'p1'),(0,'q')),(2,'->',(2,'->',(0,'p2'),(0,'q')),(2,'->',(2,'+',(0,'p1'),(0,'p2')),(0,'q'))))
    a9 = (2,'->',(0,'F'),(0,'p'))
    formula1 = (2,'->',(0,'p'),(2,'->',(0,'q'),(0,'p')))
    formula2 = (2, '->', (0, 'A'),(0, 'T'))
    formula3 = (2, '->', (2, '*', (0,'p'),(2, '->', (0,'p'),(0,'F'))),(0, 'A'))
    formula4 = (2, '->', (0,'A'),(0,'A'))
    formula5 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(0,'a'),(0,'c'))))
    formula6 = (2,'->',(2,'->',(0,'a'),(2,'->',(0,'b'),(0,'c'))),(2,'->',(2,'*',(0,'a'),(0,'b')),(0,'c')))
    formula7 = (2,'->',(2,'->',(2,'*',(0,'a'),(0,'b')),(0,'c')),(2,'->',(0,'a'),(2,'->',(0,'b'),(0,'c'))))
    formula8 = (2,'->',(0,'a'),(2,'+',(0,'a'),(0,'b')))
    formula9 = (2,'->',(0,'b'),(2,'+',(0,'a'),(0,'b')))
    formula10 = (2,'->',(2,'->',(0,'a'),(0,'c')),(2,'->',(2,'->',(0,'b'),(0,'c')),(2,'->',(2,'+',(0,'a'),(0,'b')),(0,'c'))))
    formula11 = (2,'->',(2,'*',(0,'a'),(0,'b')),(0,'a'))
    formula12 = (2,'->',(2,'*',(0,'a'),(0,'b')),(0,'b'))
    formula13 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'a'),(0,'c')),(2,'->',(0,'a'),(2,'*',(0,'a'),(0,'b')))))
    formula14 = (2,'->',(2,'->',(0,'a'),(0,'b')),(2,'->',(2,'->',(0,'b'),(0,'F')),(2,'->',(0,'a'),(0,'F'))))
    formula15 = (2,'->',(0,'a'),(2,'->',(2,'->',(0,'a'),(0,'F')),(0,'b')))
    formula16 = (2,'->',(2,'->',(0,'a'),(2,'*',(0,'a'),(2,'->',(0,'a'),(0,'F')))),(2,'->',(0,'a'),(0,'F')))
    formula17 = (2,'+',(2,'->',(0,'a'),(0,'b')),(2,'->',(0,'p'),(0,'p')))
    ph3 = generate_ph(3,True)
    ph4 = generate_ph(4, True)
    ph5 = generate_ph(5, True)
    ph6 = generate_ph(6, True)
   
    formulas = list()
    formulas.append(a1)
    formulas.append(a2)
    formulas.append(a3) 
    formulas.append(a4) 
    formulas.append(a5)
    formulas.append(a6)
    formulas.append(a7)
    formulas.append(a8) 
    formulas.append(a9)
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
    formulas.append(formula11)
    formulas.append(formula12) 
    formulas.append(formula13) 
    formulas.append(formula14)
    formulas.append(formula15) 
    formulas.append(formula16)
    formulas.append(formula17) 
    formulas.append(ph3)
#    formulas.append(ph4)
#    formulas.append(ph5)
#    formulas.append(ph6)
    return formulas
    

def generate_nonvalid_formulas():    
    formula1 = (2, '->', (2, '->', (0, 'p0'),(2, '->',(0,'p1'),(0,'F'))), (2, '+', (2, '->', (0, 'p0'),(0,'F')),(0, 'p1')))
    formula2 = (2, '+', (0, 'p'), (0, 'q'))
    formula3 = (2, '+', (0, 'q'), (0, 'p'))
    formula4 = (2, '*', (2, '+', (0, 'q'), (2, '->', (0, 'p'),(0,'F'))), (2, '->', (0, 'p'),(0,'F')))
    formula5 = (2, '*', (2, '->', (0, 'p'),(0,'F')), (2, '+', (0, 'q'), (2, '->',(0, 'p'),(0,'F'))))
    formula6 = (0, 'p')
    formula7 = (2, '->', (0, 'p'),(0,'F'))
    formula8 = (2, '->', (2, '->',(0, 'p'),(0,'F')),(0,'F'))
    formula9 = (2, '->', (0, 'p0'),(2, '->',(0,'p1'),(0,'F')))
    formula10 = (2, '+', (1, '-', (0, 'p0')),(0, 'p1'))
    formula11 = (2, '->', (0, 'A'),(2, '+',(0,'p'),(2, '->',(0,'p'),(0,'F'))))
    formulaN1 = (2, '+', (0, 'p'), (2, '->', (0, 'p'),(0,'F')))
    formulaN2 = (2, '+', (2, '*', (0, 'p'), (0, 'q')), (2, '->', (2, '*', (0, 'p'), (0, 'q')),(0,'F')))
    formulaN3 = (2, '+', (2, '*', (0, 'p'), (0, 'q')), (2, '->', (2, '*', (0, 'q'), (0, 'p')),(0,'F')))
    formulaN4 = (2, '+', (2, '+', (0, 'q'), (2, '->', (0, 'p'),(0,'F'))), (0, 'p'))
    formulaN5 = (2, '+', (1, 'dia',(0,'p')),(1,'box',(1, '-',(0,'p'))))
    formulaN6 = (2, '+',(2,'+',(2, '+', (1, 'dia',(0,'p')),(1,'box',(1, '-',(0,'q')))),(1,'box',(1, '-',(0,'r')))),(1,'box',(1, '-',(0,'p'))))
    formulaN7 = (2, '->',(2, '*', (1, 'box',(0,'p')),(1, 'box',(0,'q'))), (1, 'box',(2, '*',(0,'p'),(0,'q'))))
    formulaN8 = (2, '->', (1, 'box',(2, '->',(0,'p'),(0,'q'))),(2, '->',(1,'box',(0,'p')),(1, 'box',(0,'q'))))
    formulaN9 = (2, '->', (2, '*', (1, 'box',(0, 'p')),(1, 'dia',(0,'q'))),(1, 'dia', (2, '*', (0,'p'),(0,'q'))))
    formulaN10 = (2, '->', (2, '*',(1, 'box',(1,'dia',(0,'p'))),(1, 'box', (1, 'box',(0,'q')))),(1, 'box',(1, 'dia',(2, '*',(0,'p'),(0,'q')))))
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
    formulas.append(formula11)
    formulas.append(formulaN1)
    formulas.append(formulaN2)
    formulas.append(formulaN3)
    formulas.append(formulaN4)
    formulas.append(formulaN5)
    formulas.append(formulaN6)
    formulas.append(formulaN7)
    formulas.append(formulaN8)
    formulas.append(formulaN9)
    formulas.append(formulaN10)
    formulas.append(ph3)
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
                 

    def testIsDerivable(self):
        for i in range(1):
            for elem in self.formulas:
                self.assertTrue(derivable(elem))
        for elem in self.nvFormulas:
            self.assertFalse(derivable(elem))
            
if __name__=="__main__":
    unittest.main()




