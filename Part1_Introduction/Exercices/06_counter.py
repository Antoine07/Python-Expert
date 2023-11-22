m = "Mississippi"

# première correction
s = {}
# une chaine de caractères se parcours comme une liste 
for e in m:
    # est ce que e le caractère est dans s le dictionnaire 
    # est e qui est un caractère est une clé du dictionnaire
    # "i" in {"i" : 1} True  "a" in {"i" : 1} False
    if e in s :
        s[e] += 1
    else :
        s[e] = 1

print(s)

      
    