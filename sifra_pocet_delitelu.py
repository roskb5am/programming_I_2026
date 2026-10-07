# 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, … Co následuje?
# Počet dělitelů čísla n

n = int(input())
x = 1

while x <= n:
    pocet_delitelu = 0
    delitel = 1
    while delitel <= x:
        if x%delitel == 0:
            pocet_delitelu += 1
        delitel += 1
    print(pocet_delitelu)
    x += 1
