cisla = [] #prazdný seznam

while True:
    x = int(input())
    if x == -1:
        break #přidávání skončím zadáním -1
    else:
        cisla.append(x) #přidávám čísla na konec seznamu
        
for i in range(len(cisla)):
    print(cisla[-i - 1])
