# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:05:36 2018

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
LARGE_FONT = ("Verdana",12)

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
	
	plt.hist(liste,100)
	plt.axvline(x=note,color = 'red')
	plt.show()
	

def il_est_ou(nom):
	liste = anomation()[0]
	for i in range(len(liste)):
		if nom == liste[i][0]:
			note = liste[i][1:]
			pos = i
	return note,pos




def recherche():
	global entree
	liste = anomation()[1]
	global nom
	nom = entree.get()
	if nom in liste:
		novv = tk.Tk()
		novv.wm_title("Eleve"+nom)
		
		label = tk.Label(novv,text=nom, font=LARGE_FONT) # def ( init)
		
		label.pack(pady=10,padx=10)
		note = il_est_ou(nom)[0]
		pos = il_est_ou(nom)[1]
		
		Fig = prep_histo(liste,note)

		subplot = Fig.add_subplot(111)
		
		
				
		canvas = FigureCanvasTkAgg(Fig,novv)
		canvas.draw()
		canvas.get_tk_widget().pack(side =tk.TOP, fill=tk.BOTH, expand = True)
		novv.mainloop()
	else:
		print("ereur cet eleve n'exite pas")
			
	


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#-_-_-_-_-_-_-_-_-_-_-_-_Zone d'affichage fenetre-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
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
		
	def show_frame(self,cont):
		
		frame = self.frames[cont]
		frame.tkraise()				#met au 1er plan
		

		
	
class StartPage (tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self,text="Star PAGEEE", font=LARGE_FONT) # def ( init)
		
		label.pack(pady=10,padx=10)      #cree la fenetre
		
		bouton1 = ttk.Button(self, text="page 1",
					   command=lambda: controller.show_frame(PageUne))
		bouton1.pack()
		bouton122 = ttk.Button(self, text="page 2",
					   command=lambda: controller.show_frame(PageDE))
		bouton122.pack()
		bouton12z2 = ttk.Button(self, text="page 3 graph",
					   command=lambda: controller.show_frame(PageTROI))
		bouton12z2.pack()
		bouton12z2 = ttk.Button(self, text="Recherche",
					   command=lambda: controller.show_frame(KATRE))
		bouton12z2.pack()

		boutonQ = ttk.Button(self,text="Quiter")
		boutonQ.pack(side = "bottom")
		
class PageUne(tk.Frame):
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self,text="page2", font=LARGE_FONT) # def ( init)
		
		label.pack(pady=10,padx=10)      #cree la fenetre
		
		bouton2 = ttk.Button(self, text="Back",
					   command=lambda: controller.show_frame(StartPage))
		bouton2.pack()


class PageDE(tk.Frame):
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self,text="page23EZZ", font=LARGE_FONT) # def ( init)
		
		label.pack(pady=10,padx=10)      #cree la fenetre
		
		bouton3 = ttk.Button(self, text="Back",
					   command=lambda: controller.show_frame(StartPage))
		bouton3.pack()

class PageTROI(tk.Frame):
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self,text="Grap ;)", font=LARGE_FONT) # def ( init)
		
		label.pack(pady=10,padx=10)      #cree la fenetre
		
		bouton31 = ttk.Button(self, text="Back",
					   command=lambda: controller.show_frame(StartPage))
		bouton31.pack()
		
		Fig = Figure(figsize = (5,5),dpi=100)
		subplot = Fig.add_subplot(111)
		subplot.plot([1,2,3,4,5,6,7,8],[5,8,9,6,3,2,1,4])
		
		canvas = FigureCanvasTkAgg(Fig, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side =tk.TOP, fill=tk.BOTH, expand = True)
		
		
		canvas._tkcanvas.pack(side =tk.TOP, fill=tk.BOTH, expand = True)

class KATRE(tk.Frame):
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		global entree
		entree = tk.Entry(self, textvariable=str, width=30)
		entree.pack()
		
		
		label = tk.Label(self,text="Que recherche tu ?", font=LARGE_FONT) # def ( init)
		

		label.pack(pady=10,padx=10)      #cree la fenetre
		boutonRecherche = ttk.Button(self, text="Rechercher",command=recherche)
		boutonRecherche.pack()
		bouton41 = ttk.Button(self, text="Back",
					   command=lambda: controller.show_frame(StartPage))
		bouton41.pack()
		
		

		
class Etu(tk.Frame):
	def __init__(self, parent, controller):
				
		tk.Frame.__init__(self, parent)
				
		label = tk.Label(self,text="je veux mourir... svp... nonn", font=LARGE_FONT) # def ( init)
				
		label.pack(pady=10,padx=10)      #cree la fenetre
				
		bouton31 = ttk.Button(self, text="Back",
						   command=lambda: controller.show_frame(StartPage))
		bouton31.pack()
				
		Fig = Figure(figsize = (5,5),dpi=100)
		subplot = Fig.add_subplot(111)
		subplot.plot([1,2,3,4,5,6,7,8],[5,8,9,6,3,2,1,4])
				
		canvas = FigureCanvasTkAgg(Fig, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side =tk.TOP, fill=tk.BOTH, expand = True)
				
				
		canvas._tkcanvas.pack(side =tk.TOP, fill=tk.BOTH, expand = True)
		        				

app = Interface()
app.mainloop()
