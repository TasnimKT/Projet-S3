# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:16:14 2018

@author: etudiant
"""



## A AJOUTER DANS FONCTION RECHERCHER
##AFFICHER LES NOTES DANS CHAQUE DOMAINE DE LA PERSONNE RECHERCHE
        d1 = liste_utilisablev2[pos][0]
        d2 = liste_utilisablev2[pos][1]
        d3 = liste_utilisablev2[pos][2]
        d4 = liste_utilisablev2[pos][3]
       
        txt = nom+"a eu domaine1 ="+str(d1)+", domaine 2= "+str(d2)+ "domaine3 = "+str(d3)+ "et domaine 4 = "+str(d4)
       
        label = tk.Label(novv, text = txt,font=LARGE_FONT)
        
## AFFICHER LA MOYENNE DE L ELEVE 

        a = moyenne(liste_utilisablev2(pos))
        txta = nom+ "a eu une moyenne de" + str(a)
        label = tk.Label(novv, texta = txt,font=LARGE_FONT)
        label.pack()         

