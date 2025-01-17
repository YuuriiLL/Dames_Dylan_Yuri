"""
Project Name : Jeu de dames
Date : 17.01.2025
Auteur : Dylan Pinto, Yuri Lima

# Sources
    ChatGPT
    Forums
    Code de base donnée par le professeur
    Connaisances de bases
"""


import pygame
import sys
from code_rules import selectionner_pion, bouger_pion
from code_gfx import actualise_affichage, case_size
from code_rules import start

# Variables globales pour suivre la sélection du pionss
pion_selectionne = None
couleur_selectionnee = None

if __name__ == "__main__":
    pygame.init()

    # Lancer la boucle principale du jeu
    start()

    # Quitter
    pygame.quit()
    sys.exit()
