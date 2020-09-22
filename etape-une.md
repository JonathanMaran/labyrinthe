
# Etape 1:

## De quoi avez-vous besoin à chaque étape pour vous arreter ?

Je m'arrete immédiatement après m'etre déplacé d'une case.

## Pour continuer ?

Je vérifie si j'ai la possibilité d'aller en bas, à droite, en haut et à gauche.
Si j'ai la possibilité d'aller à plus d'un endroit, je place un repère (dans un tableau) sur la case où je me trouve, 
sinon je me déplace dans la seule direction possible.

Dans le cas où j'ai plusieurs possibilités, je me déplace en fonction de l'algorithme Depth first search (soit en bas,
soit à droite, soit en haut, soit à gauche).

Une fois le déplacement effectué, je réitère l'opération.

## Pseudocode:
```python
(L)labyrinthe=[creation-du-labyrinthe]
position = labyrinthe[i][j]
marqueurCroisement[] 

while position != 'G':
    nombreDeplacementsPossibles = 0
    deplacementsPossibles()
    if nombreDeplacementsPossibles > 1:
        sauvegardePosition()

    deplacement()



fonction deplacementsPossibles():
    if L[caseBas] = 1:
        nombreDeplacementsPossibles += 1
    if L[caseDroite] = 1:
        nombreDeplacementsPossibles += 1
    if L[caseHaut] = 1:
        nombreDeplacementsPossibles += 1
    if L[caseGauche] = 1:
        nombreDeplacementsPossibles +=1 
    
    return nombreDeplacementsPossibles

fonction sauvegardePosition():
    marqueurCroisement = push position 

fonction deplacement():
    if L[caseBas] = 1:
        L[position] = 0
        position = caseBas
    
    elif L[caseDroite] = 1:
        L[position] = 0
        position = caseDroite
    
    elif L[caseHaut] = 1:
        L[position] = 0
        position = caseHaut

    elif L[caseGauche] = 1:
        L[position] = 0
    
    else: 
        position = marqueurCroisement[len(marqueurCroisement)-1]
        remove marqueurCroisement[len(marqueurCroisement)-1]

    return position

```
