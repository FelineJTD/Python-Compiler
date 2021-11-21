#  sebuah fungsi yang menerima sebuah string yang akan di evaluasi menurut CNFdict.
# mengembalikan isi dari array teratas. Array tersebut seharusnya berisi sekumpulan string of nonterminal
from CNFtoCNFdict import CNFtoCNFdict
def CYK(word, Rules):
    # Dari referensi geeks for geeks
    # Untuk ukuran tabel CYK
    n = len(word)
    # Inisialisasi tabel CYK
    TabelCYK = [[set([]) for j in range(n)] for i in range(n)]
    # Isi tabel diagonal dulu, disini i sebagai kolom dan j sebagai baris
    for i in range(n):
        # Kita append ke TabelCYK[i][i]
        if word[i] in Rules.keys():
            TabelCYK[i][i].update(Rules[word[i]])
        # Kalo i > 0 baru cek pohon bawah nya
        if i > 0:
            # pasti di-iterate i kali, iterate mundur biar indexing lebih enak
            for j in range(i - 1, -1, -1):
                # di loop lagi buat nyari atasnya diagonal utama
                l = j + 1 # Jadi ntar algo nya kaya nyari selang seling, misal 6 huruf, jadi 1 5, 2 4, 3 3, 4 2, 5 1
                for k in range(j, i): # buat ngeloop semua possibilty jumlah huruf
                    # Loop lagi per non terminal di dalem set buat semua kemungkinan susunan non terminalnya
                    for NT in TabelCYK[j][k]:
                        for NT2 in TabelCYK[l][i]:
                            if NT + NT2 in Rules.keys():
                                if NT != "" and NT2 != "":
                                    TabelCYK[j][i].update(Rules[NT + NT2])
                    l = l + 1
    return TabelCYK

Rule = {'EI': 'E', 'RG': ['F', 'T', 'E'], 'a': ['F', 'T', 'E'], 'TH': ['T', 'E'], 'EO': 'G', 'QF': 'H', 'PT': 'I', '*': 'Q', '(': 'R', ')': 'O', '+': 'P'}
print(Rule)
# print("a" in Rule.keys())
tabel = CYK("a*(a+a)", Rule)
for row in tabel:
    print(row, end="\n")
# for a in tabel[0][0]:
#     for b in tabel[1][1]:
#         print(a)
# print(CYK("makanan bakso", {"S" : "a"}))
# elemen set di python engga bisa subscript tp iterable
# set1 = [set([]) for i in range(10)]
# set1[0].add(1)
# print(set1)
