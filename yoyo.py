import csv
import matplotlib.pyplot as plt
import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

with open('donnees_projet', 'r') as f:  #import les donnees
    reader = csv.reader(f)
    your_list = list(reader)
print(your_list)

#-----------------------------------transforme en float les valeurs max d'XP-------------------------------------------
#%%
l1 = []
for mm in range(len(your_list[0])-1):
    l1.append(float(your_list[0][mm]))

#-----------------------------------donne le nombre de validant-----(tres sale)----------------------------------------
#%%
nb_eleve = len(your_list)-1
lastt = your_list[1:]
nb_de_valide = 0
for i in range(len(lastt)):
    if lastt[i][4] == '1.0':
        nb_de_valide +=1
print('il y a ',nb_de_valide ,'etudiants qui ont valide')
#-----------------------------------transforme la liste de str en liste de float---------------------------------------
#%%
jolist = []
my_list = []

for uu in range(len(lastt)):
    uuu = 0
    temp = []
    for uuu in range(len(lastt[uu])):
        temp.append(float(lastt[uu][uuu]))
    my_list.append(temp)
print(my_list)
#-------------------------------------------moyenne les xp sur 100-----------------------------------------------------
#%%
for pp in range(len(my_list)):
    temp = []
    for ppp in range(len(my_list[0])-1):
        temp.append(my_list[pp][ppp] * (100/ l1[ppp]))
    jolist.append(temp)
print(jolist)
#------------------------------------------donne les listes de note en fonction des ue---------------------------------
#%%
Ue1 = []
Ue2 = []
Ue3 = []
Ue4 = []

for PPPP in range(len(my_list)):
    Ue1.append(my_list[PPPP][0])
    Ue2.append(my_list[PPPP][1])
    Ue3.append(my_list[PPPP][2])
    Ue4.append(my_list[PPPP][3])
#------------------------------------------moyenne des liste de note de chaque ue--------------------------------------
#%%
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
#--------------------------------------XP Fonctio nb ex-------------------------------------------------------------
#%%

xP = []
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
azerrrr = plt.hist(Moyenn,100)
#------------------------------------------test nom-----------------------------------------------------------------
#%%
#liste de nom de longeur 99
list_nom = ("a1","z1","e1","r1","t1","y1","u1","i1","o1","a2","z2","e2","r2","t2","y2","u2","i2","o2","a3","z3","e3","r3","t3","y3","u3","i3","o3","a4","z4","e4","r4","t4","y4","u4","i4","o4","a5","z5","e5","r5","t5","y5","u5","i5","o5","a6","z6","e6","r6","t6","y6","u6","i6","o6","a7","z7","e7","r7","t7","y7","u7","i7","o7","a8","z8","e8","r8","t8","y8","u8","i8","o8","a9","z9","e9","r9","t9","y9","u9","i9","o9","a0","z0","e0","r0","t0","y0","u0","i0","o0","a","z","e","r","t","y","u","i","o")
print(len(list_nom))
n = 0
ok = []
listwname = my_list
for n in range(len(my_list)-1):
    listwname[n].insert(0,list_nom[n])
print(listwname)
#----------------------------------------demande de nom-----------------------------------------------------------
#%%
def recherche_dans_list (nom):
	
	l = 0
	while l < len(listwname):
		if nom == listwname[l][0]:
			 note_de_leleve = listwname[l][1:]
			 print("il a eu :", listwname[l][1:])
			 l = len(listwname)+2     #2 ou plus, blc, c'est pour sortir de la boucle
			 return note_de_leleve
		else:
			 l += 1
		if l == len(listwname):
			 print("il n'existe pas")
			 Pas_de_note = True
			 return Pas_de_note
#--------------------------------INterface(test)-----------------------------------------------------------------
#%%
global azzz
global txt
azzz = 0
#fonction utile....
def recherche ():
	global txt
	global azzz
	azzz = azzz +30
	entre = entree.get()
	print(entre)
	app = recherche_dans_list(entre)
	print(app)
	if app == True:
		repo = str(entre+" n existe pas")
		txt = display.create_text(175,  azzz, text= repo, font="Arial 16", fill="black")
	else:
		note = str(app)
		app = entre + " a eu " + note
		txt = display.create_text(175, azzz, text=app, font="Arial 16", fill="black")

def ecriree():
	global txt
	ola =entree.get()
	txt = display.create_text(175, 60, text=ola, font="Arial 20", fill="black")
	return


#lol


	
	

	
root = tk.Tk()						#création de la fennetre sous une variable
root.title('Recherche de note :3')		#donne un nom a la fenetre
#crée une zone d'affichage
display = tk.Canvas(root, width=700, height=400, background='white')
#zone de txt
entree = tk.Entry(root, textvariable=str, width=30)
#txt = display.create_text(175, 60 +azzz, text="coucou", font="Arial 16", fill="black")	
#Mes boutons (Ils appeellent des fonctions avec command="le nom de la fonction")
BT_recherche = tk.Button(root, text='Chercher', command=recherche)
ecc = tk.Button(root, text='ecrir', command=ecriree)
ezc = tk.Button(root, text='eclrir', command=__init__)
ezc.pack()

BT_recherche.pack()
ecc.pack()
entree.pack()
display.pack()

def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(azerrrr, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


root.mainloop()

	