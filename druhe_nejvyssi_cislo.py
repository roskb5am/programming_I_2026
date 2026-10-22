cisla = [3, 2, 8, 10, 9, 13, 11]

if cisla[0] > cisla[1]: #inicilaizuju podle prvních dvou vstupů
    nejvyssi_cislo = cisla[0] #držím si nejvyšší číslo
    druhe_nejvyssi_cislo = cisla[1] #držím si i 2. nejvyšší číslo
else:
    nejvyssi_cislo = cisla[1]
    druhe_nejvyssi_cislo = cisla[0]
    
for i in range(2,len(cisla)): #postupně procházím
    if cisla[i]> nejvyssi_cislo: #když najdu nové maximum
        druhe_nejvyssi_cislo = nejvyssi_cislo #staré dám jako 2.
        nejvyssi_cislo = cisla[i] #změním na nové maximum
        
print(druhe_nejvyssi_cislo)
