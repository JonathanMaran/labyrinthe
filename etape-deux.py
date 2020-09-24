"""Etape 2"""


def printLabyrinthe():
    print('\n'.join(['|'.join(['{:5}'.format(item) for item in row]) for row in labyrinthe])+"\n")


def deplacementsPossibles(i, j, nombreDeplacementsPossibles):
    if i < len(labyrinthe) - 1 and (labyrinthe[i + 1][j] == 1 or labyrinthe[i + 1][j] == 'G'):
        nombreDeplacementsPossibles += 1
    if j < len(labyrinthe[i]) - 1 and (labyrinthe[i][j + 1] == 1 or labyrinthe[i][j + 1] == 'G'):
        nombreDeplacementsPossibles += 1
    if i > 0 and (labyrinthe[i - 1][j] == 1 or labyrinthe[i - 1][j] == 'G'):
        nombreDeplacementsPossibles += 1
    if j > 0 and (labyrinthe[i][j - 1] == 1 or labyrinthe[i][j - 1] == 'G'):
        nombreDeplacementsPossibles += 1

    return nombreDeplacementsPossibles


def sauvegardePosition(marqueurCroisement):
    return marqueurCroisement.append([i, j])


def deplacement(i, j):
    if i < len(labyrinthe) - 1 and (labyrinthe[i + 1][j] == 1 or labyrinthe[i + 1][j] == 'G'):
        #labyrinthe[i][j] = 0
        i += 1
        print(f"Déplacement d'une case vers le bas")
    elif j < len(labyrinthe[i]) - 1 and (labyrinthe[i][j + 1] == 1 or labyrinthe[i][j + 1] == 'G'):
        #labyrinthe[i][j] = 0
        j += 1
        print("Déplacement d'une case vers la droite")
    elif i > 0 and (labyrinthe[i - 1][j] == 1 or labyrinthe[i - 1][j] == 'G'):
        #labyrinthe[i][j] = 0
        i -= 1
        print("Déplacement d'une case vers le haut")
    elif j > 0 and (labyrinthe[i][j - 1] == 1 or labyrinthe[i][j - 1] == 'G'):
        #labyrinthe[i][j] = 0
        j -= 1
        print("Déplacement d'une case vers la gauche")
    else:
        i = marqueurCroisement[len(marqueurCroisement) - 1][0]
        j = marqueurCroisement[len(marqueurCroisement) - 1][1]
        #print("LA : " + str(len(marqueurCroisement) - 1))
        if len(marqueurCroisement) != 0:
            marqueurCroisement.pop()
            print("Retour à la dernière position enregistrée pour tester une nouvelle direction")
    return i, j


labyrinthe = [
    ['S', 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 'G', 1, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
]
i = 0
j = 0

marqueurCroisement = []

while labyrinthe[i][j] != 'G':
    labyrinthe[i][j] = 'x'
    nombreDeplacementsPossibles = 0
    nombreDeplacementsPossibles = deplacementsPossibles(i, j, nombreDeplacementsPossibles)
    if nombreDeplacementsPossibles > 1:
        sauvegardePosition(marqueurCroisement)

    #print(marqueurCroisement)
    printLabyrinthe()
    i, j = deplacement(i, j)

    print("Coordonnées: " + "("+str(i)+","+ str(j)+")")



print(f"\nCoordonnées finales: {i,j}")

if labyrinthe[i][j] == 'G':
    print("\nCHAMMPPIONNNN DU MONNNNDDEEEE !!")
else:
    print("\nPERDU FILSTON !!")

print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in labyrinthe]))
"""
t = Texttable()
t.add_rows([['Labyrinthe', 'j', 'j','j', 'j', 'j','j','j'], ['i','S', 0, 1,1,1,1,1]])
t.add_rows([['Labyrinthe', 'j', 'j','j', 'j', 'j','j','j'], ['i',1, 0, 1,0,0,1,0]])
t.add_rows([['Labyrinthe', 'j', 'j','j', 'j', 'j','j','j'], ['i',1, 0, 1,0,'G',1,1]])
t.add_rows([['Labyrinthe', 'j', 'j','j', 'j', 'j','j','j'], ['i',1, 1, 1,1,0,0,1]])
t.add_rows([['Labyrinthe', 'j', 'j','j', 'j', 'j','j','j'], ['i',1, 0, 1,0,1,1,1]])
t.add_rows([['Labyrinthe', 'j', 'j','j', 'j', 'j','j','j'], ['i',1, 0, 1,1,1,0,1]])


"""