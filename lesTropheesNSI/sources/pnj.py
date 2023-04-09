import pygame
from pygame.locals import *
import random

class Pnj:
    def __init__(self, nom, pos, txt, fenetre, listNom=None, listCase=None, \
                 fois=None, interaction = None, booll=False, trigger=0):
        self.nom = nom
        self.pos = pos
        self.fenetre = fenetre
        self.listNom = listNom
        self.bool = booll
        self.listCase = listCase
        self.fois = fois
        self.interaction = interaction
        self.boolTxt = False
        self.trigger = trigger

        # color 
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (127, 127, 127)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

        # texte
        self.font = pygame.font.Font('images/ShareTechMono-Regular.ttf', 20)
        self.txt = []
        for texte in txt:
            self.txt += [self.font.render(texte, True, self.black, self.white)]

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert_alpha()
        y, x = pos
        self.fenetre.blit(image, (64+x*32, 64+y*32))

    def afficheAll(self):
        total = 0
        if self.listCase:
            for ccase in self.listCase:
                statut, bonus = ccase.getBool()
                if statut:
                    total += bonus
        if total >= self.trigger and self.listNom:
            self.affiche(self.listNom[1], self.pos)
        else:
	        self.affiche(self.nom, self.pos)

            

        if self.bool and self.fois:
            a, b, c, d = self.fois[:4]
            if len(self.fois)==5:
                step = self.fois[-1]
            else:
                step = 1
            for x in range(a, b, step):
                for y in range(c, d, step):
                    self.affiche(self.nom, (x, y))
		
        if self.boolTxt and self.bool:
            yself, xself, xdim, ydim = self.interaction            
            for i in range(len(self.txt)):
                self.fenetre.blit(self.txt[i], (32+xself*32, 32+(yself)*32+i*20))	

    def switch(self):
        self.bool = not self.bool

    def interact(self, pos):
        x, y = pos
        yself, xself, xdim, ydim = self.interaction
        if x>(xself+2)*32 and x<(xself+2)*32+xdim and y>(yself+2)*32 and y<(yself+2)*32+ydim:
            self.boolTxt = not self.boolTxt

    

