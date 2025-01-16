import pygame
from code_gfx import screen, case_size, actualise_affichage, pions_positions

# Variables globales
pion_selectionne = None
couleur_selectionnee = None
couleur_contour = (255, 0, 0)  # Couleur du contour, rouge ici

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

    # Vérifier si un pion existe à la position sélectionnée
    for couleur, positions in pions_positions.items():
        if (case_x, case_y) in positions:
            if couleur == tour_actuel:  # Vérifier que c'est le tour de cette couleur
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

                # Promotion en reine si le pion atteint la dernière rangée
                if couleur_selectionnee == "blanc" and case_y == 9:
                    pions_positions["blanc"].remove((x, y))
                    pions_positions["blanc"].append((case_x, case_y, "reine"))  # Ajouter l'attribut 'reine'
                    print("Un pion blanc est devenu reine !")
                elif couleur_selectionnee == "noir" and case_y == 0:
                    pions_positions["noir"].remove((x, y))
                    pions_positions["noir"].append((case_x, case_y, "reine"))  # Ajouter l'attribut 'reine'
                    print("Un pion noir est devenu reine !")
                else:
                    # Déplacement normal du pion
                    pions_positions[couleur_selectionnee].remove((x, y))
                    pions_positions[couleur_selectionnee].append((case_x, case_y))

                # Mettre à jour la sélection et le tour
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
    toutes_positions = [pos for positions in pions_positions.values() for pos in positions]

    # Vérification des captures possibles
    if couleur == "noir":
        # Capture possible vers la gauche-haut
        if case_x - 2 >= 0 and case_y - 2 >= 0:
            if (case_x - 1, case_y - 1) in pions_positions["blanc"] and (
            case_x - 2, case_y - 2) not in toutes_positions:
                cases_possibles.append((case_x - 2, case_y - 2))

        # Capture possible vers la droite-haut
        if case_x + 2 < 10 and case_y - 2 >= 0:
            if (case_x + 1, case_y - 1) in pions_positions["blanc"] and (
            case_x + 2, case_y - 2) not in toutes_positions:
                cases_possibles.append((case_x + 2, case_y - 2))

    elif couleur == "blanc":
        # Capture possible vers la gauche-bas
        if case_x - 2 >= 0 and case_y + 2 < 10:
            if (case_x - 1, case_y + 1) in pions_positions["noir"] and (case_x - 2, case_y + 2) not in toutes_positions:
                cases_possibles.append((case_x - 2, case_y + 2))

        # Capture possible vers la droite-bas
        if case_x + 2 < 10 and case_y + 2 < 10:
            if (case_x + 1, case_y + 1) in pions_positions["noir"] and (case_x + 2, case_y + 2) not in toutes_positions:
                cases_possibles.append((case_x + 2, case_y + 2))

    # Si des captures sont possibles, on retourne uniquement ces cases
    if cases_possibles:
        return cases_possibles

    # Sinon, on retourne aussi les mouvements normaux
    if couleur == "noir":
        # Mouvement normal vers la gauche-haut
        if case_x - 1 >= 0 and case_y - 1 >= 0 and (case_x - 1, case_y - 1) not in toutes_positions:
            cases_possibles.append((case_x - 1, case_y - 1))

        # Mouvement normal vers la droite-haut
        if case_x + 1 < 10 and case_y - 1 >= 0 and (case_x + 1, case_y - 1) not in toutes_positions:
            cases_possibles.append((case_x + 1, case_y - 1))

    elif couleur == "blanc":
        # Mouvement normal vers la gauche-bas
        if case_x - 1 >= 0 and case_y + 1 < 10 and (case_x - 1, case_y + 1) not in toutes_positions:
            cases_possibles.append((case_x - 1, case_y + 1))

        # Mouvement normal vers la droite-bas
        if case_x + 1 < 10 and case_y + 1 < 10 and (case_x + 1, case_y + 1) not in toutes_positions:
            cases_possibles.append((case_x + 1, case_y + 1))
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




