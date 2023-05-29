with open('rosalind_subs.txt') as f:
    in_string, target_string = f.readlines()

target_string = target_string.rstrip()

match_pos = []
length = len(target_string)

for i in range(len(in_string) - length + 1):
    if in_string[i : i+length] == target_string:
        match_pos.append(i+1)

print(*match_pos)