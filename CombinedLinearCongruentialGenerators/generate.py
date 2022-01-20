def combined_linear_cong(n=10000):
    r = [0.0] * n

    m1 = 2147483563
    a1 = 40014
    y1 = 1

    m2 = 2147483399
    a2 = 40692
    y2 = 1

    for i in range(n):

        y1 = a1 * y1 % m1
        y2 = a2 * y2 % m2

        x = (y1 - y2) % (m1 - 1)

        if x > 0:
            r[i] = (x / m1)
        else:
            r[i] = (m1 - 1) / m1

    return r


print(combined_linear_cong())
