
m = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# start:end:step pour les indices
print(m[0:5])

# possible mais que des entiers
print(m[0: len(m) // 2])

# un nombre sur 3 jusqu'au bout de la liste

# sans rien renseigner sur le start et le end il part du début et s'arrete à la fin 
print(m[::3])

# Inverser la lise avec du slicing 
print(m[::-1])

# Inverser la lise avec du slicing 
print(m[::-2])


## 

from random import shuffle

m = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
shuffle(m)
print(m)