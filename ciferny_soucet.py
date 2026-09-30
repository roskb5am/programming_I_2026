#!/usr/bin/env python3
#Ciferný součet
n = int(input("Zadej číslo: ")) #Načte číslo z konzole a přetypuje ho na číslo
soucet = 0   #Initializace součnu na nulu, inicializace je důležitá!

while n > 0:   #Cyklus while, dělej něco, dokud je podmína splněna
    posledni_cislice = n % 10   #vymaskuji číslici na pozici jednotek
    soucet += posledni_cislice   #přičtu tuto číslici k součtu
    n = n // 10   #nové číslo je zbytek po dělení deseti, efektivně ho zkouhnu o číslo na pozici jednotek

print(soucet)   #vypsání konečného součtu
