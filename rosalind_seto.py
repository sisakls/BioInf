with open('rosalind_seto.txt') as f:
    nn_string, A_string, B_string = f.readlines()

nn = int(nn_string)
UU = set(range(1,nn+1))

AA = set(
    A_string.replace(',', '')[1:-2].split())
AA = set(map(int, AA))
BB = set(
    B_string.replace(',', '')[1:-2].split())
BB = set(map(int, BB))

with open("rosalind_seto_out.txt", "w") as f:
    f.write(str(AA.union(BB)) + "\n")
    f.write(str(AA.intersection(BB)) + "\n")
    f.write(str(AA.difference(BB)) + "\n")
    f.write(str(BB.difference(AA)) + "\n")
    f.write(str(UU.difference(AA)) + "\n")
    f.write(str(UU.difference(BB)) + "\n")