with open('RNA_codon_table.txt') as f:
    lines = f.readlines()

codon_dict = {}
for line in lines:
    string = line.rstrip()
    codon_dict[string[:3]] = string[4:]

with open('rosalind_prot.txt') as f:
    in_string = f.readline().rstrip()

out_string = ""
for i in range(0,len(in_string),3):
    translation = codon_dict[in_string[i:i+3]]
    if translation == "Stop":
        break
    else:
        out_string += translation

print(out_string)