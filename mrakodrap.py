#jdu po schodech v mrakodrapu a vypisuji v jakém patře jsem

pocet_pater = 20
moje_patro = 0

while moje_patro<pocet_pater:
    moje_patro += 1
    if moje_patro == 13: #budova nema 13. patro kvuli povercivym
        continue
    if moje_patro > 17:
        print("18. patro zatím není postaveno") 
        break
    print("Jsem v", moje_patro, ". patře")
else:
    print("Dosáhl jsem střechy budovy")
