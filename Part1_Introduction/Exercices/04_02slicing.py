from random import shuffle

m = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
shuffle(m)
# print(m)

"""
len(m) % 2 si 1 c'est vrai si 0 c'est faux
"""

createVec = lambda m : [ m[i:(i+2)] for i in range(0, len(m), 2) ]

# quand c'est impair le module 2 retourne 1 qui est dans le if équivalent à True
if len(m) % 2:
    vec = createVec(m)
    # je prend le dernier élément qui un couple seul, il est retiré,
    # on récupére le dernier qui cette fois un couple de deux valeurs puis on ajoute l'élément seul à ce couple
    vec[-1] = vec.pop(-1) + vec[-1]
else:
    vec = createVec(m)

print(vec)

def vect(m):
    lenM = len(m)
    createVec = lambda m : [ m[i:(i+2)] for i in range(0, lenM, 2)  ]

    if lenM % 2 == 0:
        return createVec(m)

    vec = createVec(m) 
    vec[-1] = vec.pop(-1) + vec[-1]

    return vec 

# plus simple
result = [ m[n:n+3] if(n+2==len(m)-1) else m[n:n+2] for n in range(0,len(m)-1,2)]

print(result)

"""
Pour le dernier couple 

len(m) = 7
range(0,6,2)
0, 2, 4, 

Le dernier pas
4 + 2  =  6 == 7 - 1  True

len(m) = 6 
range(0,5,2)
0, 2, 4 
4 + 2 = 6 == 6 - 1 False
m[4:4+2]

"""
print("------")
m = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
# shuffle(m)

vector = lambda m : [  m[i:(i+2)] + ( [m[-1]] if i == (len(m) - 3) else [] ) for i in range(0,len(m) - 1, 2) ] 

m = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
p = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

print( vector(m) )
print( vector(p) )
