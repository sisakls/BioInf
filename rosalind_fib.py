with open('rosalind_fib.txt') as f:
    in_string = f.readline()

n_months, k_rate = in_string.split()
n_months, k_rate = int(n_months), int(k_rate)

rabbits = [1, 1, None]
for _ in range(n_months-2):
    rabbits[2] = k_rate*rabbits[0] + rabbits[1]
    rabbits[0] = rabbits[1]
    rabbits[1] = rabbits[2]
print(rabbits[1])