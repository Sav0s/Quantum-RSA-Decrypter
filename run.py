from qiskit import IBMQ

from Decrypt import IBMDecrypter, QSharpDecrypter, NumericDecrypter, IBMDecrypterReal
from rsa import RSA

import argparse


def main():
    parser = argparse.ArgumentParser(description="Decrypt a rsa-encrypted message.")
    parser.add_argument("-o", "--option", type=str, required=True,
                        help="the way you want to decrypt the message. ibmq, qsharp or numeric")
    parser.add_argument("-k", "--keysize", type=int, required=False, help="the bitsize of the key for the numeric approach")
    args = parser.parse_args()

    if args.option == "ibmq":
        rsa = RSA(n=15)
        decrypter = IBMDecrypter(rsa.n)
    elif args.option == "ibmqreal":
        rsa = RSA(n=15)
        decrypter = IBMDecrypterReal(rsa.n)
    elif args.option == "qsharp":
        rsa = RSA(n=33)
        decrypter = QSharpDecrypter(rsa.n)
    elif args.option == "numeric" and args.keysize != None:
        bits = args.keysize
        if bits % 2 != 0:
            print("Please provide an even keysize")
            exit(0)
        bits = int(bits / 2)
        rsa = RSA(bits=bits)
        decrypter = NumericDecrypter(rsa.n)
    else:
        print("Wrong Arguments")
        exit(0)

    print("_____Starting Integer Factorization_____")
    p, q = decrypter.factorize()
    print("_____Found factors!_____")
    print(f"The two factors are: {p} and {q}")

    phi = (p - 1) * (q - 1)
    d = decrypter.calculateD(rsa.e, phi)
    # print(f"The regenerated private key has the value\t(d={d}, {rsa.n})")


if __name__ == '__main__':
    main()
