# portée Global
a, d = 1, 9

def foo():

     # portée Englobante
    c = 3
    def bar():
        # print(c, d)

        return c, d
    # portée locale
    b = 2
    # a : portée globale
    return a, b, bar()

print( foo() )

# print( c  ) # ici la portée est dite englobante et pas global

"""
L'espace Builtins c'est le scope (portée) de Python qui est accesible dans tous les scripts de python 

"""

len = 100 # len est définie dans le scope builtins 
print(len)

print = 7
# print(print)