import math
import random

import Crypto.Random
import Crypto.Util.number


class RSA:
    def __init__(self, bits=None, n=15):
        if bits != None:
            self.p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
            self.q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
            self.n = self.p * self.q
        else:
            self.n = 15
            self.p = 3
            self.q = 5
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.__chooseE()
        self.d = self.__egcd()


    def __chooseE(self):
        e = random.randrange(1, self.phi)

        # Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = math.gcd(e, self.phi)
        while g != 1:
            e = random.randrange(1, self.phi)
            g = math.gcd(e, self.phi)
        return e

    def __egcd(self):
        u, v, s, t = 1, 0, 0, 1
        a = self.e
        b = self.phi
        while b != 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        if u < 0:
            u += self.phi
        return u

    def encrypt(self, msg):
        return [pow(ord(char), self.e, self.n) for char in msg]
