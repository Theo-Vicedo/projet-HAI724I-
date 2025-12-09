import os, sys, re
import matplotlib.pyplot as plt

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#                    FONCTION                     #
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def txt_en_dico(fd):
    '''
    le fd en paramètre est le fichier créé par le script intensite.py. 
    Il est nommé index.txt
    Cette fonction permet d'obtenir les informations de intensity.py sans avoir à faire appel à ce script ici.
    '''
    dico={}
    clef = []                                   # pour les clefs du dictionnaire
    valeur = []                                 # pour les valeurs du dictionnaire

    lignes = fd.readlines()                     # on prend toutes les lignes du fichier .txt
    for l in lignes:
            data = l.split(":")
            clef.append(data[0].strip())
            valeur.append(data[1].strip()) 
    # ici valeur est une liste de String

    ## CONVERSION DE valeur EN LISTE DE LISTES  
    res = []                                    # res est la conversion de valeur
    for s in valeur:                            # pour chaque String
        infos = []                              # initialisation au cas où le String est vide
        if len(s)>0:
            infos = s.split(',')                # on sépare les 4 valeurs
            infos = [float(x) for x in infos]
        res.append(infos)

    ## REMPLISSAGE DU DICTIONNAIRE
    for i in range(0,len(clef)):
       dico[clef[i]]=res[i]

    return dico



###~~~~~~~~~~~~~~~~~###
# Partie pour main.sh #
###~~~~~~~~~~~~~~~~~###

res=txt_en_dico(open("index.txt"))      # dictionnaire des informations de intensite.py
pas = float(sys.argv[1])                # en nm


###~~~~~~~~~~~~~~~~~~~~~###
# demande de l'intervalle #
###~~~~~~~~~~~~~~~~~~~~~###

'''
Ici choix d'un intervalle entier.
Un intervalle en float aurait pu être envisagé
'''

print("Entrez les entiers pour l'intervalle désirer :")
print("~~~")
while True:
    infe = int(input("valeur pour la borne inférieure : "))
    supe = int(input("valeur pour la borne supérieure : "))

    if supe<infe :    
        print("~~~")
        print("Erreur : il faut que la borne inférieure soit inférieure à la borne supérieure")
        continue                # continue permet ici de revenir au début de la boucle

    if supe==infe:
        print("~~~")
        print("Erreur : ce script ne prend pas d'intervalle vide")
        continue
    
    break                       # la boucle s'arrête dès que supe > infe



### Obtention de la liste des index demandés

## Le pas peut être décimal :
cpt=0
while not pas.is_integer():
    cpt+=1
    pas*=10

# liste des index par compréhension
index = [f"{round(float(i*10**(-cpt)),cpt)}-{round(i*10**(-cpt)+pas*10**(-cpt),cpt)}" for i in range(infe*10**cpt,supe*10**cpt,int(pas))]


###~~~~~~~~~~~~~~~~~###
# partie pour le plot #
###~~~~~~~~~~~~~~~~~###

x,y = [],[]                                     # liste des clefs que demande l'utilisateur et qui existent, liste des moyennes par intervalle
# x : abscisse, y : ordonnée

mini,maxi = [],[]                               # liste des valeurs minimales et maximales pour l'incertitude 

for i in index:
    if i in res.keys() and len(res[i])>0:       # cond 1 : au cas où on demande un index qui n'existe pas chez nous | cond 2 : au cas où il n'y a pas de valeur
        y.append(res[i][2])
        x.append(i)
        maxi.append(res[i][3])
        mini.append(res[i][1])

# liste des incertitudes : (max-min) / sqrt(2)
incert = [(maxi[i]-mini[i])/2**0.5 for i in range(len(mini))]


'''
Il est possible d'avoir énormément d'indices en abscisse, rendant le plot illisible.
les variables suivantes ainsi que plt.xticks() permettent de pallier ce problème
'''

nb = 100                                        # choix arbitraire du nombre d'indices en abscisse
position = range(len(x))
pasAbscisse = max(1,len(x)//nb)

###~~~~~~~~~~~~~~~###
#       PLOT        #
###~~~~~~~~~~~~~~~###

plt.figure(figsize=(14,10))

plt.plot(x,y,'b')                                               # plot normal sans incertitude
plt.errorbar(x,y,yerr=incert, fmt='o', capsize=3, ecolor='red') # pour avoir aussi les incertitudes

plt.title('moyenne des données par intervalle')
plt.xlabel('intervalles')
plt.ylabel('moyennes')

plt.xticks(position[::pasAbscisse],rotation=90)                 # pour mieux lire l'abscisse
plt.show()

