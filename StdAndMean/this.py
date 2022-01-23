import scipy.stats


def t(alpha, n):
    # if n samples pass n-1
    return scipy.stats.t.ppf(1-(alpha/2), n)


ls = [3.27,
      16.25,
      15.19,
      7.24,
      2.93]


mean = sum(ls) / len(ls)
se = (sum([(x - sum(ls) / len(ls)) **
      2 for x in ls]) / (len(ls)-1)) ** 0.5 / (len(ls) ** 0.5)

print("mean:", mean)

print("standard deviation S:",
      (sum([(x - sum(ls) / len(ls)) ** 2 for x in ls]) / (len(ls)-1)) ** 0.5)

print("standard error S / (R^.5):", se)


level = t(0.05, len(ls)-1)
print("Confidence interval:", mean - level * se, "to", mean + level * se)
