# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:05:36 2018

@author: etudiant
"""
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana",12)



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
		
		for F in (StartPage, PageUne, PageDE, PageTROI,KATRE):		#parse au traver des page
		
			frame = F(root,self)   
			
			self.frames[F] = frame
			
			frame.grid(row= 0, column=0, sticky = "nsew") #sicky => aligne sur les coté
		
		self.show_frame(StartPage)
		
	def show_frame(self,cont):
		
		frame = self.frames[cont]
		frame.tkraise()				#met au 1er plan
		
def recherche():
	global entree
	nom = entree.get()
	print(nom)
	return "\n"
		

	
		
	
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
               				

app = Interface()
app.mainloop()
