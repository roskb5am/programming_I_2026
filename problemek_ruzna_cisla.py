seznam = [4, 8, 15, 8, 16, 23, 42, 4, 8, 11]

jsou_ruzna = True

for i in range(len(seznam)):
    for j in range(i + 1, len(seznam)):
        if seznam[i] == seznam[j]:
            jsou_ruzna = False
 
if jsou_ruzna:
    print("Čísla jsou různá")
else:
    print("Některé číslo se opakuje")

            
