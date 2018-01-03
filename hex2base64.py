#!/usr/bin/python3
import sys
from base64 import b64encode
from binascii import unhexlify


def hex2base64(hexstr):
    "This function converts input hex string to base64"
    "It returns a string of the base64 representation"
    byte = unhexlify(hexstr)
    base64 = b64encode(byte).decode()
    return base64


#main
hexstr = sys.argv[1]
base64 = hex2base64(hexstr)
print(base64)
print(type(base64))
