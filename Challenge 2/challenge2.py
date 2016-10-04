import sys, binascii
from Crypto.Util.strxor import strxor


string = sys.argv[1]
key = "686974207468652062756c6c277320657965"

def fixed_XOR():
    s = binascii.unhexlify(string)
    k = binascii.unhexlify(key)
    answer = strxor(s, k)
    print("\n\n")
    return answer

