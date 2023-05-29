with open('rosalind_dna.txt') as f:
    in_string = f.readline()

char_count = {}
for char in in_string:
    try: char_count[char] += 1
    except Exception: char_count[char] = 1

out_string = ''
for char in ['A', 'C', 'G', 'T']:
    out_string += str(char_count[char]) + ' '

print(out_string)