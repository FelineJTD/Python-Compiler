# coba2 hehe
import sys
from CFGtoCNF import CFGtoCNF
from CNFtoCNFdict import CNFtoCNFdict
from CYK import CYK
from tokenizer import tokenizer


nama_file = sys.argv[1]
with open(nama_file,"r") as f:
    data = f.read()

CFGtoCNF("cfgadit.txt")
CNFdict = CNFtoCNFdict()

tokenized = tokenizer(data.lstrip().rstrip())
print("parsing...")
listTopCNF = CYK(tokenized,CNFdict)
# print(listTopCNF)
if 'S' in listTopCNF:
    print("valid")
else:
    print("tidak valid")
