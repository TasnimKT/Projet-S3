# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:44:19 2018

@author: etudiant
"""
import csv
with open('donnees_projet', 'r') as f:  #import les donnees
    reader = csv.reader(f)
    your_list = list(reader)
	
def tensformation_de_liste(liste_de_base):
	liste_utilisable = []
	temp=[]
	#pour la 1er ligne (ou il n'y a pas que des floatant)
	for a in range(len(liste_de_base[0])-1):
		temp.append(float(liste_de_base[0][a]))
	temp.append(liste_de_base[0][-1])
	liste_utilisable.append(temp)
	#pour le reste
	liste_de_base = liste_de_base[1:]
	for i in range(len(liste_de_base)):
		temp = [] #vide la liste temporaire
		for o in range(len((liste_de_base[i]))):
			temp.append(float(liste_de_base[i][o]))
		liste_utilisable.append(temp)
	return liste_utilisable

def liste_validation_des_etudiant(liste_utilisable):
	i = 1		#on ignore la 1er ligne
	liste_validation = []
	for i in range(len(liste_utilisable)-1):
		liste_validation.append(liste_utilisable[i+1][-1])
	print(liste_validation)
	return liste_validation
liste_validation_des_etudiant(tensformation_de_liste(your_list))

def nb_eleve_valider(liste_validation):
	nb_valid=0
	d=1.0
	for d in liste_validation:
		if d == 1.0:
			nb_valid+=1
	return nb_valid
		