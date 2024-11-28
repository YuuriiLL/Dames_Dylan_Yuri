#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys

def bouge_droite():
    global screen, pion, largeur_x, longeur_y, pion_pos, case_size
    if pion_pos < 9:
        pion_pos += 1
        dessine_case()
        screen.blit(pion, (pion_pos * case_size[0], 0))

def bouge_gauche():
    global screen, pion, largeur_x, longeur_y, pion_pos, case_size
    if pion_pos > 0:
        pion_pos -= 1
        dessine_case()
        screen.blit(pion, (pion_pos * case_size[0], 0))

def dessine_case():
    for i in range(10):  # Boucle pour les lignes
        for a in range(10):  # Boucle pour les colonnes
            x = i * largeur_x / 10  # Position x de la case
            y = a * longeur_y / 10  # Position y de la case
            couleur = blanc if (i + a) % 2 == 0 else noir  # Alternance des couleurs
            pygame.draw.rect(screen, couleur, (x, y, largeur_x / 10, longeur_y / 10))  # Dessin de la case

pygame.init()

plateau = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
#asdsdsad
pion_pos = 0

largeur_x = 600
longeur_y = 600  

case_size = (largeur_x / 10, longeur_y / 10)#salut 

blanc = (255, 255, 255)
noir = (0, 0, 0)

path_to_images = "img\\MA-24_pion.png"

screen = pygame.display.set_mode((largeur_x, longeur_y))

pygame.display.set_caption("MA-24 : Bases de pygame")
screen.fill((blanc))

dessine_case()#dessine case

pion = pygame.image.load(path_to_images)
pion = pygame.transform.scale(pion, (largeur_x / 10, longeur_y / 10))
screen.blit(pion, (0, 0))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bouge_droite()
            elif event.key == pygame.K_LEFT:
                bouge_gauche()
            elif event.key == pygame.K_q:
                running = False
        pygame.display.update()

pygame.quit()
sys.exit()
