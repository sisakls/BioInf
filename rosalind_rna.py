with open('rosalind_rna.txt') as f:
    in_string = f.readline()

out_string = in_string.replace('T', 'U')

print(out_string)