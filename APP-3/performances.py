# Mesure des temps de tri sur gros volumes
from timeit import*
from tri import*
from chargement import*

def performances(liste, tri):
    t1 = default_timer()
    tri(liste)
    t2 = default_timer()
    return f"Le tri a besoin de {t2-t1} secondes pour trier les candidats"

print(performances(lire_csv_formations("parcoursup_small_10000.csv"), tri_bulles))

