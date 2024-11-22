#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : jeu_dames_projet.py
Authors : Yuri LIMA, Dylan PINTO
Date    : 2024.11.08
"""

import pygame
import sys

def bouge_droite():
    global screen, pion, largeur_x, longeur_y, pion_pos, case_size
    if pion_pos < 9:
        pion_pos += 1
        dessine_case()
        screen.blit(pion, (pion_pos*case_size[0], 0))


def bouge_gauche():
    global screen, pion, largeur_x, longeur_y, pion_pos, case_size
    if pion_pos > 0:
        pion_pos -= 1
        dessine_case()
        screen.blit(pion, (pion_pos*case_size[0], 0))

def dessine_case():
    for i in range(10):
        k = i * largeur_x / 10
        couleur = blanc if i % 2 == 0 else noir
        pygame.draw.rect(screen, couleur, (k, 0, largeur_x / 10, longeur_y))

pygame.init()

plateau = [0,1,0,1,0,1,0,1,0,1]



pion_pos = 0

largeur_x = 600
longeur_y = 60

case_size = (largeur_x/10, longeur_y)

blanc = (255, 255, 255)
noir = (0, 0, 0)

path_to_images = "img\\MA-24_pion.png"

screen = pygame.display.set_mode((largeur_x,longeur_y))

pygame.display.set_caption("MA-24 : Bases de pygame")
screen.fill((blanc))

dessine_case()

pion = pygame.image.load(path_to_images)
pion = pygame.transform.scale(pion, (largeur_x / 10, longeur_y))
screen.blit(pion, (0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()
        if btn_presse[pygame.K_RIGHT]:
            bouge_droite()
        elif btn_presse[pygame.K_LEFT]:
            bouge_gauche()
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()

pygame.quit()
sys.exit()
