def ascii2hex(astring):
    """converts ascii string to hex string"""
    str_bytes = astring.encode('ASCII')
    str_int = int.from_bytes(str_bytes, byteorder='big')
    hex_str = hex(str_int)
    return hex_str[2:]


def hex2ascii(hex_str):
    """converts hex_str to ascii string"""
    #get bytes (chars)
    char_array = [
        int(hex_str[2 * i:2 * i + 2],16) for i in range(0, int(len(hex_str) / 2))
    ]
    astring = ''.join([chr(char) for char in char_array])
    return astring
