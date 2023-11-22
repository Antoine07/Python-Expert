

def maxElem(a, b):
    if a > b :
        return a

    return b


print(maxElem(1, 2))
print(maxElem(1, maxElem(2, 3) ))
print(maxElem(10, maxElem( maxElem(200, 3), 5 ) ))

l = [10, 9, 100, 67, 89, 200, 87, 2]

from functools import reduce

print(  reduce(maxElem, l)  )

print(max(l))
print(max(1, 2, 3))