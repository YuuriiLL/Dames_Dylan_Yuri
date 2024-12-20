import pygame
import sys
from code_rules import selectionner_pion, bouger_pion
from code_gfx import actualise_affichage, case_size
from code_rules import start

# Variables globales pour suivre la sélection du pionfggfgdg
pion_selectionne = None
couleur_selectionnee = None

if __name__ == "__main__":
    pygame.init()

    # Lancer la boucle principale du jeu
    start()

    # Quitter proprement après l'exécution du programme
    pygame.quit()
    sys.exit()
