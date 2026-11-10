def min_dvou(a,b):
    if a>=b:
        return a
    else return b

def min_tri(a,b,c):
    return min_dvou(a,min_dvou(b,c))
