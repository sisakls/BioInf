from scipy.special import comb

with open('rosalind_iprb.txt') as f:
    k_dom, m_het, n_rec = f.readline().split()

k_dom, m_het, n_rec = int(k_dom), int(m_het), int(n_rec)

sum_ = k_dom + m_het + n_rec
divisor = comb(sum_, 2, exact=True)

prob_dom = divisor - comb(m_het + n_rec, 2, exact=True)
prob_hethet = comb(m_het, 2, exact=True)
prob_hetrec = m_het * n_rec

prob = (prob_dom + 0.75*prob_hethet + 0.5*prob_hetrec) / divisor
print(prob)