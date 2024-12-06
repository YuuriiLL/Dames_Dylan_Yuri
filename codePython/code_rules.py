import pygame
import sys

from code_gfx import dessine_case, screen, pion_blanc, pion_noir,case_size, pion_noir_pos_x, pion_noir_pos_y

# Logique des mouvements
def bouge_bas_droite():
    """Déplace le pion blanc en bas à droite si possible."""
    global pion_pos_x, pion_pos_y
    if pion_pos_x < 9 and pion_pos_y < 9:
        pion_pos_x += 1
        pion_pos_y += 1
        actualise_affichage()

def bouge_bas_gauche():
    """Déplace le pion blanc en bas à gauche si possible."""
    global pion_pos_x, pion_pos_y
    if pion_pos_x > 0 and pion_pos_y < 9:
        pion_pos_x -= 1
        pion_pos_y += 1
        actualise_affichage()

def actualise_affichage():
    """Met à jour l'affichage après un mouvement."""
    dessine_case()
    screen.blit(pion_blanc, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))
    screen.blit(pion_noir, (pion_noir_pos_x * case_size[0], pion_noir_pos_y * case_size[1]))
    pygame.display.update()

# Gestion des événements et boucle principale
temps_derniere_action = 0
delai = 100

def start():
    running = True
    while running:
        temps_actuel = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif temps_actuel - temps_derniere_action > delai:
                if keys[pygame.K_RIGHT]:
                    bouge_bas_droite()
                    temps_derniere_action = temps_actuel
                elif keys[pygame.K_LEFT]:
                    bouge_bas_gauche()
                    temps_derniere_action = temps_actuel

pygame.quit()
sys.exit()
