import pygame
from pygame.locals import *

class Mission:
    def __init__(self, nom, fenetre, pnjList):
        self.nom = nom
        self.fenetre = fenetre
        self.pnjList = pnjList

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert()
        self.fenetre.blit(image, pos)
    
    def afficheAll(self):
        self.affiche(self.nom, (0, 0))
        for pnj in self.pnjList:
            pnj.afficheAll()

    def check(self):
        return self.nom

