#!/usr/bin/python3
"""Method validUTF8"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""
    num_bytes = 0
    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            while (1 << (7 - num_bytes)) & byte:
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False

        num_bytes -= 1
    return num_bytes == 0
