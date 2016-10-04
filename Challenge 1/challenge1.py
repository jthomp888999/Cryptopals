#! /usr/bin/env python

import sys, binascii

string = sys.argv[1]
def converter():
    hex = string.decode("hex")
    b64 = binascii.b2a_base64(hex)
    print("\n\n")
    return b64
