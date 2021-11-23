# A -> a | BC;
# B -> b;
# C -> C;

# sebuah fungsi yang melakukan translasi dari CNF dari cnf.txt menjadi dictionary of CNF.
# mengembalikan CNF dalam bentuk dictionary
def CNFtoCNFdict():
    CNFdict = {}
    # baca file
    f = open("cnf.txt", "r")
    stringCNF = f.read()
    listCNF = stringCNF.split("\n")
    for element in listCNF:
        leftSide,rightSide = element.split("->")
        # untuk menghilangkan spasi
        leftSide = leftSide.lstrip().rstrip()
        
        listRightSide = rightSide.split(";")[0].split("|")
        for eachRightSide in listRightSide:
            # untuk menghilangkan spasi dibagian kiri dan kanan
            eachRightSide = eachRightSide.lstrip().rstrip()
            if eachRightSide in CNFdict:
                CNFdict[eachRightSide].append(leftSide)
            else:
                CNFdict[eachRightSide] = [leftSide]
    return CNFdict