import numpy as np

with open('rosalind_fibd.txt') as f:
    in_string = f.readline()

n_months, m_life = in_string.split()
n_months, m_life = int(n_months), int(m_life)

rabbits = np.zeros([n_months, m_life], dtype='object')
rabbits[0,0] += 1

for n in range(n_months-1):
    rabbits[n+1,0] = sum(rabbits[n,1:])

    for i in range(m_life-1):
        rabbits[n+1,i+1] = rabbits[n,i]
    
print(sum(rabbits[-1,:]))