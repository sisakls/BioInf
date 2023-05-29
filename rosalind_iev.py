with open("rosalind_iev.txt") as f:
    strings = f.readline().rstrip().split()
vals = [int(char) for char in strings]

exp = vals[0] + vals[1] + vals[2] + 0.75*vals[3] + 0.5*vals[4]
print(2*exp)