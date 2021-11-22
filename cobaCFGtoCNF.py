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

def readCFG(file):
    # array terminal menyimpan semua terminal
    terminals = []

    # open file, file disimpan di variable data
    with open(file, "r") as f:
        data = f.read()

    data = data.split("\n")
    for i in range (len(data)):
        data[i] = data[i][0:-2]
        print(data[i])
        data[i] = data[i].split(" -> ")
        terminals.append(data[i][0])

    return (data, terminals)

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
    # out untuk menampung isi txt
    out = {}
    # read file
    data, terminals = readCFG(filein)
    # proses
    for i in range (len(data)):
        lhs = data[i][0]
        rhs = data[i][1]
        rhs = rhs.split(" | ")
        r = 0
        for subProduction in rhs:
            # null production
            if len(rhs) == 1 and subProduction=='e': # basis, production rule tersebut hanya berisi epsilon
                base_nulls[lhs] = True
            elif 'e' in rhs: # ada epsilon di production rule tersebut
                nulls[lhs] = True

            subProductionTemp = subProduction.split()
            s = 1
            for each in subProductionTemp:
                # nonterminals
                try:
                    if (out[each] == True):
                        each = data[i][1].replace(f" {each} ", f" {out[each][0]} ")
                except:
                    if each not in terminals and each != ' e ' and each not in out.keys():
                        out[each] = [f"T{t_i}"]
                        t_i += 1
                        data[i][1] = data[i][1].replace(f" {each} ", f" {out[each][0]} ")
                # di sini semua nonterminal sudah didata ke dict out dan yang memakainya sudah diganti dengan var bersangkutan
                
                each = each.split()
                # unit production
                if len(each) == 1:
                    print('unit')
                elif len(each) > 2:
                    print('f')
                
                s += 1

            for each in subProductionTemp:
                # handle epsilon production
                if each in nulls:
                    subProduction = subProduction.replace(f" {each} ", "")
                    data[i][1] += f" | {subProduction}"
            
            r += 1

    # Output
    for i in range (len(data)-1):
        lhs = data[i][0]
        rhs = data[i][1]
        rhs = rhs.split(" | ")
        for subProduction in rhs:
            temp = subProduction.split()
            # handle epsilon productions
            trash = False
            for j in temp:
                if j in base_nulls:
                    trash = True
                    break
            
            if not trash:
                try:
                    out[subProduction].append(lhs)
                except:
                    out[subProduction] = [lhs]
        
    print(data)

    print(base_nulls)
    print(nulls)
    print(out)



CFGtoCNF("cfg.txt", "")