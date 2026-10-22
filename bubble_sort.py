cisla = [5, 9, 7, 1, 3, 11]
delka = len(cisla)

for i in range(delka):
    for j in range(delka-1):
        if cisla[j] > cisla[j+1]: #když je další číslo menší
            cisla[j], cisla[j+1] = cisla[j+1], cisla[j] #prohodím je
            
print(cisla)

#Maximální časová náročnost O(n^2)
