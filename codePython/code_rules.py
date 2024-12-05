import pygame
import sys

def bouge_bas_droite():
    global pion_pos_x, pion_pos_y
    if pion_pos_x < 9 and pion_pos_y < 9:
        pion_pos_x += 1
        pion_pos_y += 1
        dessine_case()
        screen.blit(pion_blanc, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))
        screen.blit(pion_noir, (pion_noir_pos_x * case_size[0], pion_noir_pos_y * case_size[1]))

def bouge_bas_gauche():
    global pion_pos_x, pion_pos_y
    if pion_pos_x > 0 and pion_pos_y < 9:
        pion_pos_x -= 1
        pion_pos_y += 1
        dessine_case()
        screen.blit(pion_blanc, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))
        screen.blit(pion_noir, (pion_noir_pos_x * case_size[0], pion_noir_pos_y * case_size[1]))

# Position initiale des pions
pion_pos_x = 0
pion_pos_y = 0

pion_noir_pos_x = 9  # Coin opposé du plateau
pion_noir_pos_y = 9

pygame.quit()
sys.exit()