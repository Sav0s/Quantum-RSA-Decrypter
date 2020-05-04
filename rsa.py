import math
import Crypto.Util.number
import Crypto.Random
import random


def createRSA(bits):
    p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

    print(f"Generated with p: {p} and q: {q}")

    n = p * q

    possibleResults = list()
    for i in range(p - 1):
        if math.gcd(i, p - 1) == 1:
            possibleResults.append(i)

    e = random.choice(possibleResults)

    return e, n
