# Fonction d'affichage
from chargement import*


def info_etudiant(id_etudiant, candidats_liste):
    for candidat in candidats_liste:
        if candidat["candidate_id"] == id_etudiant:
            return candidat
    return "Il n'existe aucun étudiant ayant cet identifiant"
    

def info_program(id_program, formations_liste):
    for program in formations_liste:
        if program["program_id"] == id_program:
            return program
    return "Il n'existe aucune formation ayant cet identifiant"


def candidature_program(id_program, candidats_liste):
    compteur = 0
    liste_etudiant = []
    for candidat in candidats_liste:
        if candidat["program_id"] == id_program:
            liste_etudiant.append(candidat)
            compteur += 1
    return (compteur, liste_etudiant)