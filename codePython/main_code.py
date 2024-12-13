"""---------------MAIN CODE---------------"""

import pygame
import sys

from code_rules import bouge_bas_droite, bouge_bas_gauche, actualise_affichage, start
from code_gfx import dessine_case, initialiser_gfx

pygame.init()

initialiser_gfx()

start()

pygame.quit()
sys.exit()