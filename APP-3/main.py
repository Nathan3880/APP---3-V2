from chargement import*
from formatage import*
from tri import*
from performances import*
from timeit import*
import matplotlib.pyplot as plt

fichier_candidats = input("Entrez un fichier de candidats : ")
fichier_formations = input("Entre un fichier de formations : ")
id_formation = input("Entrez un identifiant de formation : ")

candidats_liste = lire_csv_candidats(fichier_candidats)
formations_liste = lire_csv_formations(fichier_formations)
print(parcoursup(id_formation,candidats_liste,formations_liste,tri_rapide))
print("-------------------------------------------------------------------------------------------------------")
print(f"Le tri a pris {performances(id_formation,candidats_liste,formations_liste,tri_rapide)} secondes pour définir l'ordre de priorité")

graphique_perf(id_formation, formations_liste)

