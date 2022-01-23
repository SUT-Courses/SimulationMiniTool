from sympy import diff


HIGH = 100
LOW = 0

ls = [
    88.3,
    91.7,
    98.8,
    32.4,
    20.6,
    76.6,
    40.7,
    67.3,
    90.1,
    87.8,
    73.1,
    73.2,
    36.3,
    7.0,
    17.2,
    69.8,
    21.6,
    27.3,
    27.3,
    45.2,
    23.7,
    62.6,
    6.0,
    87.6,
    36.8,
    23.3,
    97.4,
    99.7,
    45.3,
    87.2
]

nls = list(map(lambda x: (x-LOW)/(HIGH-LOW), ls))
nls.sort()

benchLs_plus = [i/len(ls) for i in range(1, len(nls)+1)]
benchLs_minus = [i/len(ls) for i in range(len(nls))]

diff_plus_ls = [i-j for i, j in zip(benchLs_plus, nls)]
diff_minus_ls = [i-j for i, j in zip(nls, benchLs_minus)]

d_plus, d_minus = max(diff_plus_ls), max(diff_minus_ls)
print(d_plus, d_minus)
print("degree of freedom:", len(ls))
print("max:", max(d_plus, d_minus))
