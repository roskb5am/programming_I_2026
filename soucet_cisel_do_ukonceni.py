# Načítá posloupnost čísel ze vstupu dokud nazadám -1
# Pak vypíše jejich součet

soucet = 0
while True:
    n = int(input())
    if n == -1:
        break
    soucet += n
print(soucet)
