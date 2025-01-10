import pygame
from code_gfx import screen, case_size, actualise_affichage, pions_positions

# Variables globales
pion_selectionne = None
couleur_selectionnee = None
couleur_contour = (255, 0, 0)  # Couleur du contour, rouge ici

def selectionner_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, cases_possibles_affichees

    # Si un pion est déjà sélectionné et qu'on clique sur le même pion, on le désélectionne
    if pion_selectionne and (case_x, case_y) == pion_selectionne:
        pion_selectionne = None
        couleur_selectionnee = None
        cases_possibles_affichees = []  # Réinitialiser les cases possibles
        print("Pion désélectionné.")
        actualise_affichage(cases_possibles_affichees)
        return

    # Vérifier si un pion de la même couleur existe à la nouvelle position
    for couleur, positions in pions_positions.items():
        if (case_x, case_y) in positions:
            if couleur == tour_actuel:  # Vérifier si c'est bien le tour de cette couleur
                pion_selectionne = (case_x, case_y)
                couleur_selectionnee = couleur
                print(f"Pion {couleur} sélectionné à {case_x}, {case_y}")
                # Calculer les cases possibles de ce pion
                cases_possibles_affichees = cases_possibles(case_x, case_y, couleur)
                actualise_affichage(cases_possibles_affichees)
                return  # Sortir dès que le pion est sélectionné






# Variable globale pour suivre le tour actuel
tour_actuel = "blanc"  # Le jeu commence par le tour des blancs


def bouger_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, pions_positions, tour_actuel

    if pion_selectionne and couleur_selectionnee:
        x, y = pion_selectionne

        # Vérifier si la case sélectionnée est parmi les cases possibles
        if (case_x, case_y) not in cases_possibles_affichees:
            print("Mouvement invalide pour ce pion.")
            return  # Ne rien faire si le mouvement n'est pas valide

        if 0 <= case_x < 10 and 0 <= case_y < 10:
            toutes_positions = [pos for positions in pions_positions.values() for pos in positions]

            # Vérifier que c'est le tour de la bonne couleur
            if couleur_selectionnee != tour_actuel:
                print(f"C'est le tour des {tour_actuel} !")
                return  # Bloquer le mouvement si ce n'est pas le tour

            # Vérifier que la case cible est libre
            if (case_x, case_y) not in toutes_positions:
                # Vérifier si c'est un saut (capture)
                if abs(case_x - x) == 2 and abs(case_y - y) == 2:
                    case_capturee_x = (x + case_x) // 2
                    case_capturee_y = (y + case_y) // 2

                    # Retirer le pion adverse de la position de capture
                    if couleur_selectionnee == "noir":
                        pions_positions["blanc"].remove((case_capturee_x, case_capturee_y))
                    else:
                        pions_positions["noir"].remove((case_capturee_x, case_capturee_y))

                    print(f"Pion {couleur_selectionnee} a mangé un pion adverse à {(case_capturee_x, case_capturee_y)}")

                # Déplacer le pion
                pions_positions[couleur_selectionnee].remove((x, y))
                pions_positions[couleur_selectionnee].append((case_x, case_y))
                pion_selectionne = (case_x, case_y)
                print(f"Pion {couleur_selectionnee} déplacé à {(case_x, case_y)}")

                # Changer le tour après un mouvement valide
                tour_actuel = "noir" if tour_actuel == "blanc" else "blanc"

                # Actualiser l'affichage
                actualise_affichage(cases_possibles_affichees)
            else:
                print("La case est déjà occupée.")




def dessiner_contour_pion(case_x, case_y):
    """Dessiner un contour autour de la case contenant le pion sélectionné"""
    if case_x is not None and case_y is not None:
        x, y = case_x * case_size[0], case_y * case_size[1]
        pygame.draw.rect(screen, couleur_contour, (x, y, case_size[0], case_size[1]), 3)  # 3 est l'épaisseur du contour


def cases_possibles(case_x, case_y, couleur):
    cases_possibles = []

    # Pour les pions noirs, on se déplace vers le haut
    if couleur == "noir":
        # Mouvement vers la gauche-haut
        if case_x - 1 >= 0 and case_y - 1 >= 0:
            cases_possibles.append((case_x - 1, case_y - 1))
        # Mouvement vers la droite-haut
        if case_x + 1 < 10 and case_y - 1 >= 0:
            cases_possibles.append((case_x + 1, case_y - 1))

        # Capture d'un pion adverse
        # Si un pion adverse est entre le pion sélectionné et une case vide
        if case_x - 2 >= 0 and case_y - 2 >= 0:
            if (case_x - 1, case_y - 1) in pions_positions["blanc"]:
                cases_possibles.append((case_x - 2, case_y - 2))

        if case_x + 2 < 10 and case_y - 2 >= 0:
            if (case_x + 1, case_y - 1) in pions_positions["blanc"]:
                cases_possibles.append((case_x + 2, case_y - 2))

    # Pour les pions blancs, on se déplace vers le bas
    elif couleur == "blanc":
        # Mouvement vers la gauche-bas
        if case_x - 1 >= 0 and case_y + 1 < 10:
            cases_possibles.append((case_x - 1, case_y + 1))
        # Mouvement vers la droite-bas
        if case_x + 1 < 10 and case_y + 1 < 10:
            cases_possibles.append((case_x + 1, case_y + 1))

        # Capture d'un pion adverse
        # Si un pion adverse est entre le pion sélectionné et une case vide
        if case_x - 2 >= 0 and case_y + 2 < 10:
            if (case_x - 1, case_y + 1) in pions_positions["noir"]:
                cases_possibles.append((case_x - 2, case_y + 2))

        if case_x + 2 < 10 and case_y + 2 < 10:
            if (case_x + 1, case_y + 1) in pions_positions["noir"]:
                cases_possibles.append((case_x + 2, case_y + 2))

    return cases_possibles


def start():
    global pion_selectionne, couleur_selectionnee, tour_actuel, cases_possibles_affichees

    running = True
    cases_possibles_affichees = []  # Liste des cases où le joueur peut déplacer son pion

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                case_x = int(mouse_x // case_size[0])
                case_y = int(mouse_y // case_size[1])

                if pion_selectionne:  # Si un pion est sélectionné
                    if (case_x, case_y) in cases_possibles_affichees:
                        # Si la case est valide, déplacer le pion
                        bouger_pion(case_x, case_y)
                        pion_selectionne = None  # Deselect the pion after moving
                        couleur_selectionnee = None
                        cases_possibles_affichees = []  # Réinitialiser les cases possibles
                    else:
                        print("Case invalide pour ce mouvement.")
                else:
                    # Sélectionner un pion
                    selectionner_pion(case_x, case_y)

                    if pion_selectionne:  # Si un pion est sélectionné, calculer les cases possibles
                        cases_possibles_affichees = cases_possibles(case_x, case_y, couleur_selectionnee)

        # Actualiser l'affichage
        actualise_affichage(cases_possibles_affichees)

        # Dessiner le contour autour du pion sélectionné (si sélectionné)
        if pion_selectionne:
            case_x, case_y = pion_selectionne
            dessiner_contour_pion(case_x, case_y)

        pygame.display.flip()  # Mettre à jour l'écran



