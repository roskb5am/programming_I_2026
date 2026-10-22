#brute force
cisla = [1, 3, 5, 7, 9, 11] #setříděný seznam - čísla podle velikosti
co_hledam = int(input())

for i in range(len(cisla)):
    if co_hledam == cisla[i]:
        print("Hledané číslo je na pozici",i)
        break
else:
    print("Hledané číslo v seznamu není")
