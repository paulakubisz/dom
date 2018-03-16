
# program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

zakres = [1,3,2,4,2,5,2,6,4,7,9,10,11,14]

for element in zakres:
    if element % 2 == 0:
        print(f"{element} - Parzysta")

    else:
        print(f"{element} - Nieparzysta")