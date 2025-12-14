# projet-HAI724I-
Dépôt GitHub pour les scripts demandés dans le cadre d'un projet de physique au sein de l'UE HAI724I (M1-S7).
L'objectif était de traiter les données d'un fichier .txt afin de les exploiter.


## Les trois scripts

- `intensite.py`  
  Ce script lit le fichier contenant les informations et regroupe les intensités par fenêtres de longueurs d’onde.
  Il exploite ensuite les données afin d'en obtenir des informations pour les stocker dans un fichier nommé **`index.txt`**.

- `recherche_plot.py`  
  Ce script utilise le fichier **`index.txt`** généré par `intensite.py`. Il recherche les données pour l'intervalle souhaité par l'utilisateur afin de créer un graphique correspondant ayant les intervalles en abscisse et les moyennes d'intensité en ordonnée.
  
- `main.sh`  
  Script principal qui fait quelques vérifications quant à la validité des paramètres d'entrée. Il exécute par la suite les deux codes .py.

---

## Modules

Chacun des deux codes Python importe les modules cités par l'énoncé du projet **`projet_physique.py`**.
Les modules autorisés sont : 
- `os`
- `sys`
- `re`
- `matplotlib`

---

## Usage

L’exécution du projet se fait via le script bash principal.
Afin de le lancer, voici un exemple de ligne de commande permettant de le lancer : 

```bash
./main.sh Spectre_photoluminescence.txt 1
```

Ici, **`Spectre_photoluminescence.txt`** est le fichier contenant les données et **1** est le pas souhaité, qui détermine la taille de l'intervalle.

## Arguments

Le script principal n'accepte qu'un ou deux arguments en entrée. Le premier doit correspondre au fichier, et le second -facultatif- correspond au pas souhaité.
- Le fichier doit être un txt, et contenir les données dans le format souhaité : longueur_donde \t intensite
- Le pas doit être un nombre positif. Le pas est en nanomètre (nm).
  S'il n'y a aucune entrée pour le pas, il aura 10 nm par défaut.

NB : un pas trop faible requiert d'avoir suffisamment de données pour obtenir des résultats utilisables. 

## Résultats

Le premier script python **`intensite.py`** affiche dans le terminal les informations demandées par l'énoncé. Il s'agit de renvoyer pour chaque intervalle : le nombre de données, l'intensité minimale, l'intensité moyenne, l'intensité maximale.
Les informations obtenues sont stockées dans un dictionnaire ayant les intervalles en clefs et des listes de 4 éléments pour objets. 

NB : Pour un gain d'espace, des tuples auraient pu être utilisés car aucune modification n'est apportée à ces objets une fois créés. Mais comme les tuples n'ont été que peu voire pas abordés, le choix de faire des listes est resté.

Ce dictionnaire est enfin mis dans un fichier texte intitulé  **`index.txt`**. afin d'être réutilisé par la suite.

Le second script python, **`recherche_plot.py`**, utilise ces informations afin de tracer un graphique qui correspond à la valeur moyenne pour chaque intervalle sur une plage de longueur d'onde imposée par l'utilisateur (ex : 700-900 nm).
Le graphique est une courbe, avec également les incertitudes pour chaque intervalle.

NB : l'utilisateur est mis en garde qu'en prenant une plage de longueur d'onde trop importantes et/ou un trop petit pas peut diminuer la lisibilité du graphique.

##  Licence

Ce projet est distribué sous licence Creative Commons (CC).

## Auteur

Théo Vicedo
<theo.vicedo@etu.umontpellier.fr>