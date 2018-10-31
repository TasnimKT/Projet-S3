import csv
import matplotlib.pyplot as plt
with open('donnees_projet', 'r') as f:  #import les donnees
    reader = csv.reader(f)
    your_list = list(reader)
print(your_list)

#-----------------------------------transforme en float les valeurs max d'XP-------------------------------------------
l1 = []
for mm in range(len(your_list[0])-1):
    l1.append(float(your_list[0][mm]))

#-----------------------------------donne le nombre de validant-----(tres sale)----------------------------------------
nb_eleve = len(your_list)-1
lastt = your_list[1:]
nb_de_valide = 0
for i in range(len(lastt)):
    if lastt[i][4] == '1.0':
        nb_de_valide +=1
print('il y a ',nb_de_valide ,'etudiants qui ont valide')
#-----------------------------------transforme la liste de str en liste de float---------------------------------------
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
for pp in range(len(my_list)):
    temp = []
    for ppp in range(len(my_list[0])-1):
        temp.append(my_list[pp][ppp] * (100/ l1[ppp]))
    jolist.append(temp)
print(jolist)
#------------------------------------------donne les listes de note en fonction des ue---------------------------------
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
plt.hist(Moyenn,2)
#------------------------------------------test nom-----------------------------------------------------------------
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
#nom = str(input("qui tu cherche wesh ?"))
nom = "bite"
l = 0
a=0
while l < len(listwname):
     if nom == listwname[l][0]:
        print("il a eu :", listwname[l][1:])
        l = len(listwname)+2
     else:
        l += 1

if l == len(listwname):
    print("il n'existe pas")
#------------------------------------------------------------------------------------------------------------------