import math
import random

import Crypto.Random
import Crypto.Util.number
from util import mod_inverse


class RSA:
    def __init__(self, bits=None, factor=15):
        if bits != None:
            primfactorBit = int(bits / 2)
            self.__p = Crypto.Util.number.getPrime(primfactorBit, randfunc=Crypto.Random.get_random_bytes)
            self.__q = Crypto.Util.number.getPrime(primfactorBit, randfunc=Crypto.Random.get_random_bytes)
            self.n = self.__p * self.__q
        elif factor == 15:
            self.n = 15
            self.__p = 3
            self.__q = 5
        elif factor == 21:
            self.n = 21
            self.__p = 3
            self.__q = 7
        elif factor == 33:
            self.n = 33
            self.__p = 3
            self.__q = 11
        elif factor == 35:
            self.n = 35
            self.__p = 7
            self.__q = 5
        elif factor == 39:
            self.n = 39
            self.__p = 13
            self.__q = 3
        elif factor == 51:
            self.n = 51
            self.__p = 17
            self.__q = 3
        elif factor == 55: 
            self.n = 55
            self.__p = 5
            self.__q = 11
        else:
            self.n = 65
            self.__p = 5
            self.__q = 13
            
        self.__phi = (self.__p - 1) * (self.__q - 1)
        self.e = self.__chooseE()
        self.__d = mod_inverse(self.e, self.__phi)
        print(f"The public key has the values \t\t(e={self.e}, n={self.n})")
        print(f"The primefactors of our n are {self.__p} and {self.__q}")
        # print(f"The private key has the values \t\t(d={self.__d}, n={self.n})")
        print("____________________________________________________________")


    def __chooseE(self):
        #Choose an integer e such that e and phi(n) are coprime 
        e = random.randrange(2, self.__phi)

        #Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = math.gcd(e, self.__phi)
        while g != 1:
            e = random.randrange(2, self.__phi)
            g = math.gcd(e, self.__phi)

        return e