# TP

## Partie 1

Ce TP sera évaluer lors du prochain cours. Créez des équipes de 5 personnes.

Créez un fichier dans lequel vous écrirez votre nom/prénom et classe.

Soit la chaine de caractères suivantes m ci-après, calculez le nombre de i, puis le nombre de chaque lettre.

Faites une fonction pour répondre à cette question.

```python
m = "Mississippi"
```

1. Remplacez l'une des lettre qui apparait avec la grande plus fréquence par la lettre e dans le mot m. Remplacez également les autres lettres qui apparaissent avec la même fréquence max.

2. Calculez la fréquence d'apparition de chaque lettre dans le mot m.

3. Dans le texte suivant compter le nombre de fois que vous avez la prenom le, puis le nombre de e, et à l'aide d'un script effacez tous les e.


```txt
Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace
lui doive être plus haïssable encore.

Henri Michaux
```

4. A l'aide du code Python suivant enregistrez dans un fichier json les statistiques suivantes :
 - nombre pronon
 - nombre de e

Pensez à faire un script pour compter tous les pronons du texte.

Si le module json n'est déjà installé dans les modules Python tapez la ligne de commande suivante dans votre terminale

```bash
pip install json
```

Code pour enregistrer des données dans un fichier ( existant ou pas ).

```python
import json

# Ton objet JSON
data = {"cle": "valeur", "autre_cle": [1, 2, 3]}

# Chemin vers le fichier où tu veux enregistrer le JSON
path = "chemin/vers/ton/fichier.json"

# Enregistre le JSON dans le fichier
with open(path, 'w') as file:
    json.dump(data, file)
```
5. (facultatif ) Quel est le mot le plus utilisé dans le texte.
6. (facultatif ) Quel est le mot le plus utilisé dans le texte en dehors des pronons.

## Partie 2

Soit la liste suivante 

```python
elems = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'e']
```

Créez des couples de deux valeurs.

