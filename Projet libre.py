# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:44:33 2018

@author: etudiant
"""

import csv   #Bibliothèque pour pouvoir lire notre fichier
import numpy as np   #Importer la bibliothèque numpy

with open('donnees_projet', 'r') as f:
    reader = csv.reader(f)    #Permet de lire la liste
    your_list = list(reader)    #Cette liste s'appelle maintenant 
    
#print(your_list[0])             #Affiche la liste

#print(len(your_list)-1)      #Nombre d'étudiants concernés (la ligne 0 défini les valeurs et donc ne correspond pas à un étudiant)


T = np.rot90(np.array(your_list))[0]  #Fais passer la dernière colonne en première ligne et affiche uniquement la ligne 0
T = np.delete(T,0,0)                   #suprime l'élément 0
#print(T)

validé = 0                          #Initialisation des variables
PasValidé = 0
for i in T:                          #i parcours la liste T
    if float(i) == 1.0 :             #Dans le tableau, les valeurs sont sous forme de chaines de carctères donc i est sous forme de chaîne de caracère. Pour le comparer à 1.0 qui est un décimal, il faut le transformer avec un décimal en float.
        validé += 1
        
    else :
        PasValidé += 1
        
#print(validé)                  #Nbr de personnes qui ont validés
#print(PasValidé)

#On va maintenant éssayer de connaître la position des étudiants qui ont validés dans cette liste de donnée. 0 = étudiant 1.


position_étudiants_validés = []

for n in range(len(T)):

    if float(T[n]) == 1.0:
        position_étudiants_validés.append(n)

print(position_étudiants_validés)    
    









        
    