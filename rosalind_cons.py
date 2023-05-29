import numpy as np

with open('rosalind_cons.txt') as f:
    lines = f.readlines()

dna_dict = {}
for line in lines:
    if line.startswith(">Rosalind_"):
        current_dna = line[1:].rstrip()
        dna_dict[current_dna] = ""
    else:
        dna_dict[current_dna] += line.rstrip()

length = len(dna_dict[lines[0][1:].rstrip()])

char2idx = {"A":0, "C":1, "G":2, "T":3}
idx2char = {0:"A", 1:"C", 2:"G", 3:"T"}

cons_mtx = np.zeros([4, length], dtype=int)

for string in dna_dict.values():
    for idx, char in enumerate(string):
        cons_mtx[char2idx[char], idx] += 1

cons = ""
for col in range(cons_mtx.shape[1]):
    cons += idx2char[np.argmax(cons_mtx[:,col])]

with open("rosalind_cons_out.txt", "w") as f:
    f.write(cons + '\n')
    for i in range(4):
        f.write(idx2char[i] + ": ")
        for val in cons_mtx[i,:]:
            f.write(str(val) + " ")
        f.write("\n")