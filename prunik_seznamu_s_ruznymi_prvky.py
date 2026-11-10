def prunik(seznam1, seznam2):
    vysledek = []
    for x in seznam1:
        if x in seznam2:
            vysledek.append(x)
    return vysledek
