def gen_linear(a, seed, c, m, replicationNumber):
    x = seed
    res = []

    for i in range(0, replicationNumber):
        val = (a * x + c) % m
        res.append(val)
        x = val
    return res


a = 2175143
X0 = 3553
c = 10653
m = 1000000
replicationNumber = 10

res = gen_linear(a, X0, c, m, replicationNumber)
print(res)
