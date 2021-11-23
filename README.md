# Python-Compiler

Tugas Besar TBFO - Python Compiler with Context Free Grammar

## Dibuat oleh:
<ul>
	<li> Aditya Prawira N - 13520049  
	<li> Felicia Sutandijo - 13520050  
	<li> Christopher Jeffrey - 13520055
</ul>

## Struktur Direktori
1. `cfg.txt` &rarr; Berisi aturan produksi CFG
2. `cnf.txt` &rarr; Berisi hasil konversi `cfg.txt` menjadi cnf
3. `dfa.txt` &rarr; Berisi dfa untuk aturan penamaan variabel
4. `CFGtoCNF.py` &rarr; Berisi fungsi yang mengonversi `cfg.txt` dan menuliskannya ke dalam `cnf.txt`
5. `CNFtoCNFdict.py` &rarr; Berisi fungsi yang mengonversi `cnf.txt` ke dalam bentuk dict
6. `CYK.py` &rarr; Berisi fungsi yang menggunakan algoritma CYK untuk mengetes <em>membership</em>
7. `FA.py` &rarr; Berisi fungsi yang mengetes validasi penamaan variabel

## Cara Menjalankan Program
`python3 parserprogram.py nama_file`
