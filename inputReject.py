# file yang digunakan untuk testing. berisi kode python yang tidak valid

def isString(kata):
    matched = re.match(r'[\x00-\x7F]*', kata)
    return bool(matched)
def isNumber(angka):
    matched = re.match('^[0-9]+$', angka)
    return bool(matched)
# def CYK(word, Rules):
#     n = len(word)
#     TabelCYK = [[set([]) for j in range(n)] for i in range(n)]
# def do_something(x):
#     ''' This is a sample multiline comment
#     '''
#     x + 2 = 3
#     if x == 0 + 1
#         return 0
#     elif x + 4 == 1:
#         else:
#             return 2
#     elif x == 32:
#         return 4
#     else:
#         return "Doodoo"