# Lecture CSV + strucure de données 
import csv

with open("APP-3/800.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne)