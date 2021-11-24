#  sebuah fungsi yang menerima sebuah string yang akan di evaluasi menurut CNFdict.
# mengembalikan isi dari array teratas. Array tersebut seharusnya berisi sekumpulan string of nonterminal
from CNFtoCNFdict import CNFtoCNFdict
import re

from FA import isVarValid

def isString(kata):
    matched = re.match(r'[\x00-\x7F]*', kata)
    return bool(matched)
    
def isNumber(angka):
    matched = re.match('^[0-9]+$', angka)
    return bool(matched)

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
        if(isString(word[i])):
    
            TabelCYK[i][i].update(Rules['string'])
        if(isNumber(word[i])):
          
            TabelCYK[i][i].update(Rules['angka'])
        if(isVarValid(word[i])):
       
            TabelCYK[i][i].update(Rules['variable'])
    
            
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
                            # print('possible keys', NT + NT2)
                            if NT + NT2 in Rules.keys():
                                # print("hadir")
                                if NT != "" and NT2 != "":
                                    # print('update', NT + NT2)
                                    # print(Rules[NT + NT2])
                                    TabelCYK[j][i].update(Rules[NT + NT2])
                                    # print(TabelCYK[j][i])
                    l = l + 1
        # print("baris ke - ", i)
        # print(TabelCYK[i])
    # print("-=====================-")
    # for eachrow in TabelCYK:
    #     print(eachrow)
    # print("n-1 = ",n-1)
    return TabelCYK[0][n-1]