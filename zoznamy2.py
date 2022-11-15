def nakup(zoznam):
    if type(zoznam) == list:
        výsledok = 0
        x = 0
        for i in range(0,len(zoznam)):

            if i % 2 == 0:
                x=zoznam[i]
            else:
                výsledok += (x*zoznam[i])

        print(výsledok)

    else:
        print("toto nie je zoznam")

nakup([3, 2.5, 0.5, 10, 1.2, 1.2])