def sucin(zoznam):
    x = 1
    if len(zoznam) >= 2:

        for i in range(0,len(zoznam)):
            x*=zoznam[i]
    else:
        print("1")
    return x

c = [2, 3, 5, 7, 11]
print(sucin(c))
