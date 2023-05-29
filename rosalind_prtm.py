with open("monoisotopic-mass-table.txt") as f:
    mass_dict = {}
    for line in f.readlines():
        char, mass = line.rstrip().split()
        mass_dict[char] = float(mass)

with open("rosalind_prtm.txt") as f:
    string = f.readline().rstrip()

print(sum(
    [mass_dict[char] for char in string]
))