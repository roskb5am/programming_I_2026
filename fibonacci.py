n = int(input()) #počet členů poslupnosti
fibonacci = [0, 1]

for i in range(n-2): #první dvě čísla již mám
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
print(fibonacci)
