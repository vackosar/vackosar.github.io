import matplotlib.pyplot as plt

r = 1
q = 0.1


def current_k(p: float):
    return (p + q) / (p + q + r)


def next_p(p: float, k: float):
    return p + q + k * (p + q)


ps = []
ks = []

p = 1
for i in range(30):
    k = current_k(p)
    ks.append(k)
    p = next_p(p, k)
    ps.append(p)


plt.plot(ks)
plt.plot(ps)
plt.show()

