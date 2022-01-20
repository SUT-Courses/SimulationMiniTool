import numpy as np
def mean(x): return sum(x) / len(x)


# generate 100 uniform [0:1] random numbers
x = np.random.rand(10000000)
y = np.random.rand(10000000)


x.dot(y) / len(x)
