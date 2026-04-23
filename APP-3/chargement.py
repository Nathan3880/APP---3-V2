# Lecture CSV + strucure de données 
import csv
import os

def lire_csv(nom_fichier):
    candidats = []
    chemin = os.path.join(os.path.dirname(__file__), nom_fichier)
    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            candidats.append(ligne)
    return candidats

print(lire_csv("800.csv"))