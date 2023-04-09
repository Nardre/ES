import pygame
from pygame.locals import *

class Barre:
    def __init__(self, listCase, pos, size, tall, aug, fenetre, color=(0, 0, 0)):
        self.listCase = listCase
        self.pos = pos
        self.fenetre = fenetre
        self.color = color
        self.size = size
        self.tall = tall
        self.aug = aug

    def affiche(self):
        total = 0
        for ccase in self.listCase:
            statut, bonus = ccase.getBool()
            if statut:
                total += bonus
        x, y = self.pos
        xaug, yaug = self.aug
        pygame.draw.rect(self.fenetre, self.color, [x+min(7,total)*xaug, y+total*-yaug, self.size, self.tall+total*yaug])

    def afficheAll(self):
        self.affiche()


