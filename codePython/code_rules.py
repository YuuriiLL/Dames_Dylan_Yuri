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


# Variable globale pour suivre le tour actuel
tour_actuel = "blanc"  # Le jeu commence par le tour des blancs


def bouger_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, pions_positions, tour_actuel

    if pion_selectionne and couleur_selectionnee:
        x, y = pion_selectionne

        if 0 <= case_x < 10 and 0 <= case_y < 10:
            toutes_positions = [pos for positions in pions_positions.values() for pos in positions]

            # Vérifier que c'est le tour de la bonne couleur
            if couleur_selectionnee != tour_actuel:
                print(f"C'est le tour des {tour_actuel} !")
                return  # Bloquer le mouvement si ce n'est pas le tour

            # Vérifier que la case cible est libre
            if (case_x, case_y) not in toutes_positions:
                # Vérifier la direction du mouvement selon la couleur
                if couleur_selectionnee == "noir" and case_y < y:  # Noir va vers le haut
                    pions_positions[couleur_selectionnee].remove((x, y))
                    pions_positions[couleur_selectionnee].append((case_x, case_y))
                    pion_selectionne = (case_x, case_y)
                    print(f"Pion noir déplacé à {(case_x, case_y)}")

                elif couleur_selectionnee == "blanc" and case_y > y:  # Blanc va vers le bas
                    pions_positions[couleur_selectionnee].remove((x, y))
                    pions_positions[couleur_selectionnee].append((case_x, case_y))
                    pion_selectionne = (case_x, case_y)
                    print(f"Pion blanc déplacé à {(case_x, case_y)}")

                else:
                    print("Mouvement invalide pour cette couleur")

                # Changer le tour après un mouvement valide
                tour_actuel = "noir" if tour_actuel == "blanc" else "blanc"

                # Actualiser l'affichage
                actualise_affichage()
            else:
                print("La case est déjà occupée.")


def dessiner_contour_pion(case_x, case_y):
    """Dessiner un contour autour de la case contenant le pion sélectionné"""
    if case_x is not None and case_y is not None:
        x, y = case_x * case_size[0], case_y * case_size[1]
        pygame.draw.rect(screen, couleur_contour, (x, y, case_size[0], case_size[1]), 3)  # 3 est l'épaisseur du contour

def start():
    global pion_selectionne, couleur_selectionnee, tour_actuel

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
                        bouger_pion(case_x - 1, case_y + 1)

                    elif event.key == pygame.K_RIGHT:
                        bouger_pion(case_x + 1, case_y + 1)

                    elif event.key == pygame.K_UP:
                        bouger_pion(case_x + 1, case_y - 1)

                    elif event.key == pygame.K_DOWN:
                        bouger_pion(case_x - 1, case_y - 1)

        actualise_affichage()


        # Dessiner le contour si un pion est sélectionné
        if pion_selectionne:
            case_x, case_y = pion_selectionne
            dessiner_contour_pion(case_x, case_y)

        # Mettre à jour l'écran avec le dessin effectué
        pygame.display.flip()
