#!/usr/bin/python
import sys
from base64 import b64encode
from binascii import unhexlify

def hex2base64( hexstr ):
    "This function converts input hex to base64"
    byte = unhexlify(hexstr)
    base64 = b64encode(byte)
    return base64;

#main
hexstr = sys.argv[1]
base64 = hex2base64(hexstr)
print base64
