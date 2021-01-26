import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

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
    formulas.append(axiom17)
    formulas.append(axiom18)
    formulas.append(ph3)
 #   formulas.append(ph4)
 #   formulas.append(ph5)
 #   formulas.append(ph6)
    return formulas
    
os.chdir('..')    

formulas = generate_valid_formulas()

number = 1

for elem in formulas:
    derivable(elem,True)
    filename = "cpc_uc_formula"+str(number)
    number += 1
    print_prooftree(filename)