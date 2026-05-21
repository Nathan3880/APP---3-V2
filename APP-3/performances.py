# Mesure des temps de tri sur gros volumes
from timeit import*
from tri import*
from chargement import*
from parcoursup import*
import matplotlib.pyplot as plt


def performances(id_program,candidats_liste,formations_liste, tri):
    t1 = default_timer()
    parcoursup(id_program,candidats_liste,formations_liste, tri)
    t2 = default_timer()
    return t2-t1

def graphique_perf(id_program, formations_liste):
    taille = [10000,100000,500000]
    tri_insertion_liste = [performances(id_program,lire_csv_candidats("parcoursup_small_10000.csv"),formations_liste,tri_insertion), performances(id_program, lire_csv_candidats("parcoursup_medium_100000.csv"),formations_liste,tri_insertion),performances(id_program,lire_csv_candidats("parcoursup_massive_500000.csv"),formations_liste,tri_insertion)]
    tri_bulles_liste = [performances(id_program,lire_csv_candidats("parcoursup_small_10000.csv"),formations_liste,tri_bulles),performances(id_program,lire_csv_candidats("parcoursup_medium_100000.csv"),formations_liste,tri_bulles),performances(id_program,lire_csv_candidats("parcoursup_massive_500000.csv"),formations_liste,tri_bulles)]
    tri_fusion_liste = [performances(id_program,lire_csv_candidats("parcoursup_small_10000.csv"),formations_liste,tri_fusion),performances(id_program,lire_csv_candidats("parcoursup_medium_100000.csv"),formations_liste,tri_fusion),performances(id_program,lire_csv_candidats("parcoursup_massive_500000.csv"),formations_liste,tri_fusion)]
    tri_rapide_liste = [performances(id_program,lire_csv_candidats("parcoursup_small_10000.csv"),formations_liste,tri_rapide),performances(id_program,lire_csv_candidats("parcoursup_medium_100000.csv"),formations_liste,tri_rapide),performances(id_program,lire_csv_candidats("parcoursup_massive_500000.csv"),formations_liste,tri_rapide)]
    plt.plot(taille,tri_insertion_liste, label = "Tri insertion")
    plt.plot(taille,tri_bulles_liste, label = "Tri bulles")
    plt.plot(taille,tri_fusion_liste, label = "Tri fusion")
    plt.plot(taille,tri_rapide_liste, label = "Tri rapide")
    plt.ylabel("Temps (en s)")
    plt.xlabel("Données")
    plt.title("Évolution du temps pour trier des données\n suivant la quantité de données et le tri utilisé")
    plt.grid(True)
    plt.legend()
    plt.show()