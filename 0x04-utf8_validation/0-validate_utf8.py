#!/usr/bin/python3
"""A program thet checks if a given sequence of bits is a valid utf8
"""


def validUTF8(data):
    """A program thet checks if a given sequence of bits is a valid utf8
    """
    i = 0
    invalid_bytes = set((0xc0, 0xc1, 0xf5, 0xff))

    for d in data:
        byte = d & 0xff
        if byte in invalid_bytes:
            return False

    while i < len(data):
        byte = data[i] & 0xff
        if byte >> 0x7 == 0:
            pass
        elif byte >> 0x5 == 0x6:
            i += 1
            if len(data[i:]) < 1 or (data[i] & 0xff) >> 0x6 != 2:
                return False
        elif byte >> 0x4 == 0xe:
            i += 2
            if (len(data[i - 1:]) < 2
                or (data[i - 1] & 0xff) >> 0x6 != 0x2
                    or (data[i] & 0xff) >> 0x6 != 0x2):
                return False
        elif byte >> 0x3 == 0x1e:
            i += 3
            if (len(data[i - 2:]) < 3
                or (data[i - 2] & 0xff) >> 0x6 != 0x2
                or (data[i - 1] & 0xff) >> 0x6 != 0x2
                    or (data[i] & 0xff) >> 0x6 != 0x2):
                return False
        else:
            return False
        i += 1
    return True
