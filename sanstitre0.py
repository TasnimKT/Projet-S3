# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:28:25 2018

@author: etudiant
"""

z = [1,2,3,4,2,8,2]
f = 2
def el_compteur(a,b):
	u=0
	for i in range(len(a)):
		if b == a[i]:
			u=u+1
	return u 
txt = str(el_compteur(z,f))
print("Le nombre apparaît " + txt + " fois")