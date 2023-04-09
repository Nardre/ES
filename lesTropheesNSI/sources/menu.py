#!/bin/python3

# import
import pygame
from pygame.locals import *

class Menu:
    def __init__(self, fenetre):
        self.fenetre = fenetre

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert_alpha()
        self.fenetre.blit(image, pos)

    def afficheAll(self):
        self.affiche("menu.xcf", (0, 0))
        self.affiche("logo.xcf", (160, 0))

    def check(self):
        return "menu"
