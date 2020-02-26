#coding:utf-8
# dir > nom_fichier.txt : pour créer n'importe quel fichier en windows
# variables in python

""" Nommer une variable: 1- doit commencer par une lettre ou un underscore 
                         2- ne contient pas de caractères spéciaux
                         3- ne pas contenir des espaces
                         4- utiliser les underscores(_)
    
    Types standards: 1- entier(int)
                     2- réel(float)
                     3- caractère(char)
                     4- chaine de caractères(string)
                     5- booléen(bool)

    Fonctions vues: 1-type()                       -> est une fonction pour savoir le TYPE de donnée 
                    2-print("",)                   -> affichage d'une valeur d'une variable                  
                    3-format(,):                   -> formater une chaine
                    4-input():                     -> lire au clavier
                    5-int(),float(),str(),bool()   -> "caster" une donnée 
"""                  

Age = 19
nom = "ABDELMALEK BENMEZIANE"
taille = 1.75
handsome = True
booleen = False

# affichages des types de ces variables
print(type(Age))
print(type(nom))
print(type(taille))
print(type(handsome))

# affichages des valeurs de ces variables
print("mon age est:",Age)
print("mon nom est:",nom)
print("ma taille est:",taille)
print("je suis beau:",handsome)
print("mon age est {} et mon nom est {}. ".format(Age, nom))

# caster une booleen
print(str(booleen))