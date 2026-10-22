#Pojďme těžit ze setřízenosti - binární vyhledávání
cisla = [1, 3, 5, 7, 9, 11]
co_hledam = int(input())

#hledám v podintervalu [first, last], na poprvé je to celá velikost seznamu
first = 0 #začátek pozintervalu vyhledávání
last = len(cisla) - 1 #konec pozintervalu vyhledávání (včetně)

while first <= last:
    stred = (first + last) // 2 #celočíselné dělení
    if cisla[stred] == co_hledam: #jsme se rovnou trefili
        print("Hledané číslo je na pozici",stred)
        break
    elif cisla[stred] < co_hledam:
        first = stred +1 #hledané číslo větší než střed - nový podinterval začne o jedna více než střed
    else:
        last = stred - 1 #hledané číslo menší než střed - nový podinterval končí o jedna méně než střed
        
else: #ani pro nejmenší interval jsem číslo nenašel, v seznamu není
    print("Hledané číslo v seznamu není")
