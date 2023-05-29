with open('rosalind_sseq.txt') as f:
    lines = f.readlines()

dna_dict = {}
for line in lines:
    if line.startswith(">Rosalind_"):
        current_dna = line[1:].rstrip()
        dna_dict[current_dna] = ""
    else:
        dna_dict[current_dna] += line.rstrip()

dna1 = dna_dict.pop(
    next(iter(dna_dict.keys())))
dna2 = dna_dict.pop(
    next(iter(dna_dict.keys())))

with open("rosalind_sseq_out.txt", "w") as f:
    target = 0
    for i in range(len(dna1)):
        if dna1[i] == dna2[target]:
            target += 1
            f.write(str(i+1) + " ")
        if target == len(dna2): break