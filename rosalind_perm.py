with open('rosalind_perm.txt') as f:
    nn = int(f.readline())

seq_dict = {1: [[1]]}

for n in range(2, nn+1):
    seq_dict[n] = []
    for seq in seq_dict[n-1]:
        for i in range(n):
            new_seq = seq[:i] + [n] + seq[i:]
            seq_dict[n].append(new_seq)

with open("rosalind_perm_out.txt", "w") as f:
    f.write(str(len(seq_dict[nn])) + "\n")
    for seq in seq_dict[nn]:
        for item in seq:
            f.write(str(item) + " ")
        f.write("\n")