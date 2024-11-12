import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt

# Ce code va nous permettre d'extraire et mettre en forme les données du fichier baccalauréat

df = pd.read_csv('fr-en-reussite-au-baccalaureat-origine-sociale.csv', sep = ";") # Il y a des virgules dans le csv, on définit le séparateur ";"


""" à faire :

résultats en fonction des années, à chaque bac (bac plus facile avec le temps?)
résultats en fonction de la filière choisie (bac techno ou pro plus facile?)
Résultats en fonction de l'origine sociale pour chaque filière 
nombre de candidats dans les filières en fonction des origines sociales (+ de bac techno pour les ouvriers par ex)
Faire des graphiques pour chaque origine sociale en fonction des années
nb de candidats issue d'une origine sociale = indicateur du nb de gens dans cette catégorie sociale

Idées bonus : 
Ajouter le revenu moyen de chaque milieu pour tracer les résultats en fonction des revenus

"""
# On ajoute les colonnes pour avoir le nombre total de candidats
df["nombre_candidats_au_baccalaureat_general"] = np.floor((100/df["pourcentage_d_admis_au_baccalaureat_general"])*df['nombre_d_admis_au_baccalaureat_general'])
df["nombre_candidats_au_baccalaureat_technologique"] = np.floor((100/df["pourcentage_d_admis_au_baccalaureat_technologique"])*df['nombre_d_admis_au_baccalaureat_technologique'])
df["nombre_candidats_au_baccalaureat_professionnel"] = np.floor((100/df["pourcentage_d_admis_au_baccalaureat_professionnel"])*df['nombre_d_admis_au_baccalaureat_professionnel'])
#print(df.columns)
#print(df.isna().sum()) # pas de valeurs manquantes
#print(df["origine_sociale"].unique())
#print(df["annee"].unique())
by_origine = df.groupby(["origine_sociale"])
by_annee = df.groupby(["annee"])
by_origine_annee = df.groupby(["origine_sociale", "annee"])
# print(by_annee['nombre_d_admis_au_baccalaureat_general'].sum())
"""
print(by_origine_annee['pourcentage_d_admis_au_baccalaureat'].mean()) # par catégorie+année tout bac
print(by_origine_annee['pourcentage_d_admis_au_baccalaureat_technologique'].mean()) # par catégorie+année bac techno
print(by_origine_annee['pourcentage_d_admis_au_baccalaureat_general'].mean()) # par catégorie+année bac general
print(by_origine_annee['pourcentage_d_admis_au_baccalaureat_professionnel'].mean()) # par catégorie+année bac pro
"""
by_annee['pourcentage_d_admis_au_baccalaureat'].mean().plot()
plt.show()

by_origine['pourcentage_d_admis_au_baccalaureat'].mean().plot.bar()
plt.show()

by_origine['nombre_d_admis_au_baccalaureat_technologique'].sum().drop(labels = "Ensemble", axis = 0).plot.bar() # drop pour supprimer la ligne "Ensemble" qui est la somme de toutes les autres
plt.show()