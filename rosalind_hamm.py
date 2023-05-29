with open('rosalind_hamm.txt') as f:
    in_strings = f.readlines()

dist_count = 0
for i in range(len(in_strings[0])):
    if in_strings[0][i] != in_strings[1][i]:
        dist_count += 1

print(dist_count)