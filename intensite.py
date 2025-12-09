import os, sys, re

'''
entrées : fichier .txt de valeurs et taille de fenetre (float)

rendu : 
- affichage pour chaque intervalle des différentes informations demandées
- un fichier index.txt contenant pour chaque ligne les informations

Une suggestion pour aller plus loin : 
au lieu d'afficher pour chaque intervalle, voir pour n'afficher que celles comprises dans l'intervalle 
renseigné par l'utilisateur dans recherche_plot.py ?
'''


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#                    FONCTIONS                    #
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

### moyenne
def moyenne(liste): return sum(liste)/len(liste) # NB : certains modules la nomment mean


### I/ lecture du fichier & conversion en dictionnaire
def file_en_dico(fd,pas):
    '''
    On suppose le fichier trié par longueur d'onde croissante.
    Le pas peut être décimal. 
    '''

    ## LECTURE FICHIER
    lignes = fd.readlines()                         # on prend toutes les lignes du fichier .txt
    long_onde = []                                  # pour les clefs du dictionnaire
    intensite = []                                  # pour les valeurs du dictionnaire

    for l in lignes:             
        if l and (l[0] in ('123456789')) :          # vérifie si l est une ligne avec les valeurs voulues
            data = l.split("\t")
            long_onde.append(float(data[0].strip()))
            intensite.append(float(data[1].strip())) 

    ## INITIALISATION DU DICTIONNAIRE
    borne_inf=0.0                                   # borne inférieure des intervalles
    dico = {f"{borne_inf}-{borne_inf+pas}":[]}      # initialise le dictionnaire avec la clef "0-10" (valeur = liste vide)

    ## ARRONDIR CORRECTEMENT LE PAS
    cpt=0
    while not pas.is_integer():
        cpt+=1
        pas*=10
    # arrondir le pas permet de savoir combien de décimales prendre pour les clefs du dictionnaire

    ## REMPLISSAGE DU DICTIONNAIRE
    for i in range(0,len(long_onde)):
        while long_onde[i]>=borne_inf+pas*10**(-cpt):                                               # vérifie si la longueur d'onde est hors de la fenêtre référente
            borne_inf+=pas*10**(-cpt)                                                               # incrémente du pas
            dico[f"{round(borne_inf,cpt)}-{round(borne_inf+pas*10**(-cpt),cpt)}"]=[]                # création d'une nouvelle fenêtre (référente)
        dico[f"{round(borne_inf,cpt)}-{round(borne_inf+pas*10**(-cpt),cpt)}"].append(intensite[i])  # ajout à la fenêtre qui correspond
        
    ## TRI DES VALEURS
    for key in dico.keys():
        dico[key].sort()

    return dico


### II/ Informations sur chaque fenêtre d'intensité
def data_intensites(dico):
    ''' 
    dictionnaire res : 
    - clefs - mêmes clefs que le dictionnaire en entrée : les fenêtres d'intensité
    - valeurs - liste avec 4 informations sur les données :
        nombre de données
        valeur mininimale
        valeur moyenne
        valeur maximale
        --> len,min,mean,max
    NB : ici le choix d'une liste pour les stocker a été fait, mais un tuple aurait pu être envisagé.
    '''
    res={}

    for key in dico.keys():
        if dico[key]:                                                                # vérifie que la valeur du dictionnaire ne soit pas vide
            res[key]=[len(dico[key]),dico[key][0],moyenne(dico[key]),dico[key][-1]]  # chaque valeur de dico est ordonnée, donc a[0] et a[-1] = min et max
        else :
            res[key]=[]                                                              # liste vide si aucune donnée pour l'intensité

    return res


###~~~~~~~~~~~~~~~~~###
# Partie pour main.sh #
###~~~~~~~~~~~~~~~~~###

fd = open(sys.argv[1])                          # ouverture du fichier des données
pas = float(sys.argv[2])                        # le pas, en nm

a = file_en_dico(fd,pas)                        # le fichier converti en dictionnaire
dic_info = data_intensites(a)                   # dictionnaire des informations demandées pour intensite.py


###~~~~~~~~~~~~~~~~~~~~###
# affichage des fenêtres #
###~~~~~~~~~~~~~~~~~~~~###

for key in dic_info.keys():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Fenêtre ',key,'(nm) :')
    if len(dic_info[key])>0:
        print('nombre de données : ',dic_info[key][0])
        print('valeur min : ',dic_info[key][1])
        print('moyenne : ',round(dic_info[key][2],2)) # arrondi au centième près, choix arbitraire. Aurait pu se faire en fonction du nombre de décimales du pas
        print('valeur max : ',dic_info[key][3])
    else:
        print('Pas de valeur.')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# mise du dictionnaire dans un .txt #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# on crée le fichier et on met pour chaque ligne les informations du dictionnaire
# structure type d'une ligne : 
# clef:count,min,mean,max

with open("index.txt", "w") as f: 
    for fenetre, stats in dic_info.items():
        ligne = f"{fenetre}:{','.join(map(str, stats))}\n"
        f.write(ligne)
