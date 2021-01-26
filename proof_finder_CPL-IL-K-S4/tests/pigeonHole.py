from random import randint

def generate_ph(n,valid):
    if n < 2:
        return [False]
    if n ==2:
        if valid:
            return (2,'->',(2,'*',(0,'p0inp0'),(0,'p1inp1')),(2,'*',(0,'p0inp0'),(0,'p1inp1')))
        else:
            return (2,'->',(2,'*',(0,'p0inp0'),(0,'p1inp1')),(2, '*',(0,'F'),(1,'-',(0,'F'))))
    else:
        holes = generateMatrix(n)
        ante = generateAntecedent(n, holes)
        cons = generateConsequent(n, holes, valid)    
        return (2,'->',ante,cons)

def generateMatrix(n):
    holes = list()
    for h in range(0,n-1):
        pigeons = list()
        for p in range(0,n):
            atom = (0, 'p'+str(p)+'in'+str(h))
            pigeons.append(atom)
        holes.append(pigeons)
    return holes

def generateAntecedent(n, holes):
    antes = list()
    for p in range(n):
        ors = holes[0][p]
        for h in range(1, n-1):
            ors = (2,'+',ors,holes[h][p])
        antes.append(ors)
    ante = (2,'*',antes[0],antes[1])
    for p in range(2,n):
        ante = (2,'*',ante,antes[p])
    return ante

def generateConsequent(n, holes, valid):       
    conses = list()
    for h in range(n-1):
        index = 0
        while index < n-1:
            for p in range(index+1, n):
                ands = (2,'*',holes[h][index],holes[h][p])
                conses.append(ands)
            index+=1
    if not valid:
        rand = randint(0,len(conses)-1)
        del conses[rand]
    cons = (2,'+',conses[0],conses[1])
    for form in range(2,len(conses)):         
        cons = (2,'+',cons,conses[form])
    return cons
