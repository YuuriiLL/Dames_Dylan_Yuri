"""---------------MAIN CODE---------------"""

import pygame
import sys

from code_gfx import initialiser_gfx
from code_rules import start

pygame.init()

def main():
    """Point d'entrée du programme."""
    pygame.init()

    # Initialisation de l'interface
    initialiser_gfx()

    # Démarrage du jeu
    start()

    pygame.quit()
    sys.exit()

pygame.quit()
sys.quit()
