# Regroupement par program_id , ordre d'appel , admis + liste d'attente 
from chargement import*
from formatage import*
from tri import*
def parcoursup(id_program,candidats_liste,formations_liste, tri):
    admis, attente = [], []
    candidatures = candidature_program(id_program, candidats_liste)
    capacite = int(info_program(id_program, formations_liste)["capacity"])
    liste_candidats = candidatures[1]

    if capacite >= candidatures[0]:
        admis.extend(liste_candidats)
        return f"Les étudiants admis sont {admis}."

    else:
        
        liste_triee = tri(liste_candidats)
        for v in range(capacite):
            admis.append(liste_triee[v]["candidate_id"])
        for x in liste_triee[capacite:]:
            attente.append(x["candidate_id"])
        return f"Les étudiants admis sont {admis}.\n-------------------------------------------------------------------------------------------------------\n Les étudiants en file d'attente sont {attente}."

