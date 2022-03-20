import functools
from operator import xor

# print(hex(int("509310e65592b19ba50589ba2e333a4d7c3ea6390ae6075551221cd80c3c7d7f", 16) ^
#           int("  d2cf327a7e887b9091e16d7212766fadccc3ada53290c50351e70e3aa6188265", 16) ^
#           int("    9cef526bfe9b9a26ef01f6b2a9c694b794f377a63ee4c16ab4e41e4ecb0d5417", 16) ^
#           int("      761807dd4f58dee66eef7f66d8f8f9366183833206d7f3780723f57e07204297", 16) ^
#           int("        24dbc244026cbb149ca4cc95b6a8f9fca1dacb09297f67efd40e4e72fb07718f", 16) ^
#           int("          1581f02b97b462050c3a113a00782c36ad4134e24a273fef679886ff49e38277", 16)))

def str_hex_to_int(string):
    return int(string, 16)

def xor_list(iterable):
    iterable = tuple(map(str_hex_to_int, iterable))
    return hex(functools.reduce(lambda x, y: x ^ y, iterable))

def xor_1by1(iterable):
    iterable = tuple(zip(*tuple(map(list, iterable))))
    return "".join(tuple(elem[2] for elem in (tuple(xor_list(column) for column in iterable))))

def split_by_bytes(string):
    return [string[i:i+2] for i in range(0, len(string), 2)]

def decimal_result(iterable):
    return tuple(map(str_hex_to_int, split_by_bytes(xor_1by1(iterable))))[:len(iterable)]

def utf8_result(iterable):
    return "".join(map(chr, decimal_result(iterable)))



example = (
    "509310e65592b19ba50589ba2e333a4d7c3ea6390ae6075551221cd80c3c7d7f0000000000",
    "00d2cf327a7e887b9091e16d7212766fadccc3ada53290c50351e70e3aa618826500000000",
    "00009cef526bfe9b9a26ef01f6b2a9c694b794f377a63ee4c16ab4e41e4ecb0d5417000000",
    "000000761807dd4f58dee66eef7f66d8f8f9366183833206d7f3780723f57e072042970000",
    "0000000024dbc244026cbb149ca4cc95b6a8f9fca1dacb09297f67efd40e4e72fb07718f00",
    "00000000001581f02b97b462050c3a113a00782c36ad4134e24a273fef679886ff49e38277"
)

print(utf8_result(example))

def format_operation(iterable):
    for i in iterable:
        