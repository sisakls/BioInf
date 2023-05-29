with open('RNA_codon_table.txt') as f:
    lines = f.readlines()

codon_dict = {}
for line in lines:
    string = line.rstrip()
    codon_dict[string[:3]] = string[4:]

with open('rosalind_splc.txt') as f:
    lines = f.readlines()

dna_dict = {}
for line in lines:
    if line.startswith(">Rosalind_"):
        current_dna = line[1:].rstrip()
        dna_dict[current_dna] = ""
    else:
        dna_dict[current_dna] += line.rstrip()

target_dna = dna_dict.pop(lines[0][1:].rstrip())

for string in dna_dict.values():
    target_dna = target_dna.replace(string, "")
target_dna = target_dna.replace("T", "U")

out_string = ""
for i in range(0,len(target_dna),3):
    translation = codon_dict[target_dna[i:i+3]]
    if translation == "Stop":
        break
    else:
        out_string += translation

print(out_string)