import pygame
import sys

def dessine_case():
    for i in range(10):  # Boucle pour les lignes+
        for a in range(10):  # Boucle pour les colonnes
            x = i * largeur_x / 10
            y = a * longeur_y / 10
            couleur = blanc if (i + a) % 2 == 0 else noir
            pygame.draw.rect(screen, couleur, (x, y, largeur_x / 10, longeur_y / 10))

pygame.init()

# Position initiale des pions
pion_pos_x = 0
pion_pos_y = 0

pion_noir_pos_x = 9  # Coin opposé du plateau
pion_noir_pos_y = 9

largeur_x = 600
longeur_y = 600

case_size = (largeur_x / 10, longeur_y / 10)

blanc = (255, 255, 255)
noir = (0, 0, 0)

path_to_pion_blanc = "../img/MA-24_pion.png"
path_to_pion_noir = "../img/MA-24_pion_noir.png"

screen = pygame.display.set_mode((largeur_x, longeur_y))

pygame.display.set_caption("Jeux dames")
screen.fill(blanc)

dessine_case()

# Chargement des images des pions
pion_blanc = pygame.image.load(path_to_pion_blanc)
pion_blanc = pygame.transform.scale(pion_blanc, (largeur_x // 10, longeur_y // 10))
screen.blit(pion_blanc, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

pion_noir = pygame.image.load(path_to_pion_noir)
pion_noir = pygame.transform.scale(pion_noir, (largeur_x // 10, longeur_y // 10))
screen.blit(pion_noir, (pion_noir_pos_x * case_size[0], pion_noir_pos_y * case_size[1]))

pygame.display.flip()

# Ajout d'une temporisation minimale
temps_derniere_action = 0
delai = 100


pygame.quit()
sys.exit()