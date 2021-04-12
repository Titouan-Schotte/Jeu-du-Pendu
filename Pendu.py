"""
Projet : Pendu
Version : 2.0
Author : Titouan Schotté
Python 3.9
"""


import random
import os
import color
from os import system, name

print("==========================================\n>> #--" + color.CGREEN + "Bienvenue dans le jeu du pendu" + color.CEND + "--# <<\n==========================================")



#Nouvelle partie ?
def new_game():

    new_game = "y"
    new_game = input("Nouvelle partie ??? (y/n) \n -> ")
    if new_game == "y":
        return game()
    if new_game != "y":
        print("Merci d'avoir joué à mon jeu !!")
        print(
            color.CRED + "Si un quelconque beug est détecté contactez " + color.CEND + color.CYELLOW + "Titoune#1870" + color.CEND + color.CRED + " sur Discord" + color.CEND)
        print(color.CGREEN + "Si vous avez des suggestions n'hésitez pas aussi c'est une V1 !!" + color.CEND)
        exit()









#JEU PRINCIPAL
def game():



        # choix d'un mot au hasard dans un dictionnaire
        randomnumber = random.randint(0 , 50)
        liste = ['protocole', 'injection', 'cryptographie', 'web', 'internet', 'http', 'cryptomonnaie', 'bitcoin',
                 'hacking', 'php', 'html', 'css', 'sql', 'java', 'javascript',
                 'ddos', 'bug-bounty', 'bug', 'c', 'c sharp', 'c++', 'ruby', 'python', 'dart', 'ethereum', 'script',
                 'snowden', 'constructeur', 'classe', 'variable', 'fonction',
                 'net', 'fishing', 'informatique', 'enigma', 'framework', 'heritage', 'liste', 'github', 'sniffer',
                 'tcp', 'udp', 'binaire', 'hexadecimal', 'donnee', 'metadonnee',
                 'paquet', 'serveur', 'client', 'database']
        solution = liste[randomnumber]
        #on définit le nombre de tentatives que l'utilisateur va avoir pour réussir :
        tentatives = 7
        affichage = ""
        lettres_trouvees = ""

        tentatives_string = color.CBLUE + str(tentatives) + color.CEND




        for l in solution:
          affichage = affichage + "_ "
        print("\n"+ color.CITALIC + "=> Vous avez {} tentatives pour réussir ! GOOD LUCK ;)".format(tentatives_string) + color.CEND)
        while tentatives > 0:
          print("\n"+ color.CUNDERLINE + "Mot à deviner :" + color.CEND + "", affichage)
          proposition = input("proposez une lettre : \n")[0:1].lower()

          if proposition in solution:
              lettres_trouvees = lettres_trouvees + proposition

              print('-> Bravo vous avez trouvé la lettre "{}" .'.format(proposition))

        #différentes tentatives, -1 tentative à chaque essai !
          else:
            tentatives = tentatives - 1

            print("-> Nope\n")

            if tentatives==0:
                print(color.CGREY+" =========="+color.CEND+color.CYELLOW+"@"+color.CEND+color.CGREY+"= "+color.CEND)
            if tentatives<=1:
                print(color.CGREY  + " ||"+color.CEND+ color.CYELLOW + "/       |  "+color.CEND)
            if tentatives<=2:
                print(color.CGREY+" ||"+color.CEND+"        "+color.CBEIGE+"0"+color.CEND)
            if tentatives<=3:
                print(color.CGREY + " ||"+color.CEND+"       "+color.CBEIGE+"/|\   "+color.CEND)
            if tentatives<=4:
                print(color.CGREY+" ||"+color.CEND+"        "+color.CBEIGE+"|"+color.CEND)
            if tentatives<=5:
                print(color.CYELLOW+"/"+color.CEND+color.CGREY+"||"+color.CEND+"       "+color.CBEIGE+"/ \  "+color.CEND+"   ")
            if tentatives<=6:
                print(color.CGREY+"==============\n"+color.CEND)
            if tentatives == 0:
                print('Le mot était : ' + color.CBLUE + color.CBOLD + '{}'.format(solution) + color.CEND + color.CEND)

                print(color.CVIOLET + "=====================" + color.CEND)
                print("    * " + color.CBACKRED + "GAME OVER" + color.CEND + " *    ")
                print(color.CVIOLET + "=====================" + color.CEND)
                new_game()

#Lettre trouvée

          affichage = ""
          for x in solution:
              if x in lettres_trouvees:
                  affichage += x + " "
              else:
                  affichage += "_ "
#Win
          if "_" not in affichage:

            print(">>> Gagné! <<<")
            print("Le mot était bien {}".format(solution))
            new_game()
#Lose





#Init Game
game()