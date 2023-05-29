with open('rosalind_tree.txt') as f:
    lines = f.readlines()

nn = int(lines.pop(0))

print(nn-1 - len(lines))