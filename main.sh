clear



## aussi verif la véracité des données demandées
## ds l'idée on fait un help pr le main.sh qui explique comment on utilise le truc

# ds l'idée on verif pr le fichier : mais je crois que c'est dejà fait





# Vérifier qu'on a bien un fichier en argument
if [ $# -lt 1 ]; then
    echo "Usage: $0 <fichier_spectre> [taille_fenetre]"
    exit 1
fi

FICHIER=$1
TAILLE=${2:-10}  # par défaut 10 si non fourni

# Vérifier que le fichier existe
if [ ! -f "$FICHIER" ]; then
    echo "Erreur : fichier '$FICHIER' introuvable."
    exit 1
fi




### ICI on peut voir pr peaufiner intensite.py :
### il pourrait rendre que les infos de l'intervalle voulu. DCP on ferait la demande des borns inf et sup ICI au lieu de dans recherche_plot.py 

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
