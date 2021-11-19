# A -> a | BC;
# B -> b;
# C -> C;

#sebuah fungsi yang melakukan translasi dari CNF dari cnf.txt menjadi dictionary of CNF.
# mengembalikan CNF dalam bentuk dictionary
def CNFtoCNFdict():
    CNFdict = {}
    # baca file
    f = open("cnf.txt", "r")
    stringCNF = f.read()
    listCNF = stringCNF.split("\n")
    # print('awal')
    # print(stringCNF)
    # print(listCNF)
    for element in listCNF:
        leftSide,rightSide = element.split("->")
        # untuk menghilangkan spasi
        leftSide = leftSide.lstrip().rstrip()
        
        listRightSide = rightSide.split(";")[0].split("|")
        for eachRightSide in listRightSide:
            # untuk menghilangkan spasi
            eachRightSide = eachRightSide.lstrip().rstrip()
            CNFdict[eachRightSide] = leftSide
    return CNFdict
x = CNFtoCNFdict()
# print("hasil")
# print(x)