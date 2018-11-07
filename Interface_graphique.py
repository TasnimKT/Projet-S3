# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:48:03 2018

@author: etudiant
"""

from tkinter import * 

# Construction de la fenêtre principale «root»
root = Tk()
root.title('Simple exemple')
# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=root.quit)

# Placement du bouton dans «root»
qb.pack()

# Lancement de la «boucle principale»
root.mainloop()
print("fin")