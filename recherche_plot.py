import os, sys, re
import matplotlib.pyplot as plt

# import intensite as c

'''

python3 recherche_plot.py "/home/e20220006398/Bureau/m1/systemes/projet/Spectre_photoluminescence.txt"




BUT : 
lister les intensités pour un intervalle de longueur d'onde donnée demandée 
par l'utilisateur (fonction input) en utilisant l'index et

afficher graphiquement les intensités en fonction des longueurs d'onde 
pour l'intervalle demandé


?
NB : LE PLOT... PEUT ETRE EN BOXPLOT CAR:
ça affiche mean,min,max,length
?

exemple : 
on donne 300-400
####### NB : pb si demande 305-335 par exemple : demander si faut adapter
# alternative : si l'intervalle donné est pas bon : 
 # on le redemande

'''


# intervalle = input("donnez l'intervalle souhaité (format : inf-sup. ex : 100-210)")
### pour empecher les 165-654 :




## on check si les deux sont multiples du pas
## si oui on peut fragmenter l'intervalle en 

# if infe%pas==0 and supe%pas==0 and supe>infe :
#     frag = [i for i in range(infe,supe,pas)]
''' 
rendu :
borne inf30
borne sup150
[30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
'''

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#                    FONCTIONS                    #
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def txt_en_dico(txt):
    '''
    le txt en paramètre est le fichier créé par le script intensite.py.
    Il est normalemement nommé index.txt
    Cette fonction permet d'obtenir les informations de intensity.py sans avoir à faire appel à ce script ici.
    '''
    dico={}
    clef = []                                   # pour les clefs du dico
    valeur = []                                 # pour les valeurs du dico

    lignes = txt.readlines()                    # on prend toutes les lignes du fichier txt
    for l in lignes:
            data = l.split(":")
            clef.append(data[0].strip())
            valeur.append(data[1].strip()) 
    # ici valeur est une liste de String

    ## CONVERSION EN LISTE DE LISTES  
    res = []
    for s in valeur:                            # pr chaque string
        if len(s)>0:                            # si le string est pas vide
            numbers = s.split(',')              # on split les 4 val
            numbers = [float(x) for x in numbers]
            res.append(numbers)
        else:                                   # si vide on ajoute liste vide
            res.append([])

    ## REMPLISSAGE DU DICO AVEC CLEFS ET VALEURS
    for i in range(0,len(clef)):
       dico[clef[i]]=res[i]                     # ajout à la fenêtre qui correspond

    return dico


# dictionnaire des informations de intensite.py
res=txt_en_dico(open("index.txt"))

pas = float(sys.argv[1])                        # en nm



######################################################
######################################################
### FAUT FAIRE DAVANTAGE DE CHECK pr etre sur que user donne de bons trucs
######################################################
######################################################

print("Choissisez l'intervalle que vous voulez observer :")
print("~~~")
infe = int(input("borne inf : "))
supe = int(input("borne sup : "))
while supe<infe : #<=
    print("~~~")
    print("erreur : il faut que la borne inf soit inf à la borne sup")
    infe = int(input("borne inf : "))
    supe = int(input("borne sup : "))




####
## LE PAS PEUT ETRE DECIMAL, DONC :
####

cpt=0
while not pas.is_integer():
    cpt+=1
    pas*=10

# Obtenir la liste des index demandés
index = [f"{round(float(i*10**(-cpt)),cpt)}-{round(i*10**(-cpt)+pas*10**(-cpt),cpt)}" for i in range(infe*10**cpt,supe*10**cpt,int(pas))]







x,y = [],[]                                     # liste des clefs qui correspondent à ce que demande l'user et qui existent, liste des moyennes par intervalle

mini,maxi = [],[]                               # mini et maxi sont là pour l'incertitude 

for i in index:
    # nb : peut être fait en une cond : if ... and ... :
    if i in res.keys():                         # au cas où on demande un index qui n'existe pas chez nous
        if len(res[i]) > 0:                     # garder seulement si il y a au moins une valeur
            y.append(res[i][2])
            x.append(i)

            maxi.append(res[i][3])
            mini.append(res[i][1])


# liste des incertitudes : (max-min) / sqrt(2)
incert = [(maxi[i]-mini[i])/2**0.5 for i in range(len(mini))]


#####################
#       PLOT        #
#####################
plt.figure(figsize=(14,10))

plt.plot(x,y,'b')                        # plot normal sans incertitude

# pour avoir aussi les incertitudes : 
plt.errorbar(x,y,yerr=incert, fmt='o', capsize=5, ecolor='red')

plt.title('moyenne des données par intervalle')
plt.xlabel('intervalles')
plt.ylabel('moyennes')
plt.xticks(rotation=90)                         # pour mieux lire l'abscisse
plt.show()












#######################################################################################################################################
#####################################################     ANCIEN CODE     #############################################################
#######################################################################################################################################


# fd = open(sys.argv[1])                          # fichier des données

# pas = 10                                        # en nm |||| pas par défaut
# if len(sys.argv)>=3 :                           # si taille précisée, on remplace
#     pas = float(sys.argv[2])


# ####

# a = c.file_en_dico(fd,pas)                      # le fichier en dico
# res = c.data_intensites(a)                      # données demandées pour intensite.py

###






'''




#ici on plot TT les boxplot au meme endroit...
# plt.figure() 
# for key in res.keys():
#     plt.boxplot(res[key])
# plt.show()


keys = index
values = []
for i in keys:
    if i not in res.keys(): # au cas où on demande un index qui n'existe pas chez nous
        break
    # print(i,len(res[i]))
    if len(res[i]) > 0:         # garder seulement si il y a au moins une valeur
        values.append(res[i][2])


# plt.figure(figsize=(14,6))
# plt.boxplot(values, labels=keys)
# plt.xticks(rotation=90)   # pour voir les labels
# plt.show()

# print(keys)
'''











