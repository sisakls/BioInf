with open('rosalind_grph.txt') as f:
    lines = f.readlines()

dna_dict = {}
for line in lines:
    if line.startswith(">Rosalind_"):
        current_dna = line[1:].rstrip()
        dna_dict[current_dna] = ""
    else:
        dna_dict[current_dna] += line.rstrip()

with open("rosalind_grph_out.txt", "w") as f:
    for dna1, string1 in dna_dict.items():
        for dna2, string2 in dna_dict.items():
            if string1[-3:] == string2[:3] and dna1 != dna2:
                f.write(dna1 + " " + dna2 + "\n")