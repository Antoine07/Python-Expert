TVA = .2
PRECISION = 2

def ttc(price, tva = TVA):

    return round( (1+tva)*price, PRECISION )

print(ttc(100))
print(ttc(tva = .3, price = 100))