clear


# Type de fichier demandé : fichier.txt contenant les données sous forme :
# intensité \t longueur d'onde





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#   VERIFICATION DES ENTREES   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# vérification du nombre d'indices
if [ $# -lt 1 ]; then                           # vérifie le nombre d'arguments donnés
    echo "Erreur de format."
    echo "Format demandé : $0 fichier_spectre.txt taille_fenêtre"
    exit 1                                      # pour arrêter le script à cause d'une erreur
fi


FICHIER=$1                                      # variable pour le fichier

# vérification que le fichier est trouvé
if [ ! -f "$FICHIER" ]; then                    # vérifie que l'argument donné est un fichier qui existe
    echo "Erreur : fichier '$FICHIER' introuvable."
    exit 1
fi


TAILLE=${2:-10}                                 # variable pour la taille de la fenêtre, 10 par défaut si non fourni
# si un second indice est fourni, alors taille n'est pas forcément un nombre.

# vérifie que TAILLE est un nombre positif
if ! [[ "$TAILLE" =~ ^([0-9]+([.][0-9]+)?|[.][0-9]+)$ ]]; then
    echo "Erreur : taille_fenetre doit être un nombre (ex: 10, 2.5, 0.25)."
    exit 1
fi





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#   EXECUTION DES DEUX SCRIPTS PYTHON   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# 1er script : intensité
echo "#############################################################"
echo "Indexation des intensités avec une fenêtre de $TAILLE nm :"
python3 intensite.py "$FICHIER" "$TAILLE"   # rappel : il crée un .txt contenu les informations pour chaque intervalle

echo "    "     

#2ème script : recherche_plot
echo "#############################################################"
echo "Affichage graphique :"
python3 recherche_plot.py "$TAILLE"         # rappel : utilise le .txt du premier script pour tracer le graphique.