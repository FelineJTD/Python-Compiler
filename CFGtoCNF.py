'''
ada 4 step cara ngetranslate CFG to CNF
1. ilangin eplison
2. ilangin non terminal -> non terminal (cuman satu biji di sisi kanan)
3. ilangin variabel yg gabakal tercapai
4. bikin jadi 2 non terminal atau satu terminal di sisi kanan

ini gk ngecover no 1 sama no 3. 
no 1 gk dicapai karena blom kebayang gimana caranya hehe
no 3 gk dilakuin karena in reality, ini juga gk pernah kebikin :v. kita bikin variabel ya variabel yang at some point bisa dicapai
'''


'''
untuk memudahkan, di cfg.txt, kalo ada nonterminal 2 biji di jejerin, kasi spasi dulu. harusnya gk ngerusak, dan memudahkan pengerjaan translate ke CFG. nti waktu udah jadi CFG, mau ditempel juga gamasalah

SPECIAL SHIT. ini bakal ngaruh di CYK layer pertama

angka 
string

'''
from os import pipe


CNFVarCounter = 1
# mengembalikan true jika X adalah terminal
# terjadi ketika seluruh kata ditulis dengan huruf kapital
def isNotTerminal(X):
    for i in X:
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True

# remove burden lol
def removeBurden(burdenDict,CFGdict,outputString):
    while burdenDict:
        arrBurdenKey = []
        for eachBurdenKey in burdenDict:
            arrBurdenKey.append(eachBurdenKey)
        # print(arrBurdenKey)
        for eachKey in arrBurdenKey:
            outputString += eachKey + " -> "
            # print("burdenDict[eachBurdenKey]")
            # print(burdenDict[eachBurdenKey])
            outputString, burdenDict = addToOuputCNF(burdenDict[eachKey],CFGdict,outputString,burdenDict)
            del burdenDict[eachKey]
            outputString = outputString[0:-2] + ";"
            outputString += "\n"    
    return outputString
# digunakan untuk menambahkan arr ke dalam output string. bisa melihat catatan dict. arr itu list of non terminal or terminal yang ada di sisi kanan CFG.
def addToOuputCNF(arr,dict, outputString,burden):
    global CNFVarCounter # artinya 'hey im using the global variable'
    # kasus satu. hanya ada satu item, dan item tersebut non terminal aka variabel.
    # print('arr = ', arr)
    
    # print(len(arr))
    if len(arr) == 1 and isNotTerminal(arr[0]):
        # print("kasus satu")
        for eachShit in dict[arr[0]]:
            # print("heres each shit", eachShit)
            outputString,burden = addToOuputCNF(eachShit,dict, outputString,burden)
    # kasus dua. hanya ada satu item, dan item tersebut terminal.
    elif len(arr) == 1 and not(isNotTerminal(arr[0])):
        # print("kasus dua")
        outputString += arr[0]
        outputString += " | "
    # kasus tiga. ada dua item, dan kedunya non terminal
    elif len(arr) == 2 and isNotTerminal(arr[0]) and isNotTerminal(arr[1]):
        # print(type(outputString))
        # print("kasus ketiga")
        outputString += arr[0]
        outputString += arr[1]
        outputString += " | "
    # kasus empat. artinya perlu membuat rule baru. barulah burden dipake
    else:
        # print("kasus empat")
        if isNotTerminal(arr[0]):
            outputString += arr[0]
            outputString += 'CNF'+ str(CNFVarCounter) + " | "
            burden['CNF' + str(CNFVarCounter)] = arr[1:]
            CNFVarCounter += 1
        else:
            burden['CNF' + str(CNFVarCounter)] = [arr[0]]
            outputString += 'CNF' + str(CNFVarCounter)
            CNFVarCounter += 1
            if not(len(arr) ==  2 and isNotTerminal(arr[1])):
                outputString += 'CNF'+ str(CNFVarCounter) + " | "
                burden['CNF' + str(CNFVarCounter)] = arr[1:]
                CNFVarCounter += 1
            else:
                outputString += arr[1] + " | "
    return outputString,burden




# sebuah prosedur yang melakukan translasi CFG dari file cfg.txt menjadi CNF lalu meletakkannya di file cnf.txt.
# tidak menerima input dan output
def CFGtoCNF():
    f = open("cfg.txt", "r")
    stringCFG = f.read()
    listCFG = stringCFG.split("\n")

    outputCNF = ""
    # buat catetan CFG yang tersedia sebagai dictionary. LeftSide sebagai key, right side sebagai value, dalam bentuk aray (of array hehe)
    dictCFG  = {}
    for element in listCFG:
        leftSide, rightSide = element.split("->")
        leftSide = leftSide.lstrip().rstrip()
        # outputCNF += leftSide + " -> "
        # print(outputCNF)
        listRightSide = rightSide.split(";")[0].split("|")
        dictCFG[leftSide] = []
        for eachRightSide in listRightSide:
            eachRightSide = eachRightSide.lstrip().rstrip()
            listEachRightSide = eachRightSide.split()
            dictCFG[leftSide].append(listEachRightSide)
    # print(dictCFG)
    # leftSide = 'VALUE'
    for leftSide in dictCFG:
        # print(leftSide)
        outputCNF += leftSide + " -> "
        # print("======================================")
        burden = {}
        for eachRightSide in dictCFG[leftSide]:
            # print(eachRightSide)
            # burden adalah rule2 baru yang harus di implement
            outputCNF,burden = addToOuputCNF(eachRightSide,dictCFG,outputCNF,burden)
            # print("burden")
            # print(burden)
            
        outputCNF = outputCNF[0:-2] + ";"
        outputCNF += "\n"
        outputCNF = removeBurden(burden,dictCFG,outputCNF)
    # print("====== hasil ======")
    return outputCNF
    # print(burden)















    # for element in listCFG:
    #     leftSide, rightSide = element.split("->")
    #     leftSide = leftSide.lstrip().rstrip()
    #     outputCNF += leftSide + " -> "
    #     print(outputCNF)
    #     listRightSide = rightSide.split(";")[0].split("|")
    #     for eachRightSide in listRightSide:
    #         # untuk menghilangkan spasi di kiri dan kanan
    #         eachRightSide = eachRightSide.lstrip().rstrip()
    #         listEachRightSide = eachRightSide.split()
    #         print(listEachRightSide)
    #         # sekarang tiap sisi kanan sudah dipisah menjadi masing2 terminal atau non terminal.
    #         # sekarang waktunya membuat CNF.
    #         # kasus satu. hanya ada satu item, dan item tersebut non terminal aka variabel.
    #         # if len(listEachRightSide) == 1 and not(isTerminal(listEachRightSide[0])):
                
    #         # kasus dua. hanya ada satu item, dan item tersebut terminal.
    #         if len(listEachRightSide) == 1 and isTerminal(listEachRightSide[0]):
    #             outputCNF += listEachRightSide[0]
    #             outputCNF += " | "
                
    #         # kasus tiga. keknya yang ini pake while loop deh.
    #     outputCNF += ";\n"
    # print("=========== output CNF ============")
    # print(outputCNF)
x = CFGtoCNF()
print(x)

