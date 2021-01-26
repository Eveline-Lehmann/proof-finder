
def string2formula(string):
    liste = handle_modalsImp(list(string.replace(" ","")))
    liste = replace_atoms(liste)
    liste2 = liste[:]
    while len(liste)>3:
        indices = get_indices_brackets(liste)
        for key in indices:
            if indices[key]-key==4 and liste[key+2] in ('+','*','->'):
                liste[key]=(2,liste[key+2],liste[key+1],liste[key+3])
                for i in range(1,5):
                    liste[key+i]=[]
            if indices[key]-key==3 and liste[key+1] in ('-','box','dia'):
                liste[key]=(1,liste[key+1],liste[key+2])
                for i in range(1,4):
                    liste[key+i]=[]
            if indices[key]-key==2 and isinstance(liste[key+1],tuple):
                liste[key]=liste[key+1]
                for i in range(1,3):
                    liste[key+i]=[]                
        i = 0
        while i<len(liste)-1:
            if liste[i] in ('-', 'box','dia') and isinstance(liste[i+1],tuple):
                liste[i] = (1,liste[i],liste[i+1])
                liste[i+1]=[]
                i += 2
                continue
            if liste[i]=='':
                liste[i]=[]
            i+=1
        liste = [a for a in liste if a!= []]
        if liste == liste2 and len(liste)>3:
            return liste
        liste2 = liste[:]
    
    if len(liste) == 3:
        return (2,liste[1], liste[0], liste[2])
    elif len(liste) == 2:
        return (1, liste[0], liste[1])
    else:
        return liste[0]

def handle_modalsImp(liste):
    list2 = list()
    i = 0
    while i<len(liste):
        if liste[i] in ('b','d','-'):
            if i<len(liste)-2 and liste[i]+liste[i+1]+liste[i+2] in ('box','dia'):
                list2.append(liste[i]+liste[i+1]+liste[i+2])
                i+=3
                continue
            elif i<len(liste)-1 and liste[i]+liste[i+1]=='->':
                list2.append('->')
                i+=2
                continue
        list2.append(liste[i])
        i+=1
    return list2

def replace_atoms(liste):
    i = 0
    while i < len(liste):
        if liste[i] not in ('(',')','-','>','+','*','box','dia',' ','->'):
            atom = liste[i]
            j = 1
            while i+j<len(liste) and liste[i+j]not in ('(',')','-','>','+','*','box','dia',' ','->'):
                atom += liste[i+j]
                liste[i+j] = []
                j+=1
            liste[i]=(0,atom)
            i += j
            continue
        i+=1
    return [a for a in liste if a!=[]]

def get_indices_brackets(liste):
    indices = {}
    stack = []
    
    for i, c in enumerate(liste):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack)==0:
                raise IndexError("No matching closing parens at: " + str(i))
            else:
                indices[stack.pop()] = i
    if len(stack) > 0:
        raise IndexError("No matching opening parens at: " + str(stack.pop()))
    
    return indices


        
