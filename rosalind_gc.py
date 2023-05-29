with open('rosalind_gc.txt') as f:
    lines = f.readlines()

dna_dict = {}
for line in lines:
    if line.startswith(">Rosalind_"):
        current_dna = line[1:].rstrip()
        dna_dict[current_dna] = ""
    else:
        dna_dict[current_dna] += line.rstrip()

gc_dict = {}
for name, string in dna_dict.items():
    gc = 0
    for char in string:
        if char == "G" or char == "C": 
            gc += 1

    gc_dict[name] = gc / len(string)

out_name, out_gc = max(gc_dict.items(), key=lambda x:x[1])

print(out_name, "\n", out_gc*100)