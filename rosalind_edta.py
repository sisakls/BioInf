with open('rosalind_edta.txt') as f:
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
edta1 = {(-1, -1): ""}
edta2 = {(-1, -1): ""}
for l1 in range(len(dna1)):
    edit[l1, -1] = l1
    edta1[l1, -1] = dna1[:l1]
    edta2[l1, -1] = "-" * l1
for l2 in range(len(dna2)):
    edit[-1, l2] = l2
    edta1[-1, l2] = "-" * l2
    edta2[-1, l2] = dna2[:l2]

for l1 in range(len(dna1)):
    for l2 in range(len(dna2)):
        if dna1[l1] == dna2[l2]:
            edit[l1, l2] = edit[l1-1, l2-1]
            edta1[l1, l2] = edta1[l1-1, l2-1] + dna1[l1]
            edta2[l1, l2] = edta2[l1-1, l2-1] + dna2[l2]
        else:
            idx = min([(l1-1, l2), (l1, l2-1), (l1-1, l2-1)], 
            key = lambda x: edit[x])
            edit[l1, l2] = edit[idx] +1
            if idx == (l1-1, l2-1):
                edta1[l1, l2] = edta1[idx] + dna1[l1]
                edta2[l1, l2] = edta2[idx] + dna2[l2]
            elif idx == (l1-1, l2):
                edta1[l1, l2] = edta1[idx] + dna1[l1]
                edta2[l1, l2] = edta2[idx] + "-"
            elif idx == (l1, l2-1):
                edta1[l1, l2] = edta1[idx] + "-"
                edta2[l1, l2] = edta2[idx] + dna2[l2]
        #print(l1,l2, dna1[:l1+1], dna2[:l2+1], "|", edta1[l1,l2], edta2[l1,l2])

idx = (len(dna1)-1, len(dna2)-1)
with open("rosalind_edta_out.txt", "w") as f:
    f.write(str(edit[idx]) + "\n")
    f.write(str(edta1[idx]) + "\n")
    f.write(str(edta2[idx]) + "\n")