import sys

from qiskit import IBMQ, BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

from python import acount


class Decrypter:
    def __index__(self):
        self.a = 1

    def calculateD(self, e, phi):
        a, d, k = self._extgcd(e, phi)
        if d < 0:
            d += phi
        return d

    def _extgcd(self, a, b):
        u, v, s, t = 1, 0, 0, 1
        while b != 0:
            q = a // b
            a, b = b, a - q * b
            u, s = s, u - q * s
            v, t = t, v - q * t
        return a, u, v

    def factorize(self, factor):
        pass


class NumericDecrypter(Decrypter):
    def factorize(self, factor):
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


class IBMDecrypter(Decrypter):
    def factorize(self, factor=15):
        IBMQ.delete_account()
        IBMQ.save_account(acount.token)
        IBMQ.load_account()
        shor = Shor(factor)

        # If you use get_backend('qasm_simulator') don't factor numbers greater than 15, it lasts nearly forever
        backend = BasicAer.get_backend('qasm_simulator')
        quantum_instance = QuantumInstance(backend, shots=4)
        computation = shor.run(quantum_instance)
        result = computation['factors'][0]
        return result[0], result[1]


def printProgress(iteration, total):
    sys.stdout.write('\r|---Tried %s from %s possibilties---|' % (iteration, total))
    sys.stdout.flush()
