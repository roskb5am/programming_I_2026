#Třídění opakovaným výběrem minima
cisla = [5, 9, 7, 1, 3, 11]
delka = len(cisla)

for i in range(delka):
    pozice_minima = i #inicializuju na prvni možnou pozici
    for j in range(i+1,delka):
        if cisla[j] < cisla[pozice_minima]:
            pozice_minima = j #našel jsem novou pozici minima
            
    #teď mám minimum z pozic i až delka
    #hodnotu na pozici minima (minimum) vyměním s první pozicí
    cisla[i], cisla[pozice_minima] = cisla[pozice_minima], cisla[i] #toto je syntaxe pro dvojí přiřazení

print(cisla)

#Časová náročnost vždy O(n^2)
