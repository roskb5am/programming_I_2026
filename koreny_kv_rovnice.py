from math import sqrt as sqrt
from math import nan as NaN

def koreny_kvadraticke_rovnice(a,b,c): #ax^2 + bx + c = 0
    dikriminant = b**2 -4*a*c

    if dikriminant > 0:
        x1 = (-b + sqrt(dikriminant))/(2*a)
        x2 = (-b - sqrt(dikriminant))/(2*a)
        print(x1, x2)
    elif dikriminant == 0:
        x = -b/(2*a)
        print(x)
    else:
        print(NaN)

koreny_kvadraticke_rovnice(1,2,-5)
koreny_kvadraticke_rovnice(1,2,1)
koreny_kvadraticke_rovnice(1,2,5)
