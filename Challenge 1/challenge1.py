#! /usr/bin/env python

import sys, binascii

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
def converter():
    hex = string.decode("hex")
    b64 = binascii.b2a_base64(hex)
    return b64
result = converter()
result = result.rstrip('\n')
if result == answer:
    print 'yes'
else:
    print 'no'