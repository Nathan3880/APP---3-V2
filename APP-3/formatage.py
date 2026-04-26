# Fonction d'affichage
from chargement import*


def info_etudiant(id_etudiant):
    for candidat in lire_csv_candidats("parcoursup_small_10000.csv"):
        if candidat["candidate_id"] == id_etudiant:
            return candidat
    return "Il n'existe aucun étudiant ayant cet identifiant"
    

print(info_etudiant("11325"))