import pygame
from pygame.locals import *

class Quizz:
    
    selfpoint = 0
    
    def __init__(self, fenetre, question, listCase):
        self.fenetre = fenetre
        self.listCase = listCase
        self.font = pygame.font.Font('images/ShareTechMono-Regular.ttf', 25)
        self.question = question
        
        self.image0 = pygame.image.load(f"images/quizz0.png").convert_alpha()
        self.image1 = pygame.image.load(f"images/quizz1.xcf").convert_alpha()
        self.image2 = pygame.image.load(f"images/quizz2.png").convert_alpha()
        self.image3 = pygame.image.load(f"images/quizz3.xcf").convert_alpha()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert_alpha()
        self.fenetre.blit(image, pos)

    def afficheAll(self):
        # texte
        for i in range(len(self.question)):
            texte = self.font.render(self.question[i], True, self.white)
            self.fenetre.blit(texte, (300, 100 + i*20))

        for i in range(3):
            bouton, textes = self.listCase[i]
            bouton.afficheAll()

            # texte
            for i in range(len(textes[0])):
                xpos, ypos = textes[-1]
                texte = self.font.render(textes[0][i], True, self.white)
                self.fenetre.blit(texte, (xpos+64, ypos+(i*20)))
    
    def scoretext(self, points):
        txt = "votre score est de: " + str(points)
        texte = self.font.render(txt, True, self.white)
        self.fenetre.blit(texte, (320, 150))
        if points <= -6:
            txt = ["Sort de ma planète tout de suite"]
            self.fenetre.blit(self.image0, (400, 600))
        elif points <= 0:
            txt = ["Tu es une fraude...", "laisse la planète saine pour les autres"]
            self.fenetre.blit(self.image1, (400, 600))
        elif points <= 4:
            txt = ["Tu est un bon citoyen et le jeu ta permis", \
                    "d'acquérir de nouvelle connaissance, ", \
                    "Bien joué !"]
            self.fenetre.blit(self.image2, (400, 600))
        else:
            txt = ["C'est donc vous le citoyen qui sauvera la Terre ?", \
                   "vous êtes l'élu ! Bien joué"]
            self.fenetre.blit(self.image3, (400, 600))

        for i in range(len(txt)):
            texte = self.font.render(txt[i], True, self.white)
            self.fenetre.blit(texte, (320, 175+25*i))

