# OpenClassrooms Project: McGyver

## Informations
    @description    This Document will contain all the scope and analysis
                    of the OpenClassrooms "McGyver" Project.
    @author         Anthony Gomes <anthony.gomes@afnor.org>
    @version        0.1
    @date           2018-12-22
    @notes          cd D:/[OC]Formation_Python/Projet_3/[Projet]McGyver
    @note           0.1 (2018-12-22) : Document initialisation after
                    first read of the statement of the project


## scope

Suite à la première version du jeu remplissant le CDC, je ne suis pas content de la structure actuelle du code qui bien que fonctionnant n'a pas vraiment de logique, ce qui a été confirmé par les retours de Sébastien Declercq, collègue développeur suivant également la formation OC, et d'Olivier mon mentor :
- Classes à multiples rôles
- Fond et formes mélangés
- Beaucoup de code pouvant être simplifié
- Multiplication inutile de boucles
- Code non PEP8

**Voici la nouvelle structure du code suite à réflexion:**
## Class Game
Nouvelle classe principale du code, servira à piloter de manière générale le jeu:
- Gestion du Jeu (Boucles Home, Jeu, Fin de Jeu)
- Gestion des inputs et condition de victoire
## Class Map_level
- Parsing input Labyrinth
- Generation du level
  - Structure labyrinth (wall, Zones de déplacement, ajout des zones de déplacement libres dans une liste afin de gérer le positionnement aléatoire des items
    liste afin )
  - Calcul Position mcgyver
  - Calcul position des items
  - Calcul position Guard
## Class Character
- Position actuelle du personnage
- Gestion des items du personnage
## Class Display
- Affichage Home
- Affichage Game level (Character.items en attribut pour gérer l'affichage des items)
- Affichage End
  - Si Win = true, affichage écran Win
  - Si Win = false, affichage écran Lose
## Class Constants
- Liste des items en json
- Liens vers les images
- Taille sprite

**Fonctionnement attendu du programme**
1. Lancement du jeu, affichage du menu (via Display.Home) variage game = 0
2. Lancement de la partie, passage game = 1, entrée boucle Game:
  - Map_level
  - Init Character
  - Display.Game
  - Detection INPUT:
    - Calcul position Character
    - Gestion mouvement
      - Si Object, maj class Map_level et Character
      - Si Guard, condition de victoire (Character.item == 3), Game = 0, Win = true
      - Sinon, rien, c'est un mur
    - Si Win = 1, Display.End
    - Sinon, Display.Game pour mise à jour de l'affichage avec la nouvelle structure

Les variables sont encore sujettes à modifications, à voir lors de l'écriture si c'est gérable

De cette façon on a un programme plus cohérent, chaque classe à sa fonction, et on devrait
éviter les duplications de codes pour tester les différentes positions d'items ou d'items
possédés par le personnage comme dans la version actuelle

A valider toutefois avant de lancer la refactorisation du code (qui sera effectué sur une
  branche refactoring afin de garder la version actuelle clean le temps de valider la nouvelle)