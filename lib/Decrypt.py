import qsharp
import sys

from Microsoft.Quantum.Samples.IntegerFactorization import FactorInteger
from qiskit import IBMQ, BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

import acount


class Decrypter:
    def __init__(self, factor):
        keySize = len("{0:b}".format(factor))
        self.a = 1
        print(f"Message was encrypted with a key size of {keySize} Bits")

    def factorize(self, factor):
        pass

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


class NumericDecrypter(Decrypter):
    def __init__(self, factor=15):
        self.factor = factor
        super(NumericDecrypter, self).__init__(factor)

    def factorize(self):
        result = list()
        for i in range(2, self.factor):
            if self.factor % i == 0:
                result.append(i)
            if i % 1000 == 2:
                printProgress(i, self.factor)
            if len(result) == 2:
                break
        print("\n")
        return result[0], result[1]


class IBMDecrypter(Decrypter):
    def __init__(self, factor=15):
        self.factor = factor
        super(IBMDecrypter, self).__init__(factor)

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


class QSharpDecrypter(Decrypter):
    def __init__(self, factor=15):
        self.factor = factor
        super(QSharpDecrypter, self).__init__(factor)

    def factorize(self):
        output = FactorInteger.simulate(
            number=self.factor,
            useRobustPhaseEstimation=10,
            raise_on_stderr=True)
        return output


def printProgress(iteration, total):
    sys.stdout.write('\r|---Tried %s from %s possibilties---|' % (iteration, total))
    sys.stdout.flush()
