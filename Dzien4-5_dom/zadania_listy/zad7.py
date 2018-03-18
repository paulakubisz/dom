# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

import collections
x = ['c', 'b']
y = ['b', 'c']

if collections.Counter(x) == collections.Counter(y):
    print(True)
else:
    print(False)


print("---B---")

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B))