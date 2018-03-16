# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

for x in range(20):
    if x % 4 == 0:
        continue
    print(x)