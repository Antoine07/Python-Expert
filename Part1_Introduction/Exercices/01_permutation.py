a = 1
b = 3

t = a 
a = b 
b = t

print(f"a :{a} b : {b}")

a = 1
b = 3

# assignation en utilisant des tuples
a, b = b, a
print(f"a :{a} b : {b}")

a = 1
b = 2
c = 3

t = a 
a = b 
b = c
c = t
print(f"a :{a} b : {b} c {c}")

a, b, c = 1, 2, 3
a, b, c = b, c, a
print(f"a :{a} b : {b} c {c}")
