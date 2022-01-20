import math
from sympy import isprime


def gen_linear(a, seed, c, m, replicationNumber=None):
    x = seed
    res = []
    res_s = set()

    replicationNumber = int(
        replicationNumber if replicationNumber is not None else 1e100)
    for i in range(0, replicationNumber):
        x = (a * x + c) % m
        if x in res_s:
            break
        res.append(x)
        res_s.add(x)

    return res


def show_status(a, X0, c, m):
    if math.gcd(a, m) != 1:
        print("=====> a and m are not coprime")
    else:
        print("=====> a and m are coprime")

    if math.gcd(a, c) != 1:
        print("=====> a and c are not coprime")
    else:
        print("=====> a and c are coprime")

    if math.gcd(c, m) != 1:
        print("=====> c and m are not coprime")
    else:
        print("=====> c and m are coprime")

    if math.log(m, 2) % 1 != 0:
        print("=====> m is not a power of 2")
    else:
        print("=====> m is a power of 2")

    if X0 % 2 != 0:
        print("=====> X0 is not even")
    else:
        print("=====> X0 is even")

    print("=====> (a^(m-1)-1)MOD(m) === {}".format((a ** (m - 1) - 1) % m))

    if isprime(m):
        print("----=> m is prime")
    else:
        print("----=> m is not prime")


a = 3
X0 = 1
c = 0
m = 7
replicationNumber = 10
res = gen_linear(a, X0, c, m, replicationNumber=None)


print("=====> {} \n----=> len(result) = {}".format(res, len(res)))
print("----=> m - len(result) = {} || m / len(result) = {}".format(m - len(res), m/len(res)))

show_status(a, X0, c, m)
