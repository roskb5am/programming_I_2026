n = int(input()) #maximalni cislo do kterého testuji
je_prvocislo = [True]*(n+1)

for i in range(2, n+1): #preskakuji 1, začínám od 2
    if je_prvocislo[i]: #pokud True, vypíše číslo, je prvočíslo
        print(i)
        for j in range(2*i, n+1, i): #druhý a každý další násobek i prvočíslo není…
            je_prvocislo[j] = False #… a tak ho nastavím jako False
