import site

#set of domains to be checked, lists of 1-6, specific values can be entered to try and solve the problem with a given starting board, each domain represents a single row of the board.

x1 = [1, [2]]
#x1 = [1, [1]]
#x2 = [2, [3]]
x2 = [2, [4]]
#x2 = [2, [1,2,3,4,5,6]]
x3 = [3, [6]]
#x3 = [3, [1,2,3,4,5,6]]
x4 = [4, [1,2,3,4,5,6]]
x5 = [5, [1,2,3,4,5,6]]
x6 = [6, [1,2,3,4,5,6]]
conslist =[]
Varlist = [x1,x2,x3,x4,x5,x6]

def constraintcheck(v1,v2, i,j):

    # pulls the correct set of booleans for the row and column being checked
    v1 = v1-1
    v2 = v2-1
    wholelist =  [[(False), (i != j and i!= j+1 and i != j-1), (i != j and i != j+2 and i != j-2), (i != j and i!= j+3 and i != j-3), (i != j and i!= j +4 and i != j-4), (i != j and i!= j+5 and i != j-5)],
                  [(i != j and i != j-1 and i!= j+1), (False), (i != j and i != j+1 and i != j-1), (i != j and i!= j+2 and i != j-2), (i != j and i!= j +3 and i != j-3), (i != j and i!= j+4 and i != j-4)],
                  [(i != j and i != j-2 and i!= j+2), (i != j and i != j+1 and i != j-1), (False), (i != j and i!= j+1 and i != j-1), (i != j and i!= j +2 and i != j-2), (i != j and i!= j+3 and i != j-3)],
                  [(i != j and i != j-3 and i!= j+3), (i != j and i != j+2 and i != j-2), (i != j and i!= j+1 and i != j-1), (False), (i != j and i!= j +1 and i != j-1), (i != j and i!= j+2 and i != j-2)],
                  [(i != j and i != j-4 and i!= j+4), (i != j and i != j+3 and i != j-3), (i != j and i!= j+2 and i != j-2), (i != j and i!= j +1 and i != j-1), (False), (i != j and i!= j+1 and i != j-1)],
                  [(i != j and i != j-5 and i!= j+5), (i != j and i != j+4 and i != j-4), (i != j and i!= j+3 and i != j-3), (i != j and i!= j +2 and i != j-2), (i != j and i!= j+1 and i != j-1), (False)]
                  ]
    conslist = wholelist[v1]
    conslistretr = conslist[v2]
    
    return conslistretr


    # revises a single arc 
def Revise(i,j):
    var1 = i[0]
    var2 = j[0]
    changed = False
    print('Revising Arc x' + str(var1) + ' , x' + str(var2))
    delelist = []
    for w in i[1]:
        supported = False
        for l in j[1]:
            consanswer = constraintcheck(var1, var2, l, w)
            if consanswer == True:
                supported = True
                #sets arc for deletion if evaluation is false, not supported,
        if supported == False:
            delelist.append(w)
            print("value " + str(w) + " removed from var " + "x" + str(i[0]))
            changed = True
            #deletes arc if it has been evaluated as not supported
    for d in delelist:
            for t in i[1]:
                if t == d:
                    i[1].remove(d)
                    if len(i[1]) == 0:
                        print('Domain ' + str(i[0]) + ' is empty')
                        return('empty')
    return changed

#print(setlist)
#print(testlist)
#ac1 algorithm repeats until no changes are made in a whole pass of revisions for each arc. takes each arc in turn and removes any unsupported values from the domain.
def AC1(x):
    repeat = True
    while repeat == True:
        repeat = False
        for i in x:
            for j in x:
                if i != j:
                    ans = Revise(i,j)
                    if ans == 'empty':
                        return
                    if ans == True:
                        repeat = True

AC1(Varlist)
                    

for i in Varlist:
    print('x' + str(i[0]) + ' = ' + str(i[1]) )

        
    

    


