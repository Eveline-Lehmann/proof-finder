import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import os, webbrowser
import tkinter.font as tkFont
import cpc_uc as cl, ghpc_branching_first as il, scK, s4
import graph
import ast
import parsingString as parsing

class Proof_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.green = '#A5D19B'#797D62'
        self.red = '#E48F9A'#E56B6F'
        self.c1 = '#656A8B'#826483'#9A8C98'
        self.c2 = '#E8DBCA'#F0EEFB'#C9AdA7'
        self.c3 = '#9198D5'#D0B0D0'#8A8EB9'
        self.c4 = '#FEFEFE'#F2E9E4'
        self.root.configure(bg=self.c1)

        self.root.geometry('1000x600')
        self.fontStyle = tkFont.Font(family="Helvetica", size=20)
        self.root.title('Proof Search, LTG Unibe')
        self.logic = tk.StringVar()
        self.logic.set('cl')
        self._formula = None
        self._formulaInput = False
        self._lastForm = False
        self._recorded = True
        self._proof_recorded = False
        self._fontStyle = tkFont.Font(family="Lucida Grande", size=14)
        self._headerStyle = tkFont.Font(family="Lucida Grande", size=26)
        self._init_widgets()
        self._proof_filename=None
        self._prooftree = None
        self._openTrees = []
        

    def _init_widgets(self):
        self.frame1=tk.Frame(self.root,bg=self.c1)
        self.frame1.pack(fill=tk.BOTH, expand=1,  padx=20)
        self.frame2=tk.Frame(self.root,bg=self.c2)
        self.frame2.pack(fill=tk.BOTH, expand=1,padx=20,pady=10)
        self.frame2l=tk.Frame(self.frame2,bg=self.c2)
        self.frame2l.pack(fill=tk.BOTH, expand=1, side = tk.LEFT,padx=20,pady=10)
        self.frame2r=tk.Frame(self.frame2,bg=self.c2)
        self.frame2r.pack(fill=tk.BOTH, expand=1, side = tk.LEFT,padx=20,pady=10)
        
        self.frame2l1=tk.Frame(self.frame2l,bg=self.c2)
        self.frame2l1.pack(fill=tk.BOTH, expand=1, pady=10)
        self.frame2l2=tk.Frame(self.frame2l,bg=self.c3)
        self.frame2l2.pack(fill=tk.BOTH, expand=1)
        self.frame2l3=tk.Frame(self.frame2l,bg=self.c3)
        self.frame2l3.pack(fill=tk.BOTH, expand=1)
        self.frame2l4=tk.Frame(self.frame2l,bg=self.c3)
        self.frame2l4.pack(fill=tk.BOTH, expand=1)
        
        self.frame2r1=tk.Frame(self.frame2r,bg=self.c2)
        self.frame2r1.pack(fill=tk.BOTH, expand=1)
        self.frame2rspace1=tk.Frame(self.frame2r,bg=self.c2)
        self.frame2rspace1.pack(fill=tk.BOTH, expand=1)
        self.frame2r2=tk.Frame(self.frame2r,bg=self.c3)
        self.frame2r2.pack(fill=tk.BOTH, expand=1)
        self.frame2rspace2=tk.Frame(self.frame2r,bg=self.c2)
        self.frame2rspace2.pack(fill=tk.BOTH, expand=1)
        self.frame2r2l=tk.Frame(self.frame2r2,bg=self.c1)
        self.frame2r2l.pack(fill=tk.BOTH, expand=1,side=tk.LEFT)
        self.frame2r2r=tk.Frame(self.frame2r2,bg=self.c3)
        self.frame2r2r.pack(fill=tk.BOTH, expand=1,side=tk.LEFT)
        self.frame2r3=tk.Frame(self.frame2r,bg=self.c4)
        self.frame2r3.pack(fill=tk.BOTH, expand=1)        
        
        self.header=tk.Label(self.frame1,justify=tk.LEFT,text="Proof Search Application (University of Berne)",bg=self.c1,fg='white',font=self._headerStyle)
        self.header.pack(expand=1, anchor=tk.W)
        
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#f00")
        ttk.Style().configure("TLabel", padding=6, relief="flat",background="#FFFFFF")
        text1 = 'Hello and welcome to the proof search application.\nThis programm can be used to check derivability of logical formulas'
        text1 += ' in classical logic, intuitionistic logic and modal logics K and S4.'
        text1 += '\nIf you want to see the resulting prooftree, please make sure, that record prooftree is on while checking derivability.'
        text1 += "\nIf you have a complex formula turning OFF 'record prooftree' may inprove performance." 
        text1 += "\nWhen the button 'export Tree' is clicked, a LaTeX-file will be generated and be stored in the directory 'proof'."

        self.head = tk.Label(self.frame1, justify=tk.LEFT, text=text1, bg=self.c1, fg='white',font=self._fontStyle)
        self.head.pack(anchor = tk.W, expand=1)

        self.label_logic = tk.Label(self.frame2l1, text='Select Logic:', bg=self.c2,font=self._fontStyle)#,font=self.fontStyle)
        self.label_logic.pack(anchor=tk.W,expand=1)
 
        self.rb1 = tk.Radiobutton(self.frame2l1, text='classical logic', variable=self.logic, value='cl',bg=self.c2,font=self._fontStyle)#,style = 'Wild.TRadiobutton')
        self.rb1.pack(anchor=tk.W,expand=1)
        self.rb2 = tk.Radiobutton(self.frame2l1, text='intuitionistic logic', variable=self.logic, value='il', bg=self.c2,font=self._fontStyle)
        self.rb2.pack(anchor=tk.W,expand=1)
        self.rb3 = tk.Radiobutton(self.frame2l1, text='modal logic K', variable=self.logic, value='scK', bg=self.c2,font=self._fontStyle)
        self.rb3.pack(anchor=tk.W, expand=1)
        self.rb4 = tk.Radiobutton(self.frame2l1, text='modal logic S4', variable=self.logic, value='s4', bg=self.c2,font=self._fontStyle)
        self.rb4.pack(anchor=tk.W,expand=1)

        self.lb_pt=tk.Label(self.frame2l2,text='Record ProofTree:',bg=self.c3,font=self._fontStyle)
        self.lb_pt.pack(anchor=tk.W, side=tk.LEFT, expand=1, padx=10)
        self.pTree_on_off = ttk.Button(self.frame2l2, text="ON", command=self.toggleOnOff)
        self.pTree_on_off.pack(anchor=tk.W, side=tk.LEFT,expand=1)
        
        self.lb_pt=tk.Label(self.frame2l3,text='Enter filename:',bg=self.c3,font=self._fontStyle)
        self.lb_pt.pack(anchor=tk.W, side = tk.LEFT, expand=1, padx=10)       
        self.enter_filename = tk.Entry(self.frame2l3,bg=self.c4,  width=20, bd=5)
        self.enter_filename.pack(anchor=tk.W, side=tk.LEFT,fill=tk.X, expand=1,padx=10)       
        self.exportTree = ttk.Button(self.frame2l4, text="exportTree", command=self.exportTree)
        self.exportTree.pack(anchor=tk.E,expand=1,padx=10)
        
        text2="Please enter a formula. \nThere are two options:"
        text2+="\n\n1. Enter a tuple like (2,'->',(0,'p'),(1,'-',(0,'p'))) for p->(-p) \nUse 'enter formula' to store"
        text2+="\n\n2. Enter the formula as string using\n'*' for AND, '+' for OR,'->' for implication\n"
        text2+="'-' for negation,'box' for box, 'dia' for diamond\nUse 'parse and enter formula' to store."
        self.explainEntry1 = tk.Label(self.frame2r1, justify=tk.LEFT, text=text2,bg=self.c2,font=self._fontStyle)
        self.explainEntry1.pack(anchor=tk.W, expand=1,pady=10)

        self.enter_formula = tk.Entry(self.frame2r1,bg=self.c4 ,width=50, bd=5)
        self.enter_formula.pack(fill=tk.X, expand=1,pady=10)

        self.button_enter = ttk.Button(self.frame2r2l, text = "enter formula",command = self.enter_form)        
        self.button_enter.pack(side=tk.LEFT,expand=1,padx=10,pady=10)
        self.button_enter = ttk.Button(self.frame2r2l, text = "parse and enter formula", style = "TButton",command = self.parse_form)        
        self.button_enter.pack(side=tk.LEFT,expand=1,padx=10,pady=10)        

        self.button_check = ttk.Button(self.frame2r2r,text = "chek derivability", command = self.test_formula)
        self.button_check.pack(side=tk.RIGHT, expand=1,padx=10,pady=10)
        
        self.label = tk.Label(self.frame2r3,justify=tk.LEFT,width=50,text='\n',bg=self.c4,font=self._fontStyle)
        self.label.pack(fill=tk.BOTH,expand=1)
    
    def test_formula(self):
        if self._lastForm != self.enter_formula.get():
            self.label['text']='You must first enter the formula'
            self.label['bg']=self.red
            self.frame2r3['bg']=self.red
        elif self.check_well_defined(self._formula):
            if self.logic.get() == 'cl':
                answer = cl.derivable(self._formula, self._recorded)
                if self._recorded:
                    self._prooftree = cl.prooftree
            elif self.logic.get() == 'il':
                answer = il.derivable(self._formula, self._recorded)
                if self._recorded:
                    self._prooftree = il.prooftree
            elif self.logic.get() == 'scK':
                answer = scK.derivable(self._formula, self._recorded)
                if self._recorded:
                    self._prooftree = scK.prooftree
            else:
                answer = s4.derivable(self._formula, self._recorded)
                if self._recorded:
                    self._prooftree = s4.prooftree
            if answer:
                self.label['text']=self.logic.get()+' derivable\n' 
                self.label['bg']=self.green
                self.frame2r3['bg']=self.green
                if self._recorded:
                    self._proof_recorded: True
            else:
                self.label['text']='not '+self.logic.get()+' derivable\n'
                self.label['bg']=self.red
                self.frame2r3['bg']=self.red
        else:
            self.label['text']='not well defined formula\n'

    def run(self):
        self.root.mainloop()
        
    def string2form(self,form, source):
        try:
            if source ==0:
                formula = ast.literal_eval(form)
            elif source ==1:
                formula = parsing.string2formula(form)
            self._formula = formula
            if self.check_well_defined(formula):
                self.label['text']='successfully entered formula:\n'+form
                self.label['bg']=self.green
                self.frame2r3['bg']=self.green
            elif self.logic.get() in ('cl','il') and scK.is_welldefined(formula):
                self.label['text']='formula not well defined for logic '+self.logic.get()+ '\nTry again or change logic!'
                self.label['bg']=self.c4
                self.frame2r3['bg']=self.c4
            else:
                self.label['text']='formula not well defined: '+form+'\nTry again!'
                self.label['bg']=self.red
                self.frame2r3['bg']=self.red
        except:
                self.label['text']='formula not well defined: '+form+'\nTry again!'
                self.label['bg']=self.red
                self.frame2r3['bg']=self.red
 
        
    def check_well_defined(self, formula):
        if self.logic.get() == 'cl':
            return cl.is_welldefined(formula)            
        elif self.logic.get() == 'il':
            return il.is_welldefined(formula)                 
        elif self.logic.get() == 'scK':
            return scK.is_welldefined(formula) 
        else:
            return s4.is_welldefined(formula)
            
        
    def enter_form(self):
        form = self.enter_formula.get()
        self._lastForm = form
        if form:
            self.string2form(form, 0)
            
    def parse_form(self):
        form = self.enter_formula.get()
        self._lastForm = form
        self.string2form(form,1)
            
    def toggleOnOff(self):
        if self.pTree_on_off.config('text')[-1] == 'ON':
            self.pTree_on_off.config(text='OFF')
            self._recorded=False
        else:
            self.pTree_on_off.config(text='ON')
            self._recorded=True
            self.label['text']=''
            self.label['bg']=self.c4
            self.frame2r3['bg']=self.c4
    
    def exportTree(self):
        if self._recorded:
            if self._prooftree:
                self._filename = self.enter_filename.get().split('.',1)[0]+'.tex'
                self._prooftree.to_file(self._filename)
                self.label['text']='\n'
                self.label['bg']=self.c4
                self.frame2r3['bg']=self.c4
                if self._filename not in self._openTrees:
                    self._openTrees.append(self._filename)
                    self.openTree = ttk.Button(self.frame2l4, text="open Tree in "+self._filename, command=self.openTree)
                    self.openTree.pack(side = tk.RIGHT,padx=10, pady=10)
            else:
                self.label['text']="No prooftree to export in a file so far\nFirst, derive a formula."
                self.label['bg']=self.red
                self.frame2r3['bg']=self.red
        else:
            self.label['text']="You must set 'Recorded ProofTree' ON \nduring derivability check to export tree\n afterwards."
            self.label['bg']=self.red
            self.frame2r3['bg']=self.red
    
    def openTree(self):
        os.chdir("./proof")
        try:
            os.system("pdftex "+self._filename)
            webbrowser.open_new(self._filename.get().split('.',1)[0]+'.pdf')
        except:
            self.label['text']="Can't convert file. Please do it manually.\nYou find the LaTeX-file in directory 'proof'"
            self.label['bg']=self.red
            self.frame2r3['bg']=self.red
        os.chdir("..")
        
#    def increase_label_font(self):
#        fontsize = self._fontStyle['size']
#        #self.head['text'] = fontsize+2
#        self._fontStyle.configure(size=fontsize+2)
#
#    def decrease_label_font(self):
#        fontsize = self.fontStyle['size']
#        #self.head['text'] = fontsize-2
#        self._fontStyle.configure(size=fontsize-2)

if __name__ == '__main__':
    app = Proof_GUI()
    app.run()
