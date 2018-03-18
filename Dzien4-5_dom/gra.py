
import random

poda_cyfry = input("Podaj wylosowaną liczbę: ")

wynik = (sorted(random.sample(range(1,12),3)))
print(f"W dzisiejszym losowaniu znjadują się liczby: {(sorted(random.sample(range(1,12),3)))}")

if set(poda_cyfry) == set(wynik):
    print("Wygrałęś")

# Czy mog prosi o pomoc co tutaj ma zle? chcialabym sprawdzic czy wpisany element jest w randomowej liscie? :)

elif poda_cyfry.issuperset(wynik):

    print("Blisko, blisko!")

else:
    print("Przykro przegrales!")
