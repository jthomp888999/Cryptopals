#!/usr/bin/env python

import binascii
from Crypto.Util.strxor import strxor


string = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"

# Simply XOR's provided string with provided key
def fixed_XOR(s,k):
    s = binascii.unhexlify(string)
    k = binascii.unhexlify(key)
    answer = strxor(s, k)
    return answer

result = fixed_XOR(string, key)
print result
