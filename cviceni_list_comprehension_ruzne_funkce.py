def prunik_seznamu(x, y):
    return [a for a in x if a in y]

def nasobilka(n):
    return [[i*j for i in range(1, n+1)] for j in range(1, n+1)]

def palindromy(radek):
    return [slovo for slovo in radek.split() if slovo == slovo[::-1]]

def transpozice(x):
    return [[a[i] for a in x] for i in range(len(x[0]))]

def skalarni_soucin(x, y):
    return sum([i*j for i, j in zip(x, y)])

def nasobeni_matic(x, y):
    yt = transpozice(y)
    return [[skalarni_soucin(rx, ryt) for ryt in yt] for rx in x]

def slova_podle_delky(radek):
    dvojice = [ (len(slovo), slovo) for slovo in radek.split() ]
    return [ slovo for _, slovo in sorted(dvojice) ]
