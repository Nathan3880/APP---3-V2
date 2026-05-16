# Mesure des temps de tri sur gros volumes
from timeit import*
from tri import*
from chargement import*
from parcoursup import*


def performances(id_program, tri):
    t1 = default_timer()
    parcoursup(id_program, tri)
    t2 = default_timer()
    return f"Le tri a besoin de {t2-t1} secondes pour trier les candidats"

print(performances("1", tri_rapide))

