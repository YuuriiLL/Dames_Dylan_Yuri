import pygame
from code_gfx import screen, case_size, actualise_affichage, pions_positions

# Variables globales
pion_selectionne = None
couleur_selectionnee = None

def selectionner_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee

    for couleur, positions in pions_positions.items():
        if (case_x, case_y) in positions:
            pion_selectionne = (case_x, case_y)
            couleur_selectionnee = couleur
            print(f"Pion {couleur} sélectionné à {case_x}, {case_y}")

def bouger_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, pions_positions

    if pion_selectionne and couleur_selectionnee:
        x, y = pion_selectionne

        if 0 <= case_x < 10 and 0 <= case_y < 10:
            toutes_positions = [pos for positions in pions_positions.values() for pos in positions]

            if (case_x, case_y) not in toutes_positions:
                pions_positions[couleur_selectionnee].remove((x, y))
                pions_positions[couleur_selectionnee].append((case_x, case_y))

                pion_selectionne = (case_x, case_y)

                print(f"Pion {couleur_selectionnee} déplacé à {(case_x, case_y)}")
                actualise_affichage()


def start():
    global pion_selectionne, couleur_selectionnee

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                case_x = int(mouse_x // case_size[0])
                case_y = int(mouse_y // case_size[1])

                # Sélectionner le pion lorsqu'on clique sur une case
                selectionner_pion(case_x, case_y)

            elif event.type == pygame.KEYDOWN:
                if pion_selectionne and couleur_selectionnee:
                    case_x, case_y = pion_selectionne

                    if event.key == pygame.K_LEFT:
                        bouger_pion(case_x - 1, case_y +1)

                    elif event.key == pygame.K_RIGHT:
                        bouger_pion(case_x + 1, case_y + 1)

                    elif event.key == pygame.K_UP:
                        bouger_pion(case_x + 1, case_y - 1)

                    elif event.key == pygame.K_DOWN:
                        bouger_pion(case_x - 1, case_y - 1)

        actualise_affichage()