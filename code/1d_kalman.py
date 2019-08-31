import matplotlib.pyplot as plt

r = 1
q = 2
p = 3


def current_k(p: float):
    return (p + q) / (p + q + r)


def next_p(p: float, k: float):
    return (1 - k) * (p + q)


ps = []
ks = []

for i in range(10):
    k = current_k(p)
    ks.append(k)
    p = next_p(p, k)
    ps.append(p)


plt.plot(ks, label='ks')
plt.plot(ps, label='ps')
plt.legend()
plt.savefig('../images/test.png')
plt.show()

# plt.plot(ps, label='ps')
# plt.legend()
# plt.show()
#
