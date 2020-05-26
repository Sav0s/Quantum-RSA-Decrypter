from Decrypt import IBMDecrypter
from rsa import RSA


def main():
    bits = 32
    if bits % 2 != 0:
        exit(0)
    bits = int(bits / 2)
    rsa = RSA(bits)
    message = "This message is encrypted"
    cipher = rsa.encrypt(message)
    decrypter = IBMDecrypter()

    print("_____Starting Brute Force_____")
    p, q = decrypter.factorize()

    print(f"Found factors: {p} and {q}")
    print("_____Reconstructed Private Key_____")
    d = decrypter.calculateD(rsa.e, rsa.phi)
    print(f"Found d: {d}")
    print("_____Decrypting Message_____")
    reconstructedMessage = rsa.decrypt(cipher)
    print(reconstructedMessage)


if __name__ == '__main__':
    main()
