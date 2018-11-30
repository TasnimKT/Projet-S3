# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 09:48:03 2018

@author: etudiant
"""
import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
global nom
global entree
LARGE_FONT = ("Verdana",11)
MOINS_LARGE_FONTE = ("IMPACT", 15)

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
def xpmax():
	liste = tensformation_de_liste()
	maxEU1 = liste[0][0][0]
	maxEU2 = liste[0][0][1]
	maxEU3 = liste[0][0][2]
	maxEU4 = liste[0][0][3]
	return maxEU1 , maxEU2 , maxEU3 , maxEU4 
	
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
	list_nom = ["Aaron Alvarez","René Coty","Randy Burns","Diane Hernandez","Anna Nichols","Paul Cruz","Heather MacOwens","Thomas Powell","Debra Harris","George Webb","Kathryn Martinez","Roy Vasquez","Marilyn Herrera","Larry Robinson","Michael Rose","Nancy Martin","Juan Morales","Tammy Wilson","Robert Tran","Robin Romero","Brian Watson","Betty Harris","Katherine Arnold","Douglas Gray","Sean Roberts","Gerald Hill","Sean Watson","Gary Edwards","Susan Morales","Charles Bailey","Fred Romero","Alan White","Judith James","Stephanie Snyder","James Murray","Helen Wright","Donald Johnson","Julia Anderson","Larry Stone","Carol Evans","Sharon Wood","Roger Hunt","Bobby Payne","Howard Turner","Roger Holmes","Lawrence Alvarez","Nicholas Russell","Kathy Jackson","Richard Washington","Lawrence Dunn","Sara Kelley","Teresa Alexander","Stephanie Payne","Frances White","Joshua Butler","Angela King","Anna Woods","Arthur Hansen","Teresa Bryant","James Knight","Fred Rivera","Debra Simmons","Peter Hawkins","Lawrence Jones","Randy Reyes","Christine Kelley","Carl Martin","Bonnie Gordon","Victor Mills","James Thompson","Philip Moreno","Fred Hamilton","Clarence Nichols","Helen Rodriguez","Anna Patterson","Pamela Mitchell","Gary Myers","Patrick Daniels","Chris Martin","Julia Hunt","Frances Pierce","Clarence Thompson","Joseph Young","Albert Elliott","Nicholas Murray","Norma Mitchell","Maria Perry","Robin Wood","Donald Allen","Theresa Reyes","Frances Nguyen","Ann Spencer","Alan Webb","Sandra Fernandez","Paula Peterson","Roy Wright","Russell Castro","Harry Patterson","Melissa Ross","John Smith"]
	liste = tensformation_de_liste()[1]
	for i in range(len(liste)):
		liste[i].insert(0,list_nom[i])
	return liste,list_nom

def sous_liste():
	Eu1 = []
	Eu2 = []
	Eu3 = []
	Eu4 = []
	liste = tensformation_de_liste()[1]
	for i in range(len(liste)):
		Eu1.append(liste[i][0])
		Eu2.append(liste[i][1])
		Eu3.append(liste[i][2])
		Eu4.append(liste[i][3])
	return Eu1,Eu2,Eu3,Eu4
def moyenne(liste_de_note):
	moyenne = sum(liste_de_note)/len(liste_de_note)
	return moyenne

def prep_histo(liste,note):
	
	hist = plt.hist(liste,100)
	plt.axvline(x=note,color = 'red')
	return hist
	

def il_est_ou(nom):
	liste = anomation()[0]
	for i in range(len(liste)):
		if nom == liste[i][0]:
			note = liste[i][1:]
			pos = i
	return note,pos

def moiYenneaSion():
	new_liste =[]
	liste = tensformation_de_liste()[1]
	maxEU1,maxEU2,maxEU3,maxEU4 =xpmax()
	for i in range(len(liste)):
		temp=[]
		for u in range(len(liste[i])-1):
			temp.append(liste[i][u]/xpmax()[u]*100)
		new_liste.append(temp)
	return new_liste

def bestone():
	resulatas = []
	listesur100 = moiYenneaSion()
	for i in range(len(listesur100)):
		temp=[]
		for u in range(len(listesur100[i])):
			if u == listesur100[i].index(max(listesur100[i])):
				temp.insert(listesur100[i].index(max(listesur100[i])),1)
			else:
				temp.insert(u,0)
		resulatas.append(temp)
	return resulatas

def nbenfonctiondumax():
	liste_nb_de_max = [0,0,0,0]
	liste = bestone()
	for i in range(len(liste)):
		for u in range(len(liste[i])):
			a =liste_nb_de_max[u]+liste[i][u]
			liste_nb_de_max[u] = a
	return liste_nb_de_max
def position(pos):
	liste_moy = []
	liste=tensformation_de_liste()[1]
	for i in range(len(liste)):
		liste_moy.append(moyenne(liste[i][:-1]))
	liste_moy.sort()
	a = 0 
	place = 0
	for a in range(len(liste_moy)):
		if float(liste_moy[a]) == float(moyenne(liste[pos][:-1])):
			place =a
	return place 
	
def recherche():
	global entree
	liste = anomation()[1]
	global nom
	nom = entree.get()
	if nom in liste:
		novv = tk.Tk()
		novv.wm_title("Eleve"+nom)
		note = il_est_ou(nom)[0]
		pos = il_est_ou(nom)[1]
		#label = tk.Label(novv,text=nom, font=LARGE_FONT) # def ( init)
		#label.pack(pady=10,padx=10)
		d1 = tensformation_de_liste()[0][pos][0] 
		d2 = tensformation_de_liste()[0][pos][1] 
		d3 = tensformation_de_liste()[0][pos][2] 
		d4 = tensformation_de_liste()[0][pos][3] 
		moyA = moyenne(moiYenneaSion()[pos])
		moyA = str(moyA)
		txt = nom+" a eu au domaine 1 : "+str(d1)+" , au domaine 2 : \n"+str(d2)+ ", au domaine 3 : "+str(d3)+ " et au domaine 4 : "+str(d4)+"\n Et a eu une moyenne de : "+moyA+" (sur 100)\n Cette élève a la"+str(position(pos))+" eme meilleur note" 
		label = tk.Label(novv, text = txt,font=LARGE_FONT)
		label.pack()
		Fig, axe = plt.subplots(nrows=2,ncols=2,figsize=(7,7))
		axe[0,0].set_title("Eu1")
		axe[0,0].hist(sous_liste()[0],100)
		axe[0,0].set_xlabel("Xp")
		axe[0,0].set_ylabel("Nb de note")
		axe[0,0].axvline(note[0], color="red")
		
		axe[0,1].set_title("Eu2")
		axe[0,1].hist(sous_liste()[1],100)
		axe[0,1].set_xlabel("Xp")
		axe[0,1].set_ylabel("Nb de note")
		axe[0,1].axvline(note[1], color="red")
		
		axe[1,1].set_title("Eu3")
		axe[1,1].hist(sous_liste()[2],100)
		axe[1,1].set_xlabel("Xp")
		axe[1,1].set_ylabel("Nb de note")
		axe[1,1].axvline(note[2], color="red")
		
		axe[1,0].set_title("Eu4")
		axe[1,0].hist(sous_liste()[3],100)
		axe[1,0].set_xlabel("Xp")
		axe[1,0].set_ylabel("Nb de note")
		axe[1,0].axvline(note[3], color="red")
		
			
		canvas = FigureCanvasTkAgg(Fig, novv)
		canvas.draw()
		canvas.get_tk_widget().pack(side =tk.LEFT, expand = False)


		novv.mainloop()
	else:
		nop = tk.Tk()
		nop.wm_title("!!!!")
		labelErr = tk.Label(nop,text = "ERROR 404", font = MOINS_LARGE_FONTE)
		labelErr.pack(pady =20, padx = 25)
		print("erreur cet eleve n'exite pas")
			


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#-_-_-_-_-_-_-_-_-_-_-_-_Zone d'affichage fenetre-_-_-RIP_-_-_-_-_-_-_-_-_-_-_-
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
class Interface(tk.Tk):
	
	def __init__(self, *args, **kwargs):			#initialisation  (method)
		
		tk.Tk.__init__(self, *args, **kwargs)
		#tk.Tk.iconbitmap(self,default="icon.ico") #marche pas
		tk.Tk.wm_title(self,"Recherche des petios")
		root = tk.Frame(self)		
		root.pack()  
		root.grid_rowconfigure(0, weight=1)
		root.grid_columnconfigure(0, weight=1)		
		self.frames = {}			#crée le dictionaire		
		for F in (StartPage, PageUne, PageDE, PageTROI,KATRE,Etu):		#parse au traver des page		
			frame = F(root,self)			
			self.frames[F] = frame			
			frame.grid(row= 0, column=0, sticky = "nsew") #sicky => aligne sur les coté		
		self.show_frame(StartPage)
		
	def show_frame(self,Nom):			#merci a 
		
		frame = self.frames[Nom]
		frame.tkraise()				#met au 1er plan
		

		
	
class StartPage (tk.Frame):		#page de base(navigation)
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text="Bienvenue sur La Page d'acceuil !", font=MOINS_LARGE_FONTE) # def ( init)
		label.pack(pady=10,padx=10)      #cree la fenetre
		#bouton11 = ttk.Button(self, text="Note de la classe",command=lambda: controller.show_frame(PageUne))
		#bouton11.pack()
		#bouton12 = ttk.Button(self, text="Could be ussfull",command=lambda: controller.show_frame(PageDE))
		#bouton12.pack()
		bouton13 = ttk.Button(self, text="Répartition des notes max",command=lambda: controller.show_frame(PageTROI))
		bouton13.pack()
		bouton14 = ttk.Button(self, text="Recherche d'élève",command=lambda: controller.show_frame(KATRE))
		bouton14.pack()
		boutonQ = ttk.Button(self,text="Quiter", command=quit)
		boutonQ.pack(side = "bottom")
		
class PageUne(tk.Frame):	#affiche 2 graph
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text="Les notes des debiles", font=LARGE_FONT) # def ( init)
		label.pack(pady=10,padx=10)      #cree la fenetre
		bouton2 = ttk.Button(self, text="Back",command=lambda: controller.show_frame(StartPage))
		bouton2.pack(side =tk.BOTTOM)
		Fig = Figure(figsize = (5,5),dpi=100)
		subplot = Fig.add_subplot(111)
		subplot.plot([1,2,3,4,5,6,7,8],[5,8,9,6,3,2,1,4])
		canvas = FigureCanvasTkAgg(Fig, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side =tk.LEFT, expand = False)
		Fig2= Figure(figsize = (5,5),dpi=100)
		subplot = Fig2.add_subplot(111)
		subplot.plot([1,2,3,4,5,6,7,8],[5,2,2,6,7,8,9,4])
		canvas2 = FigureCanvasTkAgg(Fig2, self)
		canvas2.draw()
		canvas2.get_tk_widget().pack(side =tk.RIGHT, expand = False)

class PageDE(tk.Frame):# ussless
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text="ola", font=LARGE_FONT) # def ( init)
		label.pack(pady=10,padx=10)      #cree la fenetre
		bouton2 = ttk.Button(self, text="Back",command=lambda: controller.show_frame(StartPage))
		bouton2.pack()

class PageTROI(tk.Frame):		#fenetre du camenbert
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text="Répartition des notes max", font=LARGE_FONT) # def ( init)
		label.pack(pady=10,padx=10)      #cree la fenetre
		bouton31 = ttk.Button(self, text="retour",command=lambda: controller.show_frame(StartPage))
		bouton31.pack()
		labels = 'Ue1', 'Ue2', 'Ue3','Ue4'
		f,(yo) = plt.subplots()
		yo.pie(nbenfonctiondumax() , labels=labels ,autopct='%1.1f%%', shadow=True, startangle=90)
		yo.axis('equal')
		yo.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5),title="Pourcentage élèves ayant eu \nleur meilleure note  dans le domaine 1,\n le domaine 2, le domaine 3 et le domaine 4")
		canvas3 = FigureCanvasTkAgg(f, self)
		canvas3.draw()
		canvas3._tkcanvas.pack(side =tk.TOP, fill=tk.BOTH, expand = True)

class KATRE(tk.Frame):	#fenetre de rechecher
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		global entree
		label = tk.Label(self,text="Que recherche tu ?", font=LARGE_FONT) # def ( init)
		label.pack(pady=10,padx=10)      #cree la fenetre
		entree = tk.Entry(self, textvariable=str, width=30)
		entree.pack()
		boutonRecherche = ttk.Button(self, text="Rechercher",command=recherche)
		boutonRecherche.pack()
		bouton4 = ttk.Button(self, text="Retour",command=lambda: controller.show_frame(StartPage))
		bouton4.pack()
			
class Etu(tk.Frame):		#inutiliser
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text="je veux mourir... svp... nonn", font=LARGE_FONT) # def ( init)
		label.pack(pady=10,padx=10)      #cree la fenetre
		bouton31 = ttk.Button(self, text="Back",command=lambda: controller.show_frame(StartPage))
		bouton31.pack()
		Fig = Figure(figsize = (5,5),dpi=100)
		subplot = Fig.add_subplot(111)
		subplot.plot([1,2,3,4,5,6,7,8],[5,8,9,6,3,2,1,4])
		canvas = FigureCanvasTkAgg(Fig, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side =tk.TOP, fill=tk.BOTH, expand = True)
		canvas._tkcanvas.pack(side =tk.TOP, fill=tk.BOTH, expand = True)
		        				

app = Interface()		#Créé l'apli
app.geometry("900x920")	#set de la résolution
app.mainloop()			#mainloop...
