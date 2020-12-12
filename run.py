from qiskit import IBMQ

from Decrypt import IBMDecryptor, QSharpDecryptor, NumericDecryptor, IBMDecryptorReal
from rsa import RSA
from util import mod_inverse, parseDefaultFactor

import argparse


def main():
    parser = argparse.ArgumentParser(description="Decrypt a rsa-encrypted message.")
    parser.add_argument("-o", "--option", type=str, required=True,
                        help="the way you want to decrypt the message. ibmq, qsharp or numeric")
    parser.add_argument("-k", "--keysize", type=int, required=False, help="the bitsize of the key for the numeric approach")
    parser.add_argument("-f", "--factor", type=int, required=False, help="the factor for the integer factorization")
    args = parser.parse_args()

    if args.option == "ibmq":
        factor = parseDefaultFactor(args.factor)
        rsa = RSA(factor = factor)
        decryptor = IBMDecryptor(rsa.n)
    elif args.option == "ibmqreal":
        factor = parseDefaultFactor(args.factor)
        rsa = RSA(factor = factor)
        decryptor = IBMDecryptorReal(rsa.n)
    elif args.option == "qsharp":
        factor = parseDefaultFactor(args.factor)
        rsa = RSA(factor = factor)
        decryptor = QSharpDecryptor(rsa.n)
    elif args.option == "numeric" and args.keysize != None:
        bits = args.keysize
        if bits % 2 != 0:
            print("Please provide an even keysize")
            exit(0)
        bits = int(bits / 2)
        rsa = RSA(bits=bits)
        decryptor = NumericDecryptor(rsa.n)
    else:
        print("Wrong Arguments")
        exit(0)

    print("_____Starting Integer Factorization_____")
    p, q = decryptor.factorize()
    print("_____Found factors!_____")
    print(f"The two factors are: {p} and {q}")

    phi = (p - 1) * (q - 1)
    d = mod_inverse(rsa.e, phi)
    print(f"The regenerated private key has the value\t(d={d}, {rsa.n})")


if __name__ == '__main__':
    main()
