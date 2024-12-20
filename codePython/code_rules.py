import pygame
from code_gfx import screen, case_size, actualise_affichage, pions_positions

# Variables globales
pion_selectionne = None
couleur_selectionnee = None
couleur_contour = (255, 0, 0)  # Couleur du contour, rouge ici

def selectionner_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee

    # Chercher si un pion existe dans la case sélectionnée
    for couleur, positions in pions_positions.items():
        if (case_x, case_y) in positions:
            pion_selectionne = (case_x, case_y)
            couleur_selectionnee = couleur
            print(f"Pion {couleur} sélectionné à {case_x}, {case_y}")
            return  # Sortie une fois que le pion est trouvé et sélectionné

def bouger_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, pions_positions

    if pion_selectionne and couleur_selectionnee:
        x, y = pion_selectionne

        # Vérification si la case est dans les limites
        if 0 <= case_x < 10 and 0 <= case_y < 10:
            toutes_positions = [pos for positions in pions_positions.values() for pos in positions]

            # Vérification si la case n'est pas déjà occupée
            if (case_x, case_y) not in toutes_positions:
                pions_positions[couleur_selectionnee].remove((x, y))
                pions_positions[couleur_selectionnee].append((case_x, case_y))

                pion_selectionne = (case_x, case_y)

                print(f"Pion {couleur_selectionnee} déplacé à {(case_x, case_y)}")
                actualise_affichage()

def dessiner_contour_pion(case_x, case_y):
    """Dessiner un contour autour de la case contenant le pion sélectionné"""
    if case_x is not None and case_y is not None:
        x, y = case_x * case_size[0], case_y * case_size[1]
        pygame.draw.rect(screen, couleur_contour, (x, y, case_size[0], case_size[1]), 3)  # 3 est l'épaisseur du contour

def start():
    global pion_selectionne, couleur_selectionnee

    running = True

    while running:
        # Gestion des événements
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

                    # Déplacer le pion en fonction des touches directionnelles
                    if event.key == pygame.K_LEFT:
                        bouger_pion(case_x - 1, case_y + 1)

                    elif event.key == pygame.K_RIGHT:
                        bouger_pion(case_x + 1, case_y + 1)

                    elif event.key == pygame.K_UP:
                        bouger_pion(case_x + 1, case_y - 1)

                    elif event.key == pygame.K_DOWN:
                        bouger_pion(case_x - 1, case_y - 1)

        # Actualiser l'affichage après chaque événement
        actualise_affichage()

        # Dessiner le contour si un pion est sélectionné
        if pion_selectionne:
            case_x, case_y = pion_selectionne
            dessiner_contour_pion(case_x, case_y)

        # Mettre à jour l'écran avec le dessin effectué
        pygame.display.flip()
