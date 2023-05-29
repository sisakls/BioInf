with open('rosalind_lcsm.txt') as f:
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

common_substr = {}
for window in range(1, len(dna1)):
    for start in range(len(dna1) - window + 1):
        string = dna1[start:start+window]
        if string in dna2: 
            try: common_substr[len(string)].append(string)
            except Exception: common_substr[len(string)] = [string]

for length in list(common_substr.keys())[::-1]:
    for substr in common_substr[length]:
        common = True
        for dna in dna_dict.values():
            if not substr in dna: 
                common = False
                break
        if common: 
            print(substr)
            break
    if common: break