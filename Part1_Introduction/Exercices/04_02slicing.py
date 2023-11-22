from random import shuffle

m = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
shuffle(m)
print(m)

"""
len(m) % 2 si 1 c'est vrai si 0 c'est faux
"""

createVec = lambda m : [ m[i:(i+2)] for i in range(0, len(m), 2) ]

# quand c'est impair le module 2 retourne 1 qui est dans le if équivalent à True
if len(m) % 2:
    vec = createVec(m)
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
result = [l[n:n+3] if(n+2==len(l)-1) else l[n:n+2] for n in range(0,len(l)-1,2)]