import pygame

def dessine_case():
    """Dessine les cases du plateau de jeu."""
    for i in range(10):  # Lignes
        for a in range(10):  # Colonnes
            x = i * largeur_x / 10
            y = a * longeur_y / 10
            couleur = blanc if (i + a) % 2 == 0 else noir
            pygame.draw.rect(screen, couleur, (x, y, largeur_x / 10, longeur_y / 10))


pygame.init()

# Dimensions et couleurs
largeur_x = 600
longeur_y = 600

case_size = (largeur_x / 10, longeur_y / 10)

blanc = (255, 255, 255)
noir = (0, 0, 0)


# Position initiale des pions
pion_pos_x = 0
pion_pos_y = 0

pion_noir_pos_x = 9
pion_noir_pos_y = 9

# Fenêtre et affichage
screen = pygame.display.set_mode((largeur_x, longeur_y))
pygame.display.set_caption("Jeux dames")
screen.fill(blanc)

# Chemins des images
path_to_pion_blanc = "../img/MA-24_pion.png"
path_to_pion_noir = "../img/MA-24_pion_noir.png"

# Chargement et mise à l'échelle des pions
pion_blanc = pygame.image.load(path_to_pion_blanc)
pion_blanc = pygame.transform.scale(pion_blanc, (largeur_x // 10, longeur_y // 10))

pion_noir = pygame.image.load(path_to_pion_noir)
pion_noir = pygame.transform.scale(pion_noir, (largeur_x // 10, longeur_y // 10))

# Mise à jour de l'écran avec le plateau et les pions
dessine_case()

# Placement des pions
screen.blit(pion_blanc, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))
screen.blit(pion_noir, (pion_noir_pos_x * case_size[0], pion_noir_pos_y * case_size[1]))
pygame.display.flip()
