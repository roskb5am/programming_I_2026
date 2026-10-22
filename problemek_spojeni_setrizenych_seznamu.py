seznam1 = [1, 4, 9, 12, 20]
seznam2 = [2, 3, 10, 15, 18, 25, 28]

 
spojeny_seznam = []
i = 0  # ukazuje na aktuální prvek v seznam1
j = 0  # ukazuje na aktuální prvek v seznam2
 
# Dokud máme prvky v obou seznamech, vezmeme vždy menší z nich
while i < len(seznam1) and j < len(seznam2):
    if seznam1[i] <= seznam2[j]:   #prvek v seznam1 je menší nebo stejný než seznam2
        spojeny_seznam.append(seznam1[i])
        i = i + 1   #posunu pozici v seznam1
    else:   #seznam2 je menší
        spojeny_seznam.append(seznam2[j])
        j = j + 1   #posunu pozici v seznam2

# Předchozí smyčka skončí, jak nám dojde jeden seznam, ale v tom druhém jsou možná ještě další čísla
# Tak je přidáme na konec
while i < len(seznam1):
    spojeny_seznam.append(seznam1[i])
    i = i + 1
while j < len(seznam2):
    spojeny_seznam.append(seznam2[j])
    j = j + 1
 

print(spojeny_seznam)
