#Mějme rovni x = e-x ➔ x - e-x = 0. Najděte její řešení numericky s přesností 1e-10.

from math import exp

lower_edge = 0.
upper_edge = 1.
precision = 1e-10

while upper_edge - lower_edge > 1e-10:
    x = (lower_edge + upper_edge) / 2
    if x - exp(-x) < 0:
        lower_edge = x
    else:
        upper_edge = x
        
print("Priblizne reseni je ",(lower_edge + upper_edge) / 2)
