'''
ada 4 step cara ngetranslate CFG to CNF
1. ilangin eplison
2. ilangin non terminal -> non terminal (cuman satu biji di sisi kanan)
3. ilangin variabel yg gabakal tercapai
4. bikin jadi 2 non terminal atau satu terminal di sisi kanan
'''
'''
CONTOH FILE
S -> S S | IF | var = VALUE | COMMENT | FUNCTION | e ;
COMMENT -> # string | '' string '' ;
FUNCTION -> def string ;
IF -> if BOOLEAN : S ELIF ELSE ;
ELIF -> elif BOOLEAN : S | ELIF ELIF | e ;
ELSE -> else : S | e ;
VALUE -> ( VALUE ) | MATH | string ;
BOOLEAN -> True | False | VARVAL EVALUATOR VARVAL | ( BOOLEAN ) | BOOLEAN or BOOLEAN | BOOLEAN and BOOLEAN | not BOOLEAN ;
VARVAL -> var | VALUE ;
EVALUATOR -> == | <= | < | > | >= | != ;
MATH -> angka | angka OPERATOR angka | ( angka ) ;
OPERATOR -> + | - | * | / | mod ;
'''

from os import path


def readCFG(file):
    # array nterminals menyimpan semua nonterminal
    nterminals = []

    # open file, file disimpan di variable data
    with open(file, "r") as f:
        data = f.read()

    data = data.split("\n")
    for i in range (len(data)):
        data[i] = data[i][0:-2]
        data[i] = data[i].split(" -> ")
        nterminals.append(data[i][0])
        data[i][1] = data[i][1].split(" | ")
        for j in range (len(data[i][1])):
            data[i][1][j] = data[i][1][j].split()

    # data yang di-return berbentuk array dalam array dalam array...
    return (data, nterminals)

def writeCNF(data, file):
    with open(file, "w") as f:
        for i in range(len(data)):
            f.write(f"{data[i][0]} -> ")
            for j in range(len(data[i][1])-1):
                for k in range(len(data[i][1][j])):
                    f.write(f"{data[i][1][j][k]} ")
                f.write("| ")
            for k in range(len(data[i][1][(len(data[i][1]))-1])):
                f.write(f"{data[i][1][(len(data[i][1]))-1][k]} ")
            f.write(";\n")

def splitToTwos(subProduction, count):
    # basis
    if len(subProduction) == 1:
        out = []
        out.append([f"A{count}", [[subProduction[0]]]])
        return out, count
    elif len(subProduction) == 2:
        out = []
        out.append([f"A{count}", [[subProduction[0],subProduction[1]]]])
        return out, count
    # rekurens
    else:
        temp = ([f"A{count}", [[subProduction[0],f"A{count+1}"]]])
        subProduction.pop(0)
        count += 1
        out, count = splitToTwos(subProduction, count)
        out.append(temp)
        return out, count

def CFGtoCNF(filein, fileout):
    # dict base_nulls untuk menyimpan semua basis null production
    # pemakaian base_nulls[x] = True (seperti himpunan)
    base_nulls = {}
    # dict nulls untuk menyimpan semua null production
    # pemakaian nulls[x] = True (seperti himpunan)
    nulls = {}
    # counter untuk memberi nama terminal baru
    t_i = 1 # khusus terminal
    v_i = 1 # yang lainnya
    # terminals untuk menampung isi txt
    terminals = {}
    # read file
    data, nterminals = readCFG(filein)
    # proses
    for i in range (len(data)):
        lhs = data[i][0]
        rhs = data[i][1]
        r = 0
        while (r<len(rhs)):
            subProduction = rhs[r]
            # null production
            if len(rhs) == 1 and subProduction==['e']: # basis, production rule tersebut hanya berisi epsilon
                base_nulls[lhs] = True
            elif ['e'] in rhs: # ada epsilon di production rule tersebut
                nulls[lhs] = True
                data[i][1].remove(['e'])

            for s in range (len(subProduction)):
                x = subProduction[s]
                # terminals
                try:
                    if terminals[x] and len(subProduction)>1:
                        data[i][1][r][s] = terminals[x][0]
                except:
                    if x not in nterminals and x != 'e':
                        terminals[x] = [f"T{t_i}"]
                        data.append([f"T{t_i}", [[x]]])
                        t_i += 1
                        if len(subProduction)>1:
                            data[i][1][r][s] = terminals[x][0]
                
                # di sini semua terminal sudah didata ke dict terminals dan yang memakainya sudah diganti dengan var bersangkutan
                
            if len(subProduction) > 2:
                # split to twos
                base = v_i
                additions, v_i = splitToTwos(subProduction, v_i)
                data[i][1][r] = [f"A{base}"]
                for adds in additions:
                    data.append(adds)

            for s in range (len(subProduction)):
                x = subProduction[s]
                # handle epsilon production
                try:
                    if nulls[x]:
                        subProductionAdd = subProduction.pop(x)
                        data[i][1].append(subProductionAdd)
                except:
                    pass
            
            r += 1

    # Output
    i = 0
    while (i<len(data)):
        lhs = data[i][0]
        rhs = data[i][1]
        try:
            # remove base nulls
            if base_nulls[lhs]:
                data.pop(i)
                i -= 1
        except:
            pass
        for r in range (len(rhs)):
            subProduction = rhs[r]
            # unit production
            if len(subProduction) == 1:
                print("")
            # handle epsilon productions
            for s in range (len(subProduction)):
                x = subProduction[s]
                try:
                    if nulls[x]:
                        temp = subProduction.copy()
                        temp.pop(s)
                        if temp != [lhs]:
                            data[i][1].append(temp)
                except:
                    pass

            trash = False
            for s in range (len(subProduction)):
                x = subProduction[s]
                try:
                    if base_nulls[x]:
                        trash = True
                        break
                except:
                    pass
            
            if trash:
                data[i][1].pop(r)
            if data[i][1] == []:
                data.pop(i)
                i -= 1
        i += 1
        
    print(data)

    print(base_nulls)
    print(nulls)
    print(terminals)
    writeCNF(data, fileout)

CFGtoCNF("try.txt", "hey.txt")