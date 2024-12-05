import pygame
import sys

def bouge_bas_droite():
    global screen, pion, pion_pos_x, pion_pos_y, case_size
    if pion_pos_x < 9 and pion_pos_y < 9:
        pion_pos_x += 1
        pion_pos_y += 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def bouge_bas_gauche():
    global screen, pion, pion_pos_x, pion_pos_y, case_size
    if pion_pos_x > 0 and pion_pos_y < 9:
        pion_pos_x -= 1
        pion_pos_y += 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def bouge_haut_droite():
    global screen, pion, pion_pos_x, pion_pos_y, case_size
    if pion_pos_x < 9 and pion_pos_y > 0:
        pion_pos_x += 1
        pion_pos_y -= 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def bouge_haut_gauche():
    global screen, pion, pion_pos_x, pion_pos_y, case_size
    if pion_pos_x > 0 and pion_pos_y > 0:
        pion_pos_x -= 1
        pion_pos_y -= 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def dessine_case():
    for i in range(10):  # Boucle pour les lignes
        for a in range(10):  # Boucle pour les colonnes
            x = i * largeur_x / 10  # Position x de la case
            y = a * longeur_y / 10  # Position y de la case
            couleur = blanc if (i + a) % 2 == 0 else noir  # Alternance des couleurs
            pygame.draw.rect(screen, couleur, (x, y, largeur_x / 10, longeur_y / 10))  # Dessin de la case

pygame.init()

pion_pos_x = 0
pion_pos_y = 0

largeur_x = 600
longeur_y = 600

case_size = (largeur_x / 10, longeur_y / 10)

blanc = (255, 255, 255)
noir = (0, 0, 0)

path_to_images = "img\\MA-24_pion.png"

screen = pygame.display.set_mode((largeur_x, longeur_y))

pygame.display.set_caption("Déplacement diagonal")
screen.fill((blanc))

dessine_case()

pion = pygame.image.load(path_to_images)
pion = pygame.transform.scale(pion, (largeur_x / 10, longeur_y / 10))
screen.blit(pion, (0, 0))

pygame.display.flip()

running = True
while running:
    keys = pygame.key.get_pressed()  # Récupérer les touches pressées
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            bouge_bas_droite()
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            bouge_bas_gauche()
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            bouge_haut_droite()
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            bouge_haut_gauche()

    pygame.display.update()

pygame.quit()
sys.exit()
