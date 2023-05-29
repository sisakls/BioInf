with open('rosalind_lcsq.txt') as f:
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

sseq = {(-1,-1): ""}
for l1 in range(len(dna1)):
    sseq[l1, -1] = ""
for l2 in range(len(dna2)):
    sseq[-1, l2] = ""

for l1 in range(len(dna1)):
    for l2 in range(len(dna2)):
        if dna1[l1] == dna2[l2]:
            sseq[l1, l2] = sseq[l1-1, l2-1] + dna1[l1]
        else:
            sseq[l1, l2] = max([sseq[l1-1, l2], sseq[l1, l2-1]], key=len)
        #print(l1,l2,sseq[l1,l2], dna1[:l1], dna2[:l2])

print(sseq[len(dna1)-1, len(dna2)-1])