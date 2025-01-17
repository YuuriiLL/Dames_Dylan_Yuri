import pygame
from code_gfx import screen, case_size, actualise_affichage, pions_positions

# Variables globales que on va utiliser dans notre codes
pion_selectionne = None
couleur_selectionnee = None
couleur_contour = (255, 0, 0)  # couleur que on a definis quand on click sur un pion

def selectionner_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, cases_possibles_affichees

    # Si un pion est déjà sélectionné et qu'on clique sur le même pion
    if pion_selectionne == (case_x, case_y):
        pion_selectionne = None
        couleur_selectionnee = None
        cases_possibles_affichees = []  # Réinitialiser les cases possibles
        print("Pion désélectionné.")
        actualise_affichage(cases_possibles_affichees)
        return

    # Vérifier si a cette endroit selectionner a pion y est deja
    for couleur, positions in pions_positions.items():
        for pos in positions:
            if pos[0] == case_x and pos[1] == case_y:
                if couleur == tour_actuel:  # regarde si c'est le tour de cette couleur
                    pion_selectionne = (case_x, case_y)
                    couleur_selectionnee = couleur
                    cases_possibles_affichees = cases_possibles(case_x, case_y, couleur)
                    print(f"Pion {couleur} sélectionné à {case_x}, {case_y}")
                    actualise_affichage(cases_possibles_affichees)
                    return

    # Si la case sélectionnée ne contient pas de pion valide, désélectionner
    pion_selectionne = None
    couleur_selectionnee = None
    cases_possibles_affichees = []
    print("Aucun pion sélectionné.")
    actualise_affichage(cases_possibles_affichees)


# Variable globale pour definir le tour actuel
tour_actuel = "blanc"  # Le jeu commence par le tour des blancs


def bouger_pion(case_x, case_y):
    global pion_selectionne, couleur_selectionnee, pions_positions, tour_actuel

    if pion_selectionne and couleur_selectionnee:
        x, y = pion_selectionne

        # Vérifie si c'est une dame
        is_reine = (x, y, "reine") in pions_positions[couleur_selectionnee]

        if 0 <= case_x < 10 and 0 <= case_y < 10:
            toutes_positions = [pos[:2] for positions in pions_positions.values() for pos in positions]

            # Vérifie que la case où l'on veut aller est libre
            if (case_x, case_y) not in toutes_positions:
                # Déplacement pour une dame
                if is_reine:
                    if (case_x, case_y) in cases_possibles(x, y, couleur_selectionnee):
                        # Déplacement de la dame
                        pions_positions[couleur_selectionnee].remove((x, y, "reine"))
                        pions_positions[couleur_selectionnee].append((case_x, case_y, "reine"))
                        print(f"Dame {couleur_selectionnee} déplacée à {(case_x, case_y)}")

                        # Si c'est une capture (saut), on retire le pion mangé
                        if abs(case_x - x) == 2 and abs(case_y - y) == 2:
                            case_capturee_x = (x + case_x) // 2
                            case_capturee_y = (y + case_y) // 2
                            adversaire = "noir" if couleur_selectionnee == "blanc" else "blanc"
                            pions_positions[adversaire] = [
                                pion for pion in pions_positions[adversaire]
                                if pion[:2] != (case_capturee_x, case_capturee_y)
                            ]
                            print(f"Pion {couleur_selectionnee} a mangé un pion à {(case_capturee_x, case_capturee_y)}")

                # Déplacement pour un pion normal
                else:
                    if (case_x, case_y) in cases_possibles(x, y, couleur_selectionnee):
                        # Vérifie si c'est une capture
                        if abs(case_x - x) == 2 and abs(case_y - y) == 2:
                            case_capturee_x = (x + case_x) // 2
                            case_capturee_y = (y + case_y) // 2

                            # Retirer le pion adverse de la position de capture
                            adversaire = "noir" if couleur_selectionnee == "blanc" else "blanc"
                            if (case_capturee_x, case_capturee_y) in [pos[:2] for pos in pions_positions[adversaire]]:
                                pions_positions[adversaire] = [
                                    pion for pion in pions_positions[adversaire]
                                    if pion[:2] != (case_capturee_x, case_capturee_y)
                                ]
                                print(f"Pion {couleur_selectionnee} a mangé un pion à {(case_capturee_x, case_capturee_y)}")

                        # Transformation en dame si nécessaire
                        if couleur_selectionnee == "blanc" and case_y == 9:
                            pions_positions["blanc"].remove((x, y))
                            pions_positions["blanc"].append((case_x, case_y, "reine"))
                            print("Un pion blanc est devenu une dame !")
                        elif couleur_selectionnee == "noir" and case_y == 0:
                            pions_positions["noir"].remove((x, y))
                            pions_positions["noir"].append((case_x, case_y, "reine"))
                            print("Un pion noir est devenu une dame !")
                        else:
                            # Déplacement normal
                            pions_positions[couleur_selectionnee].remove((x, y))
                            pions_positions[couleur_selectionnee].append((case_x, case_y))

                # Fin de la sélection et changement de tour
                pion_selectionne = None
                couleur_selectionnee = None
                tour_actuel = "noir" if tour_actuel == "blanc" else "blanc"
                actualise_affichage([])  # Met à jour l'affichage des cases possibles
            else:
                print("La case est déjà occupée.")





