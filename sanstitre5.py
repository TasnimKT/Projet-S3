# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:44:19 2018

@author: etudiant
"""
import csv
def importation():
	with open('donnees_projet', 'r') as f:  #import les donnees
	    reader = csv.reader(f)
	    your_list = list(reader)
	return your_list


def tensformation_de_liste():	#prend la liste de base en arg
	liste_de_base = importation()
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
	liste_utilisablev2 = liste_utilisable[1:]
	return liste_utilisable,liste_utilisablev2

def liste_validation_des_etudiant():	#prend la liste en float en arg
	liste_utilisable = tensformation_de_liste()
	i = 1		#on ignore la 1er ligne
	liste_validation = []
	for i in range(len(liste_utilisable)-1):
		liste_validation.append(liste_utilisable[i+1][-1])
	return liste_validation


def nb_eleve_valider(): # prend la liste de validation (1 ou 0) ene arg
	liste_validation = liste_validation_des_etudiant() 
	nb_valid=0
	d=1.0
	for d in liste_validation:
		if d == 1.0:
			nb_valid+=1
	return nb_valid

def anomation():
	list_nom = ["Aaron Alvarez","Patricia Sanchez","Randy Burns","Diane Hernandez","Anna Nichols","Paul Cruz","Heather MacOwens","Thomas Powell","Debra Harris","George Webb","Kathryn Martinez","Roy Vasquez","Marilyn Herrera","Larry Robinson","Michael Rose","Nancy Martin","Juan Morales","Tammy Wilson","Robert Tran","Robin Romero","Brian Watson","Betty Harris","Katherine Arnold","Douglas Gray","Sean Roberts","Gerald Hill","Sean Watson","Gary Edwards","Susan Morales","Charles Bailey","Fred Romero","Alan White","Judith James","Stephanie Snyder","James Murray","Helen Wright","Donald Johnson","Julia Anderson","Larry Stone","Carol Evans","Sharon Wood","Roger Hunt","Bobby Payne","Howard Turner","Roger Holmes","Lawrence Alvarez","Nicholas Russell","Kathy Jackson","Richard Washington","Lawrence Dunn","Sara Kelley","Teresa Alexander","Stephanie Payne","Frances White","Joshua Butler","Angela King","Anna Woods","Arthur Hansen","Teresa Bryant","James Knight","Fred Rivera","Debra Simmons","Peter Hawkins","Lawrence Jones","Randy Reyes","Christine Kelley","Carl Martin","Bonnie Gordon","Victor Mills","James Thompson","Philip Moreno","Fred Hamilton","Clarence Nichols","Helen Rodriguez","Anna Patterson","Pamela Mitchell","Gary Myers","Patrick Daniels","Chris Martin","Julia Hunt","Frances Pierce","Clarence Thompson","Joseph Young","Albert Elliott","Nicholas Murray","Norma Mitchell","Maria Perry","Robin Wood","Donald Allen","Theresa Reyes","Frances Nguyen","Ann Spencer","Alan Webb","Sandra Fernandez","Paula Peterson","Roy Wright","Russell Castro","Harry Patterson","Melissa Ross","John Smith"]
	liste = tensformation_de_liste()[1]
	for i in range(len(liste)):
		liste[i].insert(0,list_nom[i])
	return liste

def recherche():
	liste = anomation()
	



