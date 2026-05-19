# Implémentation des algorithmes de tri 
from chargement import*

policy_1 = "score"
policy_2 = "timestamp"

def tri_insertion(liste):
    arr = liste[:]
    for i in range(1, len(arr)):
        en_cours = arr[i]
        j = i - 1
        policy = policy_1
        if arr[j][policy] == en_cours[policy]:
            policy = policy_2
        while j >= 0 and arr[j][policy] < en_cours[policy]:
            arr[j + 1] = arr[j]
            j = j -1
            policy = policy_1
            if arr[j][policy] == en_cours[policy]:
                policy = policy_2
        arr[j + 1] = en_cours
    
    
    return arr
 

def tri_bulles(liste):
    arr = liste[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            policy = policy_1
            if arr[j][policy] == arr[j + 1][policy]:
                policy = policy_2
            if arr[j][policy] < arr[j + 1][policy]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    return arr



def fusion(liste1,liste2):
    liste = []
    i,j = 0,0
    while i < len(liste1) and j <len(liste2):
        policy = policy_1
        if liste1[i][policy] == liste2[j][policy]:
            policy = policy_2
        if liste1[i][policy] > liste2[j][policy]:
            liste.append(liste1[i])
            i+=1
        else:
            liste.append(liste2[j])
            j+=1
    while i <len(liste1):
        liste.append(liste1[i])
        i+=1
    while j <len(liste2):
        liste.append(liste2[j])
        j+=1
    return liste

def tri_fusion(liste):
    if len(liste) < 2:
        return liste
    else:
        milieu = len(liste) //2
        liste1 = tri_fusion(liste[:milieu])
        liste2 = tri_fusion(liste[milieu:])
    return fusion(liste1,liste2)



def tri_rapide(liste):
    if len(liste) < 2:
        return liste
    l1,l2 = [],[]
    e = liste[0]
    for x in liste[1:]:
        policy = policy_1
        if x[policy] == e[policy]:
            policy = policy_2
        if x[policy] > e[policy]:
            l1.append(x)
        else:
            l2.append(x)
    return tri_rapide(l1) + [e] + tri_rapide(l2)




# Je suis pas sûr que ça marche mais j'ai adapté les codes de tri du cours à notre cas, en triant les étudiants par score décroissant.