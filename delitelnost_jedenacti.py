#Dělitelnost jedenácti - číslo je dělitelné 11 pokud je alternující ciferný součet,
#kde střídavě přičítáme a odečítáme cifry, dělitelný 11

#Příklad: 1243. Alternující součet 3 -4 +2 -1 = 0 => číslo 1243 je dělitelné 11

n = int(input("Zadej číslo: ")) 
soucet = 0   #initializace souču

faktor = 1   #faktor, který bude alternovat znaménko

while n > 0:  
    posledni_cislice = n % 10
    soucet = soucet + faktor*posledni_cislice   #faktor je buď 1 nebo -1
    faktor *= -1   #faktor při každé operaci vynásobím -1, čímž efektivně měním znaménko
    n = n // 10   

if soucet%11 == 0:
    print("Cislo je delitelne jedenacti")
if soucet%11 != 0:
    print("Cislo neni delitelne jedenacti")
