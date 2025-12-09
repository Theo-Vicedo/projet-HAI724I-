clear


# Type de fichier demandé : fichier.txt contenant les données sous forme :
# intensité   longueur d'onde'





## aussi verif la véracité des données demandées






# vérification du nombre d'indices
if [ $# -lt 1 ]; then
    echo "Erreur de format de ligne de commande."
    echo "Format demandé : $0 fichier_spectre.txt taille_fenetre"
    exit 1
fi

FICHIER=$1          # variable pour le fichier
TAILLE=${2:-10}     # variable pour la taille de la fenêtre, 10 par défaut si non fourni

# Vérification que le fichier est trouvé
if [ ! -f "$FICHIER" ]; then
    echo "Erreur : fichier '$FICHIER' introuvable."
    exit 1
fi



echo "#############################################################"
echo "Indexation des intensités avec une fenêtre de $TAILLE nm :"
python3 intensite.py "$FICHIER" "$TAILLE"
echo "    "


echo "#############################################################"
echo "Affichage graphique :"
python3 recherche_plot.py "$TAILLE"




## readme de github : dire que le f index.txt est donné par intensite et que recherche plot l'use
## + expliquer pourquoi utiliser une liste ou un dico
# + en gros des infos sur :

# requirements / module to install
# usage / command line (en gros moi : ./main.sh Spectre_photoluminescence.txt 1)
# input data / arguments / parametres
# output / files / plots / stats...
# licence (CC)
# authors noms/<email>