def dessiner_contour_pion(case_x, case_y):
    # Dessiner le contour rouge uatour du pion selectionner
    if case_x is not None and case_y is not None:
        x, y = case_x * case_size[0], case_y * case_size[1]
        pygame.draw.rect(screen, couleur_contour, (x, y, case_size[0], case_size[1]), 3)  #  l'épaisseur du contour


def cases_possibles(case_x, case_y, couleur):
    cases_possibles = []
    toutes_positions = [pos[:2] for positions in pions_positions.values() for pos in positions]

    # Vérifier si le pion est une dame
    is_reine = (case_x, case_y, "reine") in pions_positions[couleur]

    if is_reine:
        # Déplacements en diagonale de la dame (avant et arrière)
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Ces directions incluent avant et arrière

        # Déplacements multiples de la dame sans restriction
        for dx, dy in directions:
            i = 1
            while True:
                nx, ny = case_x + i * dx, case_y + i * dy
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if (nx, ny) in toutes_positions:
                        # S'arrête si une pièce bloque le chemin
                        break
                    cases_possibles.append((nx, ny))
                else:
                    break
                i += 1

        # Captures possibles (sauts en diagonale avant et arrière)
        for dx, dy in directions:
            nx, ny = case_x + 2 * dx, case_y + 2 * dy
            mx, my = case_x + dx, case_y + dy
            if (
                    0 <= nx < 10 and 0 <= ny < 10 and
                    (mx, my) in toutes_positions and
                    (nx, ny) not in toutes_positions
            ):
                adversaire = "noir" if couleur == "blanc" else "blanc"
                if (mx, my) in [pos[:2] for pos in pions_positions[adversaire]]:
                    cases_possibles.append((nx, ny))

    else:
        # Déplacement pour un pion normal
        direction = -1 if couleur == "noir" else 1
        for dx in [-1, 1]:
            nx, ny = case_x + dx, case_y + direction
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in toutes_positions:
                cases_possibles.append((nx, ny))

        # Captures possibles pour les pions normaux
        for dx in [-2, 2]:
            nx, ny = case_x + dx, case_y + 2 * direction
            mx, my = case_x + dx // 2, case_y + direction
            if (
                    0 <= nx < 10 and 0 <= ny < 10 and
                    (mx, my) in toutes_positions and
                    (nx, ny) not in toutes_positions
            ):
                adversaire = "noir" if couleur == "blanc" else "blanc"
                if (mx, my) in [pos[:2] for pos in pions_positions[adversaire]]:
                    cases_possibles.append((nx, ny))

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

                # Si un pion est déjà sélectionné
                if pion_selectionne:
                    # Si on clique sur la même case, désélectionner le pion
                    if (case_x, case_y) == pion_selectionne:
                        pion_selectionne = None
                        couleur_selectionnee = None
                        cases_possibles_affichees = []
                        print("Pion désélectionné.")
                        actualise_affichage(cases_possibles_affichees)
                    # Si la case est valide pour un déplacement
                    elif (case_x, case_y) in cases_possibles_affichees:
                        bouger_pion(case_x, case_y)
                        pion_selectionne = None
                        couleur_selectionnee = None
                        cases_possibles_affichees = []
                    else:
                        print("Case invalide pour ce mouvement.")
                else:
                    # Si aucun pion n'est sélectionné, tenter de sélectionner un pion
                    selectionner_pion(case_x, case_y)

        # Actualiser l'affichage
        actualise_affichage(cases_possibles_affichees)

        # Dessiner le contour autour du pion sélectionné (si sélectionné)
        if pion_selectionne:
            case_x, case_y = pion_selectionne
            dessiner_contour_pion(case_x, case_y)

        pygame.display.flip()  # Mettre à jour l'écran
