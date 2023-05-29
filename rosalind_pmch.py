from math import factorial

with open("rosalind_pmch.txt") as f:
    f.readline()
    AUcnt, GCcnt = 0, 0
    for line in f.readlines():
        AUcnt += line.count('A')
        GCcnt += line.count('G')

print(factorial(AUcnt) * factorial(GCcnt))