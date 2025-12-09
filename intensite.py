import os, sys, re

'''2 entrées : fichier de valeurs et taille de fenetre'''

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#                    FONCTIONS                    #
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

## moyenne :
def moy(liste): return sum(liste)/len(liste)
#NB : certains modules la nomment mean, donc ici c'est moy

###################################
## 1e partie : fichier into dico ##
###################################
def file_en_dico(fd,pas):
    '''
    ICI pas PEUT ETRE DECIMAL
    '''
    lignes = fd.readlines()                                                              # on prend toutes les lignes du fichier fd
    # NB : on suppose notre fichier trié par longueurs d'onde

    ## INIT
    long_onde = []                                                                       # pour les clefs du dico
    intensite = []                                                                       # pour les valeurs du dico
    for l in lignes:
        if l and (l[0] in ('123456789')) :                                               # check si l est une ligne avec les valeurs voulues
            data = l.split("\t")
            long_onde.append(float(data[0].strip()))
            intensite.append(float(data[1].strip())) 


    # le faire directement ds la boucle du haut

    ## LE DICO
    tps=0.0                                                                              # borne inf des intervalles
    dico = {f"{tps}-{tps+pas}":[]}                                                       # init le dico avec 1 clef : "0-10"


    # POUR ARRONDIR LE PAS CORRECTEMENT 
    cpt=0
    while not pas.is_integer():
        cpt+=1
        pas*=10

 ## REMPLISSAGE DU DICO AVEC CLEFS ET VALEURS
    for i in range(0,len(long_onde)):
        while long_onde[i]>=tps+pas*10**(-cpt):                                          # check si hors de la fenêtre
            tps+=pas*10**(-cpt)                                                          # incrémente du pas
            dico[f"{round(tps,cpt)}-{round(tps+pas*10**(-cpt),cpt)}"]=[]                 # création nouvelle fenêtre (référente)
        dico[f"{round(tps,cpt)}-{round(tps+pas*10**(-cpt),cpt)}"].append(intensite[i])   # ajout à la fenêtre qui correspond
    

    ## TRI DES VALEURS
    for key in dico.keys():
        dico[key].sort()

    return dico

####################################################
## 2e partie : infos sur les fenetres d'intensité ##
####################################################
def data_intensites(dico):
    ''' 
    DANS LE DICO res : 
    - clefs - mêmes que pour le premier dico
    - valeurs - liste avec 4 éléments :
        nb de données d'intensité
        val min de données d'intensité
        val moyen de données d'intensité
        val max de données d'intensité
        --> len,min,mean,max
    NB : on aurait pu en faire un tuple au lieu d'une liste pour gain de place
    '''
    res={}

    for key in dico.keys():
        a = dico[key]                                                                # pr aller plus vite dans écriture
        if a:                                                                        # check si a n'est pas vide
            res[key]=[len(a),a[0],moy(a),a[-1]]
            # ici a est ordonnée donc a[0] et a[-1] = min et max
        else :
            res[key]=[]                                                              # tuple vide si intervalle vide

    return res                                                                       # renvoie le dico demandé


###################
# EXEC POUR LE BASH
###################
fd = open(sys.argv[1])                          # fichier des données
pas = float(sys.argv[2])                        # pas, en nm

####
a = file_en_dico(fd,pas)                        # le fichier avec les données converti en dico
res = data_intensites(a)                        # données demandées pour intensite.py


#~~~~~~~~~~~~~~~~~~~~#
# print des fenêtres #
#~~~~~~~~~~~~~~~~~~~~#
## NB : 
for key in res.keys():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Fenêtre ',key,'(nm) :')
    if len(res[key])>0:
        print('nombre de données : ',res[key][0])
        print('valeur min : ',res[key][1])
        print('moyenne : ',res[key][2]) # modifier en fonction du pas pr le nb de décimales  ou %.2f
        print('valeur max : ',res[key][3])
    else:
        print('Pas de valeur.')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MISE DU DICTIONNAIRE DANS UN .TXT #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# on crée le fichier et on met pour chaque ligne les infos du dico
# structure type d'une ligne : clef:count,min,mean,max

with open("index.txt", "w") as f: 
    for fenetre, stats in res.items():
        # stats = [count, min, moyenne, max]
        ligne = f"{fenetre}:{','.join(map(str, stats))}\n"
        f.write(ligne)