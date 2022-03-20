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
    return "".join(tuple(elem[2:] for elem in (tuple(xor_list(column) for column in iterable))))


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


hash_list = ['4dcd61730129ba48ad4b7b62d773c4c5c1160f84f606cbc428d0a949600f18c1',
            'a206401ee2eb57e887896979e9a8612134ce614d59ee0137b1f4640d7703b13b',
            '0e5b565d08271ff3991a8f39a7e6a4f3e7a3f7afa86575d190abb42060dde89c',
            '443b222cec6715d0b0846463e330d18fcd18f73a0f33b28a6c09fd8df9cae1c3',
            '522c001c3a18fcf5e7eaea4e50a0dbb5980e544d400e2424a6efeb276a5b6ec0',
            'cba6022e423e8d18ae5061842ac44774030b4dc9556eb11a2e5f796724856df3', 'b2957a9942f4f247e2cbf3bda11731c038f7f482946e7b67af25336fc1da116d', '2b13dc9e46da658a07c6ed10dad1da7a414149a7bf57e948a722ef6e8d616e2b', '2fc5f8a6a6f9e08b559b4f117f45bab170a265abd3643e7bd3c5d22fb39b782a', '832a3ed4cd512b59eeeb431f2ba344450d4315d38f435f2185b171cad6cc4103', '1f21e88145e697a72486c12cda8c2535ee765bd5ed6197bc5f1c0eb28b7aef11', 'bbefc592ee6f11552a190b2451c4a078bd2277938db9db788dd2ee4efec156b7', '2b13dc9e46da658a07c6ed10dad1da7a414149a7bf57e948a722ef6e8d616e2b', 'e281489c849f50c74ffbe5bfef05193726c3c6e863c91bd3edf9aeb4ff161ec0', '2b13dc9e46da658a07c6ed10dad1da7a414149a7bf57e948a722ef6e8d616e2b', '4a1c445e06c1f70d54a801a046d6ac3871c788f1244b491ff662aca5f62d011d', '5b0c09204bcb50fe8add9bbe55f9affac3a9e7cf9cf18f0baa5d3896fd0b04c8', 'e7f716fd222fa0ccaa425d30286120a8d954e36d71b69de4ca8b7aa8fd06c7c7', 'a74690cd1cb1ff2218735f4d0257989b8dda95e4d3b12b12fa1c7e71bf81cfd5', '59297a7ab95cad20e906fc04d568ac3f515c3df2e2e242752065063a186aac88', 'e5ee26aabcdba33e9e57433d1e55894bd399dd62298245016aec6e610adf91b1', '6e1eb7c639b61a6e1c8a73a13f5d06dd2093015935f04729c456d39b9b898074', '500d2a1ff7d64fe8912cba308beed2a1b757952c966b7205955a578eb988df65', '74215b983a39e5973da8649c3ca906380be8c02d22b04f526617d7e1ec43416f', '60af87bd4cd5cd2af83480919bfae24025224436b11c4d2d0c791c36702560c4', '56a06c2877da74cc42a37d5b09beb8880e945c194a4e00b9225c0565591d9191', 'f1c28eddcdcb8ead118f92b1945f0ddab609349b80e9e7b66793f4dc3c79c4d5', 'ec796976ae5bc99b0d5a15eb26d5fa514c8957d2932eb6b36d4ac57a14ea937a', '03a1a49860b5251ec20b9eb4582b2dad1dcc030c064cc9bc9cfa16e8c3ff0e81', 'f1c28eddcdcb8ead118f92b1945f0ddab609349b80e9e7b66793f4dc3c79c4d5',
             'fd832479530c4051cad11a21103633bf77e4268afd60431eb46b300052a460ec', '982611d60caf818d7e45db172a55bfd035265631495abcbef0e6a2fa193c0add', '04e6e0656e94a834b35b1c87ece50784ada40bacf005a5ac3d7c041fdd5e2204', '46b8a2da1948127d23ca39edf8ef16dcfd2deddd25c4696dcc84b2ab5dc74475', 'd5383da4e22fa34b11cd1d505bb282198753ba26eb6474b214d85cb029cd5a68', '5f0434de12894281b05997de169da93e6cbb6716d34956e256efd86873da2da5', 'db5f12b6995c83983b403ae84d9053a7e8942dfaa934710fec08aac94417179e', '2b13dc9e46da658a07c6ed10dad1da7a414149a7bf57e948a722ef6e8d616e2b', 'f739e749dff91120cc4716822949d7bb9c43040db1f74ad26df810f6cd295518', '249e2cd9b4c822549ea17ec091fbc6a9059d1feac9c369a3d4ce9ea6badb6989', '6a037778ae517e1de4be7558cfaa3833e2b6240299aab6c287c2c1d51f51815f', 'f0d10c7736d6a01c62cf86e82b1d35c05e6ce3cb2e813a8a653f0dde0788391c', '1bdac9336b3de87c8ac7f40ba0299bf139df62bc819ef0d999fa75c27df5614b', '009c179817938a6c8281a4cf6bc84497256e73c91910e4a6330545e4cef60578', '6a037778ae517e1de4be7558cfaa3833e2b6240299aab6c287c2c1d51f51815f', 'c5d192ffd292ce622875ec9508b85cefcdc549d12d98c2be971966b7218e7e14', '58706dcc2ec43bbc4c59e028dda6ca47acc41ab4e3693b1fad8838aa6bebea93', '7805d1e60f28439bcf4ffc1dfb98161ab97d168b9f53a6e64227cad85c5ea067', '4c43e28dcbf0177f6d34ed63a2479dd93f566e58c9ad49830c920a04546acbd4', 'f4adc8e6b540ac860818671308fb3b84d4105d49a22c1453a4ee4359a3bcff13', '06e9d7d395b9f8e2b6634650cd6bf6c85a9032c44ac3b626db814779522928b3', '6cbfaf23f6db57c1206642d3f2f9df76d615fe2de1e239950729ef7c27de0f0a', '40deba11125f6e7f1443089544e473ecfc1c9700d3d13b503c14039e557ffaae', '477648ae7cc7902193d7c76546a6fed8ba4c627972619613d228d7b9e29a0b43', 'cf9ac26bc95d0af4ca557f6fc4affb462c3933db1321e8a851715a1027d06327', '623a55f06b97d75b7f64d67cc978ef918f617a7bb8a14555093e6630afdd4890', 'e9f92ff7d7c909dcbc9705f5c85179a87d296f7f420b662e77fb92d52d96de10', 'cd382e41809c268943e0a6b3b8c75513254875a779a1026c9302b77d8e09a1ee', '63b37af451998e4b2b875c19ded66fe644c1660e4d11d96a5645dd86a8f0fd47', 'fe4ebcaca35f0957fe39eb5d96984234a824e57e86b20513b76994297e29d2fd', 'da6f7058c2cc0231ef79114eebb78cec4ce7f67817263febf5002892d8b7d2ab']


def format_operation(iterable):
    for i, elem in enumerate(iterable):
        iterable[i] = 2 * i * "0" + elem + 2 * (len(iterable) - i - 1) * "0"
    return iterable

print(utf8_result(format_operation(hash_list)))