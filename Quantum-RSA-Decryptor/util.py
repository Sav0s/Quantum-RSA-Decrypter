import sys
import math
import Crypto.Random
import Crypto.Util.number

def printProgress(iteration, total):
    sys.stdout.write('\r|---Tried %s from %s possibilties---|' % (iteration, round(math.sqrt(total))))
    sys.stdout.flush()

def decrypt(cipher, d, n):
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

def encrypt(msg, e, n):
    return [pow(ord(char), e, n) for char in msg]


def mod_inverse(e, phi):

	# See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
	def eea(a,b):
		if b==0:return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = eea(b,r)
		return (t, s-(q*t) )

	inv = eea(e,phi)[0]
	if inv < 1: inv += phi # we only want positive values
	return inv

def parseDefaultFactor(factor):
    if factor == None:
        return 15
    else: 
        return factor