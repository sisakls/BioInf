from math import factorial
mod = 1000000

with open("rosalind_pper.txt") as f:
    n, k = f.readline().rstrip().split()
n, k = int(n), int(k)

print((factorial(n) / factorial(n-k)) % mod)