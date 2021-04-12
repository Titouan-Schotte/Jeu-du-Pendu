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
    new_game = input("Nouvelle partie ??? ("+color.CGREEN+"y"+color.CEND+"/"+color.CRED+"n"+color.CEND+") \n -> ")
    if new_game == "y":
        print(color.CYELLOW+"\n\n\n\n\n\n\nNOUVELLE PARTIE "+color.CEND)
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
        randomnumber = random.randint(0 , 58)
        liste = ['protocole', 'injection', 'cryptographie', 'web', 'internet', 'http', 'cryptomonnaie', 'bitcoin',
                 'hacking', 'php', 'html', 'css', 'sql', 'java', 'javascript',
                 'ddos', 'bug-bounty', 'bug', 'c', 'c sharp', 'c++', 'ruby', 'python', 'dart', 'ethereum', 'script',
                 'snowden', 'constructeur', 'classe', 'variable', 'fonction',
                 'net', 'fishing', 'informatique', 'enigma', 'framework', 'heritage', 'liste', 'github', 'sniffer',
                 'tcp', 'udp', 'binaire', 'hexadecimal', 'donnee', 'metadonnee',
                 'paquet', 'serveur', 'client', 'database', 'ip', 'adresse mac', 'arp', 'pare feu', 'linux', 'kali linux', 'arch linux', 'thor'] #58 words
        solution = liste[randomnumber]
        #on définit le nombre de tentatives que l'utilisateur va avoir pour réussir :
        tentatives = 7
        affichage = ""
        lettres_trouvees = ""

        tentatives_string = color.CBLUE + str(tentatives) + color.CEND




        for l in solution:
            if l != " ":
                if l != "-":
                    affichage +="_ "
            if l == " ":
                affichage += " "
            if l == "-":
                affichage += "- "
        print("\n"+ color.CITALIC + "=> Vous avez {} tentatives pour réussir ! GOOD LUCK ;)".format(tentatives_string) + color.CEND)
        while tentatives > 0:
            print("\n"+ color.CUNDERLINE + "Mot à deviner :" + color.CEND + "", affichage)
            n = 0
            while n != 1:
                proposition = input("proposez une lettre : \n").lower()
                prop_lenght = len(proposition)
                if prop_lenght <= 1:
                    n += 1
                if prop_lenght > 1 or proposition.isdigit():
                    n = 0
                    print(color.CRED + "Veuillez entrer une lettre uniquement !"+color.CEND)


            if proposition in solution:
                lettres_trouvees = lettres_trouvees + proposition

                print(color.CSELECTED+'-> Bravo vous avez trouvé la lettre "{}" .'.format(proposition)+color.CEND)

        #différentes tentatives, -1 tentative à chaque essai !
            else:
                tentatives = tentatives - 1

                print(color.CSELECTED+"-> Nope"+color.CEND+"\n")

                if tentatives==0:
                    print(" =========="+color.CYELLOW+"@"+color.CEND+color.CGREY+"= "+color.CEND)
                if tentatives<=1:
                    print(" ||"+ color.CYELLOW + "/       |  "+color.CEND)
                if tentatives<=2:
                    print(" ||        "+color.CBEIGE+"0"+color.CEND)
                if tentatives<=3:
                    print(" ||       "+color.CBEIGE+"/|\   "+color.CEND)
                if tentatives<=4:
                    print(" ||        "+color.CBEIGE+"|"+color.CEND)
                if tentatives<=5:
                    print(color.CYELLOW+"/"+color.CEND+"||       "+color.CBEIGE+"/ \  "+color.CEND+"   ")
                if tentatives<=6:
                    print("==============\n")
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
                    if x == " ":
                        affichage += " "
                    elif x == "-":
                        affichage += "- "
                    else:
                        affichage += "_ "
#Win
            if "_" not in affichage:
                print("\n"+color.CGREENBG2 + "=====================" + color.CEND)
                print("     * " + color.CYELLOW + "YOU WIN" + color.CEND + " *    ")
                print(color.CGREENBG2 + "=====================" + color.CEND+"\n")
                print('Le mot était : ' + color.CBLUE + color.CBOLD + '{}'.format(solution) + color.CEND + color.CEND)
                new_game()
#Lose





#Init Game
game()