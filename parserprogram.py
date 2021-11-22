# PROGRAM UTAMA PARSER

'''
Alur umum dari program yang akan dibangun adalah sebagai berikut.
    1. Menerima input berupa file eksternal berisi string yang merupakan kode sebuah program python
    2. Melakukan evaluasi sintaks dengan CFG
    3. Melakukan evaluasi nama-nama variabel yang ada dengan FA
    4. Memberikan keluaran hasil evaluasi program antara “Accepted” jika input diterima atau “Syntax Error” jika input tidak diterima
    5. (BONUS) Memberi tahu letak dan detail kesalahan syntax jika ada 
'''

import sys
from CFGtoCNF import CFGtoCNF
from CNFtoCNFdict import CNFtoCNFdict
from CYK import CYK
from FA import isVarValid

# KAMUS
listReservedNonTerminal = ['IF', 'ElSE']
stack = []
isValid = True
# ALGORITMA

'''1. Menerima input berupa file eksternal berisi string yang merupakan kode sebuah program python'''

nama_file = sys.argv[1]
with open(nama_file,"r") as f:
    data = f.read()

# input disimpan dalam var 'data'

'''2. Melakukan evaluasi sintaks dengan CFG'''
# melakukan print jika terjadi kesalahan. implementasi dari Stack terjadi disini.

# siap kan CFG hingga menjadi CNFdict
CFGtoCNF()
print("translating CFG to CNF...")
CNFdict = CNFtoCNFdict()
print("translating CNF to CNF dictionary...")

listDataLine = data.split("\n")
for eachListDataLine in listDataLine:
    # bersihkan tabulasi dan spasi
    eachListDataLine = eachListDataLine.lstrip().rstrip()
    # print(eachListDataLine)
    listTopCNF = CYK(eachListDataLine,CNFdict)

    # kalau di dalam listTopCNF itu gada S dan ada ReservedNonTerminal, brarti perlu tindakan khusus terhadap stack
    isSpecial = False
    adaS = False
    specialNonTerminal = ''
    for eachTopCNF in listTopCNF:
        if eachTopCNF == 'S':
            adaS = True
        else:
            for eachReservedNonTerminal in listReservedNonTerminal:
                if eachTopCNF == eachReservedNonTerminal:
                    specialNonTerminal = eachTopCNF
                    isSpecial = True
                    break
        if isSpecial or adaS:
            break
    
    if(isSpecial and not(adaS)):
        # kalo nge append, yang aku append cuman yg special. ini bakal trouble kalo suatu statement bisa menjadi 2 spesial yang berbeda(misal dia IF statement sekaligus ELSE, tapi dia bukan S), tapi keknya gk mungkin. jadi harusnya aman 
        if specialNonTerminal == 'IF':
            stack.append(specialNonTerminal)
        elif specialNonTerminal == 'ELSE':
            if stack[-1] == 'IF': # stack[-1] artinya top of stack.
                stack.pop()
            else:
                print("ada else tapi atasnya bukan if")
                isValid = False
        # if2 lainnya
    elif(not(isSpecial) and not(adaS)): # berarti ada baris yang gk valid
        isValid = False
        print("ada baris yang tidak valid:")
        print(eachListDataLine)
    # kalo udah ada baris yang gk valid, gk usah cek bawah2nya
    if not(isValid):
        break
# checking tiap line selesai. 

# bersihin stack, ada keyword yang gk perlu penutup (contoh IF)
while stack:
    if stack[-1] == 'IF':
        stack.pop()
    


# Stack harus kosong. kalau gk kosong berarti gk valid
if isValid:
    if stack: # jika semua line aman, tapi stack masih ada isinya
        print("stack tidak kosong.")
        print("ada ", stack[-1], "tanpa penutup")
    else:
        print("yay valid")