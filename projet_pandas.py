import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Ce code va nous permettre d'extraire et mettre en forme les données du fichier baccalauréat

df = pd.read_csv('fr-en-reussite-au-baccalaureat-origine-sociale.csv', sep = ";") # Il y a des virgules dans le csv, on définit donc le séparateur comme étant ";"
print(df.describe())
print(df.info)

""" à faire :

résultats en fonction des années, à chaque bac (bac plus facile avec le temps?)
résultats en fonction de la filière choisie (bac techno ou pro plus facile?)
Résultats en fonction de l'origine sociale pour chaque filière 
nombre de candidats dans les filières en fonction des origines sociales (+ de bac techno pour les ouvriers par ex)
Faire des graphiques pour chaque origine sociale en fonction des années
nb de candidats issue d'une origine sociale = indicateur du nb de gens dans cette catégorie sociale

Idées bonus : 
Ajouter le revenu moyen de chaque milieu pour tracer les résultats en fonction des revenus ( corrélation ?)

"""