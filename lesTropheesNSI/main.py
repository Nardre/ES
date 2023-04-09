#!/bin/python3

# import
import pygame
from pygame.locals import *
from sources.menu import *
from sources.mission import *
from sources.pnj import *
from sources.bouton import *
from sources.barre import *
from sources.quizz import *

# initialisation
height, width = 960, 960

# fenetre
pygame.init()
fenetre = pygame.display.set_mode((height, width))
pygame.display.set_caption("CO2, l'avenir de la planète")


#auto
AUTOFPS = USEREVENT + 1
pygame.time.set_timer(AUTOFPS, 64)


# scene
scene = Menu(fenetre)

"""
#######################################################################
                        le jeu principal
#######################################################################
"""

# bouton
menuMission0 = Bouton("bouton3.xcf", (60, 192), (240, 80), fenetre)

# case
case0 = Bouton("case.xcf", (32*2, 32*25), (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
case1 = Bouton("case.xcf", (32*2, 32*27), (32, 32), fenetre, ["case.xcf", "case1.xcf"], 2)
case2 = Bouton("case.xcf", (32*5, 32*25), (32, 32), fenetre, ["case.xcf", "case1.xcf"], 1)
case3 = Bouton("case.xcf", (32*11, 32*25), (32, 32), fenetre, ["case.xcf", "case1.xcf"], 2)
case4 = Bouton("case.xcf", (32*11, 32*27), (32, 32), fenetre, ["case.xcf", "case1.xcf"], 1)
case5 = Bouton("case.xcf", (32*14, 32*25), (32, 32), fenetre, ["case.xcf", "case1.xcf"], -2)
case6 = Bouton("case.xcf", (32*17, 32*25), (32, 32), fenetre, ["case.xcf", "case1.xcf"], 2)
case7 = Bouton("case.xcf", (32*20, 32*25), (32, 32), fenetre, ["case.xcf", "case1.xcf"], 1)
listCase = [case0, case1, case2, case3, case4, case5, case6, case7]

# pnj
arbre = Pnj("arbre.xcf", (23, 1), ["Un arbre absorbe", "environ 25kg", "de CO2 par an", "Le CO2 stocké", "par l'arbre lui sert", "donc indirectement", "à faire pousser ses", "différentes", "parties"], fenetre, fois=(17, 20, 9, 12), interaction=[17, 9, 160, 160])

champs = Pnj("champs.xcf", (25, 1), ["l'empreinte carbone", "du secteur de l’agriculture", "représente environ un"," dixième des émissions", "de GES mondiales. ,", "à 41% des cultures et", "à 11% des", "machines agricoles"], fenetre, fois=(13, 19, 0, 6, 2), interaction=[13, 0, 256, 256])

ville1 = Pnj("ville1.xcf", (99, 99), [""], fenetre, fois=(11, 12, 13, 14), interaction=[11, 14, 160, 160])
ville0 = Pnj("ville.xcf", (23, 4), ["les villes", "augmentent le CO2"], fenetre, fois=(11, 12, 8, 9), interaction=[11, 8, 160, 160])

route = Pnj("route.xcf", (99, 99), "", fenetre, fois=(13, 14, 14, 15), interaction=[13, 14, 320, 320])
voiture0 = Pnj("voiture.xcf", (23, 10), [""], fenetre, fois=(15, 16, 13, 14), interaction=[15, 13, 32, 32])
voiture1 = Pnj("voiture.xcf", (23, 10), ["les voitures", "augmentent le CO2"], fenetre, fois=(14, 15, 10, 11), interaction=[14, 10, 32, 32])

bus = Pnj("bus.xcf", (25, 10), ["un trajet en bus consomme en moyenne 104 g / km ,", "a privilégiez a la", "voiture /  voiture : 134 g / km"], fenetre, fois=(15, 16, 15, 16), interaction=[15, 15, 32, 32])

tri = Pnj("tri.xcf", (23, 13), ["Le recyclage des déchets" ,"en France permet d'éviter", "l'équivalent de 5%", "des émissions nationales ", "annuelles de CO2"], fenetre, fois=(12, 13, 7, 8), interaction=[12, 7, 32, 32])

nucleaire = Pnj("nucleaire.xcf", (23, 15), ["Les centrales ","thermiques", "sont les plus", "répandues ,", "ce sont aussi celles", "qui émettent le plus", "de CO2 par kWh produit :", "73 % des émissions"], fenetre, fois=(16, 17, 21, 22), interaction=[16, 21, 160, 160])

eolienne = Pnj("eolienne.xcf", (23, 19), ["Une éolienne terrestre émet", "en moyenne 12,7 g", "de CO2 par kWh ,", "ce qui est une source", "d'Énergie bas carbone"], fenetre, fois=(16, 17, 14, 17), interaction=[16, 14, 160, 160])

soleil = Pnj("soleil.xcf", (-2, 23), ["","","         soleil"], fenetre, interaction=[-2, 23, 160, 160], booll=True)
barre = Pnj("barre.xcf", (-5, 0), ["","","","","","","","","","Barre de neutralité carbonne", "équilibre entre les émissions de CO2", "et leur éliminations de l'atmosphère"], fenetre, interaction=[-3, 0, 320, 320], booll=True)
temperature = Pnj("temperature.xcf", (-2, 10), ["","","","","","","","","","","Les gaz à effet de serre", "augmentent la température"], fenetre, interaction=[-1, 10, 160, 160], booll=True)
iceberg = Pnj("iceberg0.xcf", (7, 18), ["","","","","","","","plus il fait chaud", "plus les iceberg fond", "plus le niveau de l'eau augmente"], fenetre, ["iceberg0.xcf", "iceberg1.xcf"], listCase, interaction=[7, 18, 160, 160], booll=True, trigger=3)

mer = Pnj("mer0.xcf", (-2, -2), ["","","","","","","","","la neutralité carbonne est trop déséquilibre", "il fait trop chaud", "l'iceberg a fondu", "et la ville est submergée"], fenetre, ["mer0.xcf", "mer1.xcf"], listCase, interaction=[0, 0, 0, 0], booll=True, trigger=9)

decoListMission0 = [soleil, barre, temperature, iceberg, mer]
pnjList0 = [soleil, route, ville0, ville1, barre, temperature, iceberg, arbre, champs, \
voiture0, voiture1, bus, tri, nucleaire, eolienne, mer, menuMission0]

boutonListMission0 = [(case0, [arbre]), 
					  (case1, [champs]), 
                      (case2, [ville0, ville1]),
					  (case3, [voiture0, voiture1]), 
					  (case4, [bus]), 
					  (case5, [tri]),
                      (case6, [nucleaire]),
                      (case7, [eolienne])]

# barre
barreNeutralite = Barre(listCase, (210, 38), 10, 50, (20, 0), fenetre)
barreTemperature = Barre(listCase, (459, 68), 3, 20, (0, 5), fenetre, (255, 0, 0))

"""
#######################################################################
                               Menu
#######################################################################
"""


# bouton de retour
menuMission1 = Bouton("bouton3.xcf", (60, 64), (240, 80), fenetre)
menuMission2 = Bouton("bouton3.xcf", (60, 64), (240, 80), fenetre)

pnjList1 = []
pnjList2 = []

# mission
mission0 = Mission("mission0.xcf", fenetre, pnjList0)
mission1 = Mission("mission1.xcf", fenetre, pnjList1)
mission2 = Mission("mission2.xcf", fenetre, pnjList2)

# bouton
bouton0 = Bouton("bouton0.xcf", (64, 512), (480, 160), fenetre)
bouton1 = Bouton("bouton1.xcf", (64, 666), (480, 160), fenetre)
bouton2 = Bouton("bouton2.xcf", (64, 824), (480, 160), fenetre)
boutonList = [(bouton0, mission0), (bouton1, mission1), (bouton2, mission2)]

"""
#######################################################################
                                Quizz
#######################################################################
"""

# quizz
points = 0
quizzPos = ((32*3, 32*17), (32*3, 32*22), (32*3, 32*27))

quizz0Question = ["Quel serait l'impact d'une montée", "des eaux ? "]
quizz0Case0 = Bouton("case.xcf", quizzPos[0], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz0Case1 = Bouton("case.xcf", quizzPos[1], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz0Case2 = Bouton("case.xcf", quizzPos[2], (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz0Text0 = (["1) rendre inhabitable des zones géographiques "], quizzPos[0])
quizz0Text1 = (["2) un changement des courants marins"], quizzPos[1])
quizz0Text2 = (["3) les deux"], quizzPos[2])
quizz0ListCase = [[quizz0Case0, quizz0Text0], 
                  [quizz0Case1, quizz0Text1], 
                  [quizz0Case2, quizz0Text2]]
quizz0 = Quizz(fenetre, quizz0Question, quizz0ListCase)

quizz1Question = ["Combien de g de co2 produit le trajet", "d'un bus ", "(d'ailleurs la voiture consomme : 134 g / km)"]
quizz1Case0 = Bouton("case.xcf", quizzPos[0], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz1Case1 = Bouton("case.xcf", quizzPos[1], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz1Case2 = Bouton("case.xcf", quizzPos[2], (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz1Text0 = (["1 ) 50g/km "], quizzPos[0])
quizz1Text1 = (["2) 5g/m "], quizzPos[1])
quizz1Text2 = (["3) 104 g / km"], quizzPos[2])
quizz1ListCase = [[quizz1Case0, quizz1Text0], 
                  [quizz1Case1, quizz1Text1], 
                  [quizz1Case2, quizz1Text2]]
quizz1 = Quizz(fenetre, quizz1Question, quizz1ListCase)
 
quizz2Question = ["Quel source d'énergie n'est", "pas renouvelable ?  "]
quizz2Case0 = Bouton("case.xcf", quizzPos[0], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz2Case1 = Bouton("case.xcf", quizzPos[1], (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz2Case2 = Bouton("case.xcf", quizzPos[2], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz2Text0 = (["1) énergie géothermique  "], quizzPos[0])
quizz2Text1 = (["2) énergie nucléaire  "], quizzPos[1])
quizz2Text2 = (["3) biomasse "], quizzPos[2])
quizz2ListCase = [[quizz2Case0, quizz2Text0], 
                  [quizz2Case1, quizz2Text1], 
                  [quizz2Case2, quizz2Text2]]
quizz2 = Quizz(fenetre, quizz2Question, quizz2ListCase)

quizz3Question = ["Quel élément a la plus grand impact", "sur la neutralité carbone ?", \
"(41 % du total des émissions)"]
quizz3Case0 = Bouton("case.xcf", quizzPos[0], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz3Case1 = Bouton("case.xcf", quizzPos[1], (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz3Case2 = Bouton("case.xcf", quizzPos[2], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz3Text0 = (["1) la déforestation "], quizzPos[0])
quizz3Text1 = (["2) la production d'énergie "], quizzPos[1])
quizz3Text2 = (["3) les transports "], quizzPos[2])
quizz3ListCase = [[quizz3Case0, quizz3Text0],
                  [quizz3Case1, quizz3Text1],
                  [quizz3Case2, quizz3Text2]]
quizz3 = Quizz(fenetre, quizz3Question, quizz3ListCase)

quizz4Question = ["De nos jour, en combien d'années nous", \
                  "faut-il pour prendre 1°C sur la", "température globale ? ", \
                  "(sachant que de manière naturel", " cela prendrait 4000 années)"]
quizz4Case0 = Bouton("case.xcf", quizzPos[0], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz4Case1 = Bouton("case.xcf", quizzPos[1], (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz4Case2 = Bouton("case.xcf", quizzPos[2], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz4Text0 = (["1) 100 ans "], quizzPos[0])
quizz4Text1 = (["2) 150 ans "], quizzPos[1])
quizz4Text2 = (["3) 200 ans "], quizzPos[2])
quizz4ListCase = [[quizz4Case0, quizz4Text0],
                  [quizz4Case1, quizz4Text1],
                  [quizz4Case2, quizz4Text2]]
quizz4 = Quizz(fenetre, quizz4Question, quizz4ListCase)

quizz5Question = ["En moyenne un Français émet: ", \
                  "nous pouvons réduire nos émissions", \
                  "a l'aide d'une conduite plus responsable"]
quizz5Case0 = Bouton("case.xcf", quizzPos[0], (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz5Case1 = Bouton("case.xcf", quizzPos[1], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz5Case2 = Bouton("case.xcf", quizzPos[2], (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz5Text0 = (["1) 4,47 tonnes "], quizzPos[0])
quizz5Text1 = (["2) 3.14 tonnes "], quizzPos[1])
quizz5Text2 = (["3) 9.81 tonnes "], quizzPos[2])
quizz5ListCase = [[quizz5Case0, quizz5Text0],
                  [quizz5Case1, quizz5Text1],
                  [quizz5Case2, quizz5Text2]]
quizz5 = Quizz(fenetre, quizz5Question, quizz5ListCase)

quizz6Question = []
quizz6Case0 = Bouton("case.xcf", (999, 999), (32, 32), fenetre, ["case.xcf", "case2.xcf"], 1)
quizz6Case1 = Bouton("case.xcf", (999, 999), (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz6Case2 = Bouton("case.xcf", (999, 999), (32, 32), fenetre, ["case.xcf", "case1.xcf"], -1)
quizz6Text0 = ([], (999, 999))
quizz6Text1 = ([], (999, 999))
quizz6Text2 = ([], (999, 999))
quizz6ListCase = [[quizz6Case0, quizz6Text0],
                  [quizz6Case1, quizz6Text1],
                  [quizz6Case2, quizz6Text2]]

quizz6 = Quizz(fenetre, quizz6Question, quizz6ListCase)
quizzListCases = [quizz0ListCase, quizz1ListCase, quizz2ListCase, 
                  quizz3ListCase, quizz4ListCase, quizz5ListCase, quizz6ListCase]
listQuizz = [quizz0, quizz1, quizz2, quizz3, quizz4, quizz5, quizz6]
nQuizz = 0
suivant = Bouton("suivant.xcf", (800, 900), (480, 160), fenetre)

# boucle infini
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

        if scene.check() == "menu":
            if event.type == AUTOFPS:
                scene.afficheAll()
                for element in boutonList:
                    bouton = element[0]
                    bouton.afficheAll()
                pygame.display.flip()

            #souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for element in boutonList:
                        bouton, mission = element
                        if bouton.clique(event.pos):
                            scene = mission

        if scene.check() == "mission0.xcf":
            if event.type == AUTOFPS:
                scene.afficheAll()
                for element in boutonListMission0:
                    bouton = element[0]
                    bouton.afficheAll()
                barreNeutralite.afficheAll()
                barreTemperature.afficheAll()
                pygame.display.flip()

            #souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuMission0.clique(event.pos):
                        scene = Menu(fenetre)

                    for element in boutonListMission0:
                        bouton, listEntite = element
                        if bouton.clique(event.pos):
                           for entite in listEntite:
                                entite.switch()
                           bouton.switch() 
                
                if event.button == 3:
                    for element in decoListMission0:
                        element.interact(event.pos)

                    for element in boutonListMission0:
                        bouton, listEntite = element
                        if bouton.getBool()[0]:
                            for entite in listEntite:
                                entite.interact(event.pos)

            # keyboard
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE:
                    scene = Menu(fenetre)
                
        if scene.check() == "mission1.xcf":
            if event.type == AUTOFPS:
                scene.afficheAll()
                menuMission1.afficheAll()
                pygame.display.flip()
            
            #souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuMission1.clique(event.pos):
                        scene = Menu(fenetre)
            # keyboard
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE:
                    scene = Menu(fenetre)

        if scene.check() == "mission2.xcf":
            if event.type == AUTOFPS:
                scene.afficheAll()
                listQuizz[nQuizz].afficheAll()
                suivant.afficheAll()
                menuMission2.afficheAll()
                if nQuizz == len(listQuizz)-1:
                    listQuizz[nQuizz].scoretext(points)
                pygame.display.flip()

            #souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuMission2.clique(event.pos):
                        scene = Menu(fenetre)

                    for bouton, textes in quizzListCases[nQuizz]:
                        if bouton.clique(event.pos):
                           bouton.switch()
                           points += bouton.bonus

                    if suivant.clique(event.pos):
                        nQuizz = (nQuizz + 1) % len(listQuizz)

                        
            # keyboard
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE:
                    scene = Menu(fenetre)

# quit
pygame.quit()
