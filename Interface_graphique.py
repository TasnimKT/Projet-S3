# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:48:03 2018

@author: etudiant
"""

#from tkinter import * 
import tkinter as tk
def verif():
	
	print(entree.get())
	return "l"
def recherche ():
	txt = canvas.create_text(75, 60, text='yo', font="Arial 16", fill="black")
	entre = entree.get()
	if entre =='lol':
		app = "cool"
		print("cool")
	else:
		app = "nul"
		print('nul')
	txt = canvas.create_text(75, 60, text=app, font="Arial 16", fill="black")

	return "lol"
def dell(canvas):
	
	canvas.destroy()
	canvas = tk.Canvas(root, width=500, height=300, background='white')
	#txt = canvas.create_text(75, 60, text="coucou", font="Arial 16 italic", fill="blue")
	
	entree = tk.Entry(root, textvariable=str, width=30)
	entree.pack()
	canvas.pack()

	return "rip"
def ecriree():
	ola =entree.get()
	txt = canvas.create_text(175, 60, text=ola, font="Arial 20", fill="black")
	return
	
# Construction de la fenêtre principale «root»
root = tk.Tk()
root.title('Simple exemple')

# Construction d'un simple bouton
qb = tk.Button(root, text='Chercher', command=recherche)
ecc = tk.Button(root, text='ecrir', command=ecriree)
clear = tk.Button(root, text='clear', command=dell)


canvas = tk.Canvas(root, width=500, height=300, background='white')
#txt = canvas.create_text(75, 60, text="coucou", font="Arial 16 italic", fill="blue")

entree = tk.Entry(root, textvariable=str, width=30)
entree.pack()
canvas.pack()
ecc.pack()


qb.pack()
clear.pack()


root.mainloop()
print("fin")