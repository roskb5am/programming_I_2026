seznam = [4, 8, 15, 8, 16, 23, 42, 4, 8, 11]

opakujici_se_cisla = []

for i in range(len(seznam)):
    cetnost = 0
    
    for j in range(len(seznam)): #spočtu četnost čísla na pozici i
        if seznam[i]==seznam[j]:
            cetnost += 1

    if cetnost>1 and seznam[i] not in opakujici_se_cisla: #pokud je tam víckrát a není již v seznamu opakujících se čísel
        opakujici_se_cisla.append(seznam[i])

print(opakujici_se_cisla)
        
               
