# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:10:27 2018

@author: etudiant
"""
import csv
import matplotlib.pyplot as plt

def importation():
	with open('donnees_projet', 'r') as f:  # import les donnees
		reader = csv.reader(f)
		your_list = list(reader)
	print(your_list)
	return your_list
#-----------------------------------transforme en float les valeurs max d'XP-------------------------------------------
#%%
def float_max_xp(your_list):
	l1 = []
	for mm in range(len(your_list[0])-1):
	    l1.append(float(your_list[0][mm]))
	return l1
#-----------------------------------donne le nombre de validant-----(tres sale)----------------------------------------
#%%
def nb_valid(your_list):
	nb_eleve = len(your_list)-1
	lastt = your_list[1:]
	nb_de_valide = 0
	for i in range(len(lastt)):
	    if lastt[i][4] == '1.0':
	        nb_de_valide +=1
	print('il y a ',nb_de_valide ,'etudiants qui ont valide')
	return nb_de_valide,lastt,nb_eleve
#-----------------------------------transforme la liste de str en liste de float---------------------------------------
#%%
def str_to_float(nb_de_valid,lastt):
	my_list = []
	
	for uu in range(len(lastt)):
	    uuu = 0
	    temp = []
	    for uuu in range(len(lastt[uu])):
	        temp.append(float(lastt[uu][uuu]))
	    my_list.append(temp)
	print(my_list)
	return my_list
#-------------------------------------------moyenne les xp sur 100-----------------------------------------------------
#%%
def moyenne_xp_sur_100(my_list,l1):
	jolist = []
	for pp in range(len(my_list)):
	    temp = []
	    for ppp in range(len(my_list[0])-1):
	        temp.append(my_list[pp][ppp] * (100/ l1[ppp]))
	    jolist.append(temp)
	print(jolist)
	return jolist
#------------------------------------------donne les listes de note en fonction des ue---------------------------------
#%%
def listage_ue_note(your_list,my_list):
	Ue1 = []
	Ue2 = []
	Ue3 = []
	Ue4 = []
	
	for PPPP in range(len(my_list)):
	    Ue1.append(my_list[PPPP][0])
	    Ue2.append(my_list[PPPP][1])
	    Ue3.append(my_list[PPPP][2])
	    Ue4.append(my_list[PPPP][3])
	return Ue1,Ue2,Ue3,Ue4
#------------------------------------------moyenne des liste de note de chaque ue--------------------------------------
#%%
def moyenne_list_note_ue(Ue1,Ue2,Ue3,Ue4):
	a =0
	b= 0
	c=0
	d=0
	
	for i in range(len(Ue1)):
	    a = a + Ue1[i]
	    b = b + Ue2[i]
	    c = c + Ue3[i]
	    d = d + Ue4[i]
	
	MoyUe1 = a / len(Ue1)
	MoyUe2 = b / len(Ue1)
	MoyUe3 = c / len(Ue1)
	MoyUe4 = d / len(Ue1)
	print(MoyUe1)
	print(MoyUe2)
	print(MoyUe3)
	print(MoyUe4)
	return MoyUe1,MoyUe2,MoyUe3,MoyUe4
#--------------------------------------XP Fonctio nb ex-------------------------------------------------------------
#%%
def Xp_jesaisplus(my_list,str_to_float,lastt):
	Moyenn = []
	for POP in range(len(lastt)):
	    a = my_list[POP][0]+my_list[POP][1]+my_list[POP][2]+my_list[POP][3]
	    Moyenn.append(a/4)
	n=0
	a=0
	while a<len(Moyenn)-1:           #ordonne la liste
	    a = 0
	    for n in range(len(Moyenn)-1):
	        if Moyenn[n] > Moyenn[n+1]:
	            p = Moyenn[n]
	            Moyenn[n] = Moyenn[n+1]
	            Moyenn[n+1] = p
	        else:
	            a =a+1
	print(Moyenn)
	plt.hist(Moyenn,100)
	return Moyenn