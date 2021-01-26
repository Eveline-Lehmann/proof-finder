import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from s4 import *
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
    formula11 = (2, '->', (2, '->', (0, 'p0'),(1, '-',(0,'p1'))), (2, '+', (1, '-', (0, 'p0')),(0, 'p1')))
    formula12 = (2, '+', (0, 'p'), (0, 'q'))
    formula13 = (2, '+', (0, 'q'), (0, 'p'))
    formula14 = (2, '*', (2, '+', (0, 'q'), (1, '-', (0, 'p'))), (1, '-', (0, 'p')))
    formula15 = (2, '*', (1, '-', (0, 'p')), (2, '+', (0, 'q'), (1, '-',(0, 'p'))))
    formula16 = (0, 'p')
    formula17 = (1, '-', (0, 'p'))
    formula18 = (1, '-', (1, '-',(0, 'p')))
    formula19 = (2, '->', (0, 'p0'),(1, '-',(0,'p1')))
    formula20 = (2, '+', (1, '-', (0, 'p0')),(0, 'p1'))
    s4_1 = (2,'->',(1,'box',(0,'p')),(1,'dia',(0,'p')))
    s4_2 = (2, '->',(1,'box',(0,'p')),(1,'box',(1,'box',(0,'p'))))
    s4_3 = (2,'->',(1,'box',(0,'p')),(0,'p'))
    
    not_s4_B = (2,'->',(0,'p'),(1,'box',(1,'dia',(0,'p'))))
    not_s4_5 = (2,'->',(1,'dia',(0,'p')),(1,'box',(1,'dia',(0,'p'))))
   
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
    formulas.append(formula11)
    formulas.append(formula12)
    formulas.append(formula13)
    formulas.append(formula14)
    formulas.append(formula15)
    formulas.append(formula16)
    formulas.append(formula17)
    formulas.append(formula18)
    formulas.append(formula19)
    formulas.append(formula20)
    formulas.append(s4_1)
    formulas.append(s4_2)
    formulas.append(s4_3)
    formulas.append(not_s4_B)
    formulas.append(not_s4_5)
    return formulas
    
os.chdir('..')    

formulas = generate_valid_formulas()

number = 1

for elem in formulas:
    derivable(elem,True)
    filename = "s4_formula"+str(number)
    number += 1
    print_prooftree(filename)
    