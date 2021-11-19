# Python-Compiler

Tugas Besar TBFO - Python Compiler with Context Free Grammar

Aditya PN 13520049  
Felicia Sutandijo 13520050  
Christopher Jeffrey 13520055

## Cara Menjalankan Program
`python3 parserprogram.py nama_file`

[link to TBFO spec](https://docs.google.com/document/d/1Fd8wLOP_GzJ66atpw1yK1_S1dLCFQcKFTgnePFHql7Y/edit)

### urutan langkah algo
1. bikin CFG
2. bikin CNF
3. input file
4. evaluasi input berdasarkan CNF dengan algo CYK
	-ubah CNF menjadi dictionary(harus dictionary, objectively better untuk kasus ini)
	- terapkan algo CYK terhadap input
	- cek FA variabel
	- cek baris teratas dari hasil algo CYK
	- output
---
catatan, bukan dibagi berdasarkan tingkat kesusahan, tapi berdasarkan 'keterpisahan' dan urutan pengerjaan.

### pembagian tugas

1. bikin CFG(dalam txt)
	- bisa dibagi2 dulu berdasarkan keyword python 
2. algo prosedur CFGtoCNF(bakal write txt)
3. algo function CNFtoCNFdict -> dict
4. algo prosedur CYK(input1line, CNFdict) -> array di matriks cyk 0,0.
5. algo parseInput(inputSemua,CNFdict) (langsung print2 kalau ada kesalahan, disini implement stack buat ngecek validitas per line)


#### contoh CNF dan CFG (kalo CFG tanpa constrain CNF)

A -> a | b | CD


#### contoh dictionary
{"CD": "A",\
"a": "A",\
"b": "A"}

### konvensi penamaan CFG
terminal\
-> huruf kapital semua\
-> kalau mau kasih angka, kasih dibelakang\
non terminal\
-> sesuasi nama di python

contoh terminal\
`IF`\
`ELSE`\
`IF30`\
contoh non terminal\
`if`\
`else`\
`;`\
--- 
**start dari terminal S**\
biar logical aja, S bisa stand for Statement atau Start