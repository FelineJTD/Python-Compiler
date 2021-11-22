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
from tokenizer import tokenizer

# KAMUS
listReservedNonTerminal = ['IF', 'ELSE', 'ELIF', 'DEF', 'CLASS', 'FOR', 'WHILE', 'BREAK', 'PASS', 'CONTINUE', 'RETURN', 'TRIPLEDOUBLEQUOTEOPEN','TRIPLEDOUBLEQUOTECLOSE', 'TRIPLESINGLEQUOTEOPEN', 'TIPLESINGLEQUOTECLOSE']
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
print("translating CFG to CNF...")
CFGtoCNF("cfgadit.txt")
print("berhasil menulis di cnf.txt")    
print("translating CNF to CNF dictionary...")
CNFdict = CNFtoCNFdict()
print("CNFdict")
# for keys in CNFdict.keys():
#     print(keys,":", CNFdict[keys])
print("berhasil melakukan translasi menjadi CNFdict")
listDataLine = data.split("\n")
baris = 0
for eachListDataLine in listDataLine:
    baris += 1
    prevIsS = False
    # bersihkan tabulasi dan spasi
    eachListDataLine = eachListDataLine.lstrip().rstrip()
    # print("eachListDataLine")
    # print(eachListDataLine)
    if(eachListDataLine != ""):
        tokenizedLine = tokenizer(eachListDataLine)
        print("===========================")
        print("BARIS ",baris)
        print('tokenized = ',tokenizedLine)
        listTopCNF = CYK(tokenizedLine,CNFdict)

        # kalau di dalam listTopCNF itu gada S dan ada ReservedNonTerminal, brarti perlu tindakan khusus terhadap stack
        isSpecial = False
        adaS = False
        specialNonTerminal = ''
        # untuk mencatat apakkah sebelumnya sudah ada Statement. untuk menghandle 'if diikuti else tapi belom ada statement, atau def tanpa statement
        print("listTopCNF = ", listTopCNF)
        for eachTopCNF in listTopCNF:
            if eachTopCNF == 'S':
                adaS = True
                prevIsS = True
            else:
                for eachReservedNonTerminal in listReservedNonTerminal:
                    # print("eachReservedNonTerminal")
                    # print(eachReservedNonTerminal)
                    if eachTopCNF == eachReservedNonTerminal:
                        # kasus khusus, hopefully doesnt kick my ass later
                        if 'TRIPLEDOUBLEQUOTECLOSE' in listTopCNF:
                            specialNonTerminal = 'TRIPLEDOUBLEQUOTECLOSE'
                        elif 'TRIPLESINGLEQUOTECLOSE' in listTopCNF:
                            specialNonTerminal = 'TRIPLESINGLEQUOTECLOSE'
                        else:
                            specialNonTerminal = eachTopCNF
                        isSpecial = True
                        break
            if isSpecial or adaS:
                break
        
        if(isSpecial and not(adaS)):
            # kalo nge append, yang aku append cuman yg special. ini bakal trouble kalo suatu statement bisa menjadi 2 spesial yang berbeda(misal dia IF statement sekaligus ELSE, tapi dia bukan S), tapi keknya gk mungkin. jadi harusnya aman 
            print("specialNonTerminal = ", specialNonTerminal)
            # ['IF', 'ELSE', 'ELIF', 'DEF', 'CLASS', 'FOR', 'WHILE', 'BREAK', 'PASS', 'CONTINUE', 'RETURN', 'TRIPLEDOUBLEQUOTEOPEN','TRIPLEDOUBLEQUOTECLOSE', 'TRIPLESINGLEQUOTEOPEN', 'TIPLESINGLEQUOTECLOSE']
            if specialNonTerminal == 'IF':
                stack.append(specialNonTerminal)
            elif specialNonTerminal == 'ELSE':
                if (len(stack) != 0 and stack[-1] == 'IF'): # stack[-1] artinya top of stack.
                    stack.pop()
                else:
                    print("ada else tapi atasnya bukan if")
                    isValid = False
            elif specialNonTerminal == 'ELIF':
                if not(len(stack) != 0 and stack[-1] == 'IF'): # stack[-1] artinya top of stack.
                    print("ada elif tanpa if")
                    isValid = False
            elif specialNonTerminal == 'DEF':
                stack.append(specialNonTerminal)
            elif specialNonTerminal == 'CLASS':
                stack.append(specialNonTerminal)
            elif specialNonTerminal == 'FOR':
                stack.append(specialNonTerminal)
            elif specialNonTerminal == 'WHILE':
                stack.append(specialNonTerminal)
            elif specialNonTerminal == 'BREAK':
                pass
            elif specialNonTerminal == 'PASS':
                pass
            elif specialNonTerminal == 'CONTINUE':
                pass
            elif specialNonTerminal == 'RETURN':
                if (len(stack) != 0 and stack[-1] == 'DEF'):
                    stack.pop()
                elif(len(stack) != 0 and 'DEF' in stack):
                    pass
                else:
                    isValid = False
            elif specialNonTerminal == 'TRIPLEDOUBLEQUOTECLOSE':
                if (len(stack) != 0 and stack[-1] == 'TRIPLEDOUBLEQUOTEOPEN'):
                    stack.pop()
                else:
                    isValid = False
            elif specialNonTerminal == 'TRIPLEDOUBLEQUOTEOPEN':
                stack.append(specialNonTerminal)
            elif specialNonTerminal == 'TRIPLESINGLEQUOTECLOSE':
                if (len(stack) != 0 and stack[-1] == 'TRIPLESINGLEQUOTEOPEN'):
                    stack.pop()
                else:
                    isValid = False
            elif specialNonTerminal == 'TRIPLESINGLEQUOTEOPEN':
                stack.append(specialNonTerminal)
                
            
        elif(not(isSpecial) and not(adaS)): # berarti ada baris yang gk valid
            isValid = False
            # print("ada baris yang tidak valid:")
            # print(eachListDataLine)
        # kalo udah ada baris yang gk valid, gk usah cek bawah2nya
        if not(isValid):
            print("\n!!!!! NOT VALID !!!!!\n")
            print("baris yang dicurigai")
            print(eachListDataLine)
            break
# checking tiap line selesai. 

# bersihin stack, ada keyword yang gk perlu penutup (contoh IF)
print("KONDISI STACK DIAKHIR PROGRAM")
print(stack)
# while stack:
#     if stack[-1] == 'IF':
#         stack.pop()
#     # if2 lainnya
    


# Stack harus kosong. kalau gk kosong berarti gk valid
# if isValid:
#     if stack: # jika semua line aman, tapi stack masih ada isinya
#         print("stack tidak kosong.")
#         print("ada ", stack[-1], "tanpa penutup")
#     else:
#         print("yay valid")