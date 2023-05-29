with open('rosalind_edit.txt') as f:
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

edit = {(-1, -1): 0}
for l1 in range(len(dna1)):
    edit[l1, -1] = l1
for l2 in range(len(dna2)):
    edit[-1, l2] = l2

for l1 in range(len(dna1)):
    for l2 in range(len(dna2)):
        if dna1[l1] == dna2[l2]:
            edit[l1, l2] = edit[l1-1, l2-1]
        else:
            edit[l1, l2] = min([edit[l1-1, l2], edit[l1, l2-1], edit[l1-1, l2-1]]) +1
        #print(l1,l2, dna1[:l1+1], dna2[:l2+1], edit[l1,l2])

print(edit[len(dna1)-1, len(dna2)-1])