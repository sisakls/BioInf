with open('RNA_codon_table.txt') as f:
    lines = f.readlines()

codon_dict = {}
for line in lines:
    string = line.rstrip()
    codon_dict[string[:3]] = string[4:]

reverse_dict = {}
for val in codon_dict.values():
    try: reverse_dict[val] += 1
    except Exception: reverse_dict[val] = 1

mod = 1000000

with open('rosalind_mrna.txt') as f:
    in_string = f.readline().rstrip()

variation = 1
for char in in_string:
    variation = (variation * reverse_dict[char]) % mod 

print((variation * reverse_dict["Stop"]) % mod)