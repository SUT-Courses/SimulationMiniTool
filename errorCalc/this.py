import scipy.stats


def t(alpha, n):
    # if n samples pass n-1
    return scipy.stats.t.ppf(1-(alpha), n)


def norm(alpha):
    # if n samples pass n-1
    return scipy.stats.norm.ppf(1-(alpha))


# inputs
ls = [3.27,
      16.25,
      15.19,
      7.24,
      2.93]
ERR = 10
alpha_right = 0.025
############

std = (sum([(x - sum(ls) / len(ls)) ** 2 for x in ls]) / (len(ls)-1)) ** 0.5
se = std / (len(ls) ** 0.5)


def level_z(): return (norm(alpha_right))
def get_ts0e(l): return (t(alpha_right, l-1)*std/ERR)**2


R0 = (level_z()*std/ERR)**2
print("R0 :", R0)

R_i = int(R0) + 1
print("R_i :", R_i)


while True:
    print(R_i, ":", get_ts0e(R_i))
    if get_ts0e(R_i) < R_i:
        break
    R_i += 1
