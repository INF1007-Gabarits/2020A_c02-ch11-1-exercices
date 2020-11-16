[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Combat de personnages dans un jeu (chapitre 10.2)

<!-- Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md) -->

Nous allons programmer une classe de personnage très simple qui permet d'effectuer des combats tour-à-tour dans un jeu.

## Armes des personnages
### `characters.Weapon`

On veut une classe qui représente une arme. Une arme possède un nom, un niveau d'attaque et un niveau minimal pour l'utiliser.

Le nom ne peut pas être changé.

On veut une méthode de classe `make_unarmed` qui construit un `Weapon` nommé `"Unarmed"` avec une puissance de 20.

## Personnages du jeu
### `characters.Character`

Dans notre jeu, un personnage est composé des propriétés suivantes :

`Character.name` : Le nom du personnage <br>
`Character.max_hp` : HP maximum <br>
`Character.attack` : Le niveau d'attaque du personnage <br>
`Character.defense` : Le niveau de défense du personnage <br>
`Character.level` : Le niveau d'expérience du personnage <br>
`Character.weapon` : L'arme utilisée par le personnage <br>
`Character.hp` : Les HP restants <br>

On a une méthode `compute_damage` qui calcule les dégâts infligés à un autre personnage (en paramètre). La formule est la suivante : 

<img src="doc/assets/dmg_eq.png" width="600">

Où *a* est l'attaquant et *d* est le défendeur. <br>
*crit* est 2 envrion 1/16 (6.25%) du temps, 1 sinon <br>
*random* est un nombre aléatoire entre 85% et 100%

## Déroulement d'un combat
### `deal_damage` et `run_combat`_

