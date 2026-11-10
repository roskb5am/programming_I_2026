def nasobilka(zaklad, do):
    seznam=[]
    for i in range(zaklad,do,zaklad):
        seznam.append(i)
    return seznam

print(nasobilka(4,30))
