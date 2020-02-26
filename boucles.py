#coding: utf-8
#python boucles.py

"""
les boucles: WHLIE / FOR
               <initialiser compteur>
            1- while condition
                <instructions>
                <compteur>+1
            2- for

Mots clés  : BREAK / CONTINUE
fonctions prédéfininies: 1- range():returns a sequence of numbers, starting from 0 by default, 
                                  and increments by 1 (by default), and ends at a specified number.
"""
i=1
n = int(input("donner le nombre n:"))

print("LA BOUCLE TANT QUE")
while i <= n:
    print("you came to me")
    i=i+1
"""
print("LA BOUCLE FOR")

for x in range(4):
    print(x)
"""