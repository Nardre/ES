import pygame
from pygame.locals import *

class Bouton:
    def __init__(self, nom, pos, dim, fenetre, listNom=None, bonus=None):
        self.nom = nom
        self.pos = pos
        self.dim = dim
        self.fenetre = fenetre
        self.listNom = listNom
        self.bool = False
        self.bonus = bonus

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert_alpha()
        self.fenetre.blit(image, pos)

    def afficheAll(self):
        self.affiche(self.nom, self.pos)

    def clique(self, pos):
        x, y = pos
        xPos, yPos = self.pos
        xDim, yDim = self.dim
        if xPos < x < xPos+xDim and yPos < y < yPos + yDim:
            return True

    def getBool(self):
        return (self.bool, self.bonus)

    def switch(self):
        self.bool = not self.bool
        if self.nom == self.listNom[0]:
            self.nom = self.listNom[1]
        else:
            self.nom = self.listNom[0]
