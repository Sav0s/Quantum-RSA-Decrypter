from Decrypt import IBMDecrypter, QSharpDecrypter, NumericDecrypter
from rsa import RSA

import argparse


def main():
    parser = argparse.ArgumentParser(description="Decrypt a rsa-encrypted message.")
    parser.add_argument("-o", "--option", type=str, required=True,
                        help="the way you want to decrypt the message. ibmq, qsharp or numeric")
    parser.add_argument("-k", "--keysize", type=int, required=False, help="the bitsize of the key for the numeric approach")
    args = parser.parse_args()

    message = "This message is encrypted"
    if args.option == "ibmq":
        rsa = RSA(15)
        cipher = rsa.encrypt(message)
        decrypter = IBMDecrypter()
    elif args.option == "qsharp":
        rsa = RSA(15)
        cipher = rsa.encrypt(message)
        decrypter = QSharpDecrypter()
    elif args.option == "numeric" and args.keysize != None:
        bits = args.keysize
        if bits % 2 != 0:
            exit(0)
        bits = int(bits / 2)
        rsa = RSA(bits)
        cipher = rsa.encrypt(message)
        decrypter = NumericDecrypter(rsa.n)
    else:
        print("Wrong Arguments")
        exit(0)

    print("_____Starting Brute Force_____")
    p, q = decrypter.factorize()

    print(f"Found factors: {p} and {q}")
    d = decrypter.calculateD(rsa.e, p, q)
    print("_____Reconstructed Private Key_____")
    print("_____Decrypting Message_____")
    reconstructedMessage = decrypter.decrypt(cipher, d)
    print(reconstructedMessage)


if __name__ == '__main__':
    main()
