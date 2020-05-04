import sys

from rsa import RSA


def factorize(factor):
    result = list()
    for i in range(2, factor):
        if factor % i == 0:
            result.append(i)
        if i % 1000 == 2:
            printProgress(i, factor)
        if len(result) == 2:
            break
    print("\n")
    return result[0], result[1]


def calculateD(e, phi):
    a, d, k = extgcd(e, phi)
    if d < 0:
        d += phi
    return d


def extgcd(a, b):
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t
    return a, u, v


def printProgress(iteration, total):
    sys.stdout.write('\r|---Tried %s from %s possibilties---|' % (iteration, total))
    sys.stdout.flush()


def main():
    bits = 52
    if bits % 2 != 0:
        exit(0)
    bits = int(bits / 2)
    rsa = RSA(bits)
    message = "This message is encrypted"
    cipher = rsa.encrypt(message)
    keySize = len("{0:b}".format(rsa.n))
    print(f"Message was encrypted with a key size of {keySize} Bits")

    print("_____Starting Brute Force_____")
    p, q = factorize(rsa.n)
    print(f"Found factors: {p} and {q}")
    print("_____Reconstructed Private Key_____")
    d = calculateD(rsa.e, rsa.phi)
    print(f"Found d: {d}")
    print("_____Decrypting Message_____")
    reconstructedMessage = rsa.decrypt(cipher)
    print(reconstructedMessage)


if __name__ == '__main__':
    main()
