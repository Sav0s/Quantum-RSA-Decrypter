import rsa

def factorize(factor):
    result = list()
    for i in range(2, factor):
        if n % i == 0:
            result.append(i)
    return result[0], result[1]


def extgcd(a, b):
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t
    return a, u, v


if __name__ == '__main__':
    e, n = rsa.createRSA(16 )
    print(e, n)
    p, q = factorize(n)
    print(f"Found factors: {p} and {q}")
    phi = (p - 1) * (q - 1)
    a, d, k = extgcd(23, phi)
    print(d, k)
