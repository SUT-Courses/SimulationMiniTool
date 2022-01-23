import scipy.stats


def t(alpha, n):
    # if n samples pass n-1
    return scipy.stats.t.ppf(1-(alpha), n)


def norm(alpha):
    # if n samples pass n-1
    return scipy.stats.norm.ppf(1-(alpha))
