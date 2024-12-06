"""---------------MAIN CODE---------------"""

import pygame
import sys

from code_rules import actualise_affichage
from code_gfx import dessine_case
from code_rules import start

pygame.init()

dessine_case()
start()
actualise_affichage()
pygame.display.flip()

pygame.quit()
sys.quit()
