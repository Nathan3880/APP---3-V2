# Lecture CSV + strucure de données 
import csv
import os

def lire_csv_formations(nom_fichier):
    formations = []
    chemin = os.path.join(os.path.dirname(__file__), nom_fichier)
    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            formations.append(ligne)
    return formations

print(lire_csv_formations("800.csv"))

def lire_csv_candidats(nom_fichier):
    candidats = []
    chemin = os.path.join(os.path.dirname(__file__), nom_fichier)
    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            candidats.append(ligne)
    return candidats

print(lire_csv_candidats("parcoursup_small_10000.csv"))