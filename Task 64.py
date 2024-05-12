from math import *

list_squares = []

list_non_squares = []

for i in range(1, 101):
    list_squares.append(i**2)

for i in range(1, 10001):
    if i in list_squares:
        continue
    else:
        list_non_squares.append(i)

def fraction_representations(number):
    list = []
    a = sqrt(number)
    b = int(a)
    c = 1
    for i in range(500):
        k = number - b**2
        d = int(c*(a + b)) // k
        list.append(d)
        b = ceil((d*k - b*c)/c)
        c = ceil(k/c)
    return list

def period(B):
    L1 = len(B)
    D = set(B)
    L = len(D)
    if L == 1:
        return 1
    else:
        for j in range(2, L1 + 1):
            predel = int((L1 // j) - 1)
            k = 0
            for i in range(0, j):
                for jj in range(1, predel + 1):
                    if B[i] == B[i + jj*j]:
                        k += 1
            if k == (j*predel):
                return j
            else:
                continue 

count = 0

for i in list_non_squares:
    if period(fraction_representations(i)) % 2 == 1:
        count += 1

print(count)
