with open('rosalind_sset.txt') as f:
    nn = int(f.readline())

mod = 1000000

print(2**nn % mod)