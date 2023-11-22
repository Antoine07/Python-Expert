

def mult(t):
    l = [] # une liste vide 
    for i in range(1, 11):
        l.append( t * i )  # push les éléments dans la liste
    
    return l

print(mult(5))

print( [ [t * i for i in range(1, 11)] for t in range(1, 10) ] )

# compréhension de liste
print( [5 * i for i in range(1, 11)] )

