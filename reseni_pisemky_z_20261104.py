#Faktorial
n = int(input("Zadej kladné celé číslo:"))

faktorial = 1

for i in range(1, n + 1):   #Pamatuj, odkud kam jde range, první včetně, druhé mimo.
    faktorial *= i          #Např. pro n=5 bude i nabývat hodnot 1,2,3,4,5 

print(faktorial)

#---------------------------------------------
#Ciferný součet
cislo = int(input("Zadej celé kladné číslo:"))

soucet = 0

while cislo > 0:
    soucet = soucet + cislo % 10
    cislo = cislo // 10
    
print(soucet)

#---------------------------------------------
#Minimum a jeho pozice
seznam = [7, -2, 5, 8, -3, 0, -1, 10, 152]

minimum = seznam[0]
pozice_minima = 0

for i in range(len(seznam)):
    if seznam[i] < minimum:
        minimum = seznam[i]
        pozice_minima = i
        
print(minimum)
print(pozice_minima)
