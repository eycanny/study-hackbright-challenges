def dec2bin(num):
    """Convert a decimal number to binary representation."""

    import math
    
    binary = ""

    i = int(math.log2(num))

    while i > -1:
        if num >= 2 ** i:
            binary = binary + "1"
            num = num - (2 ** i)
        else:
            if "1" in binary:
                binary = binary + "0"
        
        i = i - 1

    return binary
