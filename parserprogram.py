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

# KAMUS

# ALGORITMA

'''1. Menerima input berupa file eksternal berisi string yang merupakan kode sebuah program python'''

nama_file = sys.argv[1]
with open(nama_file,"r") as f:
    data = f.read()

# input disimpan dalam var 'data'

'''2. Melakukan evaluasi sintaks dengan CFG'''

# melakukan print jika terjadi kesalahan. implementasi dari Stack terjadi disini.