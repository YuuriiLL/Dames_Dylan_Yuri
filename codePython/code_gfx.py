import pygame

# Dimensions du plateau et des cases
largeur_x = 600
longueur_y = 600
case_size = (largeur_x / 10, longueur_y / 10)

# Couleurs
blanc = (255, 255, 255)
noir = (255, 209, 220)

# Images des pions
path_to_pion_blanc = "../img/MA-24_pion.png"
path_to_pion_noir = "../img/MA-24_pion_noir.png"

pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((largeur_x, longueur_y))
pygame.display.set_caption("Jeu de dames")

# Chargement des images des pions
pion_blanc = pygame.image.load(path_to_pion_blanc)
pion_blanc = pygame.transform.scale(pion_blanc, (int(case_size[0]), int(case_size[1])))
pion_noir = pygame.image.load(path_to_pion_noir)
pion_noir = pygame.transform.scale(pion_noir, (int(case_size[0]), int(case_size[1])))

# Positions initiales des pions
pions_positions = {
    "blanc": [(j, i) for i in range(4) for j in range(10) if (i + j) % 2 != 0],
    "noir": [(j, i) for i in range(6, 10) for j in range(10) if (i + j) % 2 != 0],
}

def dessine_case(cases_possibles=[]):
    for ligne in range(10):
        for colonne in range(10):
            x = colonne * case_size[0]
            y = ligne * case_size[1]
            couleur = blanc if (ligne + colonne) % 2 == 0 else noir
            pygame.draw.rect(screen, couleur, (x, y, case_size[0], case_size[1]))

            # Si la case fait partie des cases possibles, colorier en vert
            if (colonne, ligne) in cases_possibles:
                pygame.draw.rect(screen, (0, 255, 0), (x, y, case_size[0], case_size[1]), 3)




def placer_pions():
    for couleur, positions in pions_positions.items():
        pion = pion_blanc if couleur == "blanc" else pion_noir
        for x, y in positions:
            screen.blit(pion, (x * case_size[0], y * case_size[1]))

def actualise_affichage(cases_possibles_affichees):
    screen.fill(blanc)
    dessine_case(cases_possibles_affichees)  # Afficher les cases possibles en vert
    placer_pions()
    pygame.display.update()


