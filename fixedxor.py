from binascii import unhexlify


#main
def main():
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'
    c = xor(a, b)
    print(c)


def xor(a, b):
    """Return xor string of inputs a,b"""
    a = int(a, 16)
    b = int(b, 16)
    c = a ^ b
    c = hex(c)
    return c[2:]


if __name__ == "__main__":
    main()
