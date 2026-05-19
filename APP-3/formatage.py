# Fonction d'affichage
from chargement import*


def info_etudiant(id_etudiant):
    for candidat in lire_csv_candidats("parcoursup_massive_500000.csv"):
        if candidat["candidate_id"] == id_etudiant:
            return candidat
    return "Il n'existe aucun étudiant ayant cet identifiant"
    

def info_program(id_program):
    for program in lire_csv_formations("parcoursup_programs_small_800.csv"):
        if program["program_id"] == id_program:
            return program
    return "Il n'existe aucune formation ayant cet identifiant"


def candidature_program(id_program):
    compteur = 0
    liste_etudiant = []
    for candidat in lire_csv_candidats("parcoursup_massive_500000.csv"):
        if candidat["program_id"] == id_program:
            liste_etudiant.append(candidat)
            compteur += 1
    return (compteur, liste_etudiant)