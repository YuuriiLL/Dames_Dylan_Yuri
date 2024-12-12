"""---------------MAIN CODE---------------"""

import pygame
import sys

from code_rules import bouge_bas_droite, bouge_bas_gauche
from code_rules import actualise_affichage
from code_gfx import dessine_case
from code_rules import start

pygame.init()

start()

dessine_case()

actualise_affichage()

pygame.display.flip()

pygame.quit()
sys.quit()
