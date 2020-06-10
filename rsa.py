import math
import random

import Crypto.Random
import Crypto.Util.number


class RSA:
    def __init__(self, bits=None, n=0):
        if bits != None:
            self.__p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
            self.__q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
            self.n = self.__p * self.__q
        elif n == 21:
            self.n = 21
            self.__p = 3
            self.__q = 7
        elif n == 33:
            self.n = 33
            self.__p = 3
            self.__q = 11
        else:
            self.n = 15
            self.__p = 3
            self.__q = 5
        self.__phi = (self.__p - 1) * (self.__q - 1)
        self.e = self.__chooseE()
        self.__d = self.__egcd()
        print(f"The public key has the values \t\t(e={self.e}, n={self.n})")
        print(f"The private key has the values \t\t(d={self.__d}, n={self.n})")
        print("____________________________________________________________")


    def __chooseE(self):
        e = random.randrange(3, self.__phi)

        # Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = math.gcd(e, self.__phi)
        while g != 1:
            e = random.randrange(1, self.__phi)
            g = math.gcd(e, self.__phi)
        return e

    def __egcd(self):
        u, v, s, t = 1, 0, 0, 1
        a = self.e
        b = self.__phi
        while b != 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        if u < 0:
            u += self.__phi
        return u

    def encrypt(self, msg):
        return [pow(ord(char), self.e, self.n) for char in msg]
