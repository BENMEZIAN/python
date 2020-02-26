#coding: utf-8
#python strings.py
# Classe chaine de caractères: strings(str)
import keyword
"""   
les Méthodes des chaines travaillent sur une copie de la chaine, et pas la chaine elle meme

LES Méthodes :  1- str.upper()                        : rendre les lettres majuscules
                2- str.lower()                        : rendre les lettres miniscules
                3- str.capitalize()                   : rendre la première lettre du chaine majuscule
                4- str.title()                        : rendre les lettres du chaque mot majuscule
                5- str.center(<int>,"")               : ajuster le nombre de caractères
                6- str.find(<chaine>)                 : trouver une sous-chaine à partir d'une position
                7- str.index(<chaine>)                : trouver une sous-chaine à partir d'une position
                8- str.strip()                        : enlever tous les espaces dans une chaine
                9- str.replace(<ancienne>,<nouvelle>) : remplacer une chaine par une autre
               10- str.split(separateurr, maxsplit)   : transformer une chaineg vers un tableau
               11- isidentifier()                     : pour les mots résevés au langage python
               12- iskeyword()                        : pour les mots résevés au langage python
"""

nom = "abdelmalek ben"

print(nom.strip())
print(nom.upper())
print(nom.lower())
print(nom.capitalize())
print(nom.title())
print(nom.center(15,"-"))
print(nom.find("malek")) 
try:
    print(nom.index("malek"))
except ValueError: 
    print("je n'ai pa trouvé la chaine")
print(nom.replace('a','2',2))
print(nom.split())

# exemple simple pour les sous-chaines à la place de str.index et str.find
if "ben" in nom:
    print("found")
else: 
    print("not found")

if "class".isidentifier(): 
    print("reservé")

str = "class"

if keyword.iskeyword(str):
    print("Mot réservé par Python")
