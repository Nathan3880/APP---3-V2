# Implémentation des algorithmes de tri 

def tri_insertion(liste):
    
    arr = liste[:]
 
    for i in range(1, len(arr)):
        en_cours = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["score"] < en_cours["score"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = en_cours
 
    return arr
 

 def tri_bulles(liste):

    arr = liste[:]
    n = len(arr)
 
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]["score"] < arr[j + 1]["score"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    return arr

# Je suis pas sûr que ça marche mais j'ai adapté les codes de tri du cours à notre cas, en triant les étudiants par score décroissant.