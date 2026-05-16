# Regroupement par program_id , ordre d'appel , admis + liste d'attente 
from chargement import*
from formatage import*
from tri import*
def parcoursup(id_program,tri):
    admis, attente = [], []
    candidatures = candidature_program(id_program)
    capacite = int(info_program(id_program)["capacity"])
    liste_candidats_ids = candidatures[1]

    if capacite >= candidatures[0]:
        admis.extend(liste_candidats_ids)
        return f"Les étudiants admis sont {admis}."

    else:
        liste_candidats = []
        for i in liste_candidats_ids:
            liste_candidats.append(info_etudiant(i))
        
        liste_triee = tri(liste_candidats)
        for v in range(capacite):
            admis.append(liste_triee[v]["candidate_id"])
        for x in liste_triee[capacite:]:
            attente.append(x["candidate_id"])
        return f"Les étudiants admis sont {admis}.\nLes étudiants en file d'attente sont {attente}."

print(parcoursup("2",tri_insertion))

