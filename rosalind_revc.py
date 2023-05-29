replace_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def replace_func(char):
    try: 
        return replace_dict[char]
    except Exception:
        return char

with open('rosalind_revc.txt') as f:
    in_string = f.readline()

rev_string = in_string[::-1]
out_string = ''
for char in rev_string:
    out_string += replace_func(char)

print(out_string)