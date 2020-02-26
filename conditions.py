#coding:utf-8
# les conditions en python
# python conditions.py
"""
 opérateurs de comparaison: 1- == (égale à)
                            2- != (différent de)
                            3- <  (plus petit que)
                            4- >  (plus grand que)
                            5- <= (plus petit ou égale à)
                            6- >= (plus grand ou égale à)

 mots clés des conditions : if / elif / else                            
                            IF:    il faut avoir condition
                            ELIF:  il faut avoir condition
                            ELSE:  pas forcément la condition (exécution automatique si la condition de IF n'est pas vérifiée)
 conditions multiples     : 1- and (ET)
                            2- or (OU)
                            3- in / not in (DANS/PAS DANS)
"""
# IF simple

identifiant = "ABDELMALEK"
mot_de_passe = "Abdelmalek"

username = input("donner votre nom:")
password = input("donner votre mot de passe:")

if username == identifiant and password == mot_de_passe:
        print("you are connected, welcome")


#  IN/NOT IN 
lettre = "b"
if lettre in "aeiouy":
    print("la lettre est une VOYELLE")
else:
    print("la lettre est une CONSONNE")

# IF structurée(elif)
age = 19

if age == 20:
    print("tu es un jeune homme")
elif age == 50: 
    print("tu es un vieux")
else: 
    print("tu es majeur")

if age > 0 and age < 100:      #   0 < age < 100
    print("votre age est valide")
else:
    print("votre age n'est pas valide")
