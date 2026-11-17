# Statement: unit terkecil yang dapat dieksekusi
x = 10
print(x)
## atau
if x > 5:
    print(x, "lebih besar dari 5")

# Case sensitive: aturan menggunakan huruf kecil dan huruf kapital
print("Hello World!")
## Print("Halo Dunia!") # NameError: fungsi print() tidak sesuai aturan pada Python

# Identation: penataan baris-baris kode program, bagian mana yang menjorok lebih ke dalam dan yang tidak
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

print(luas_segitiga(6, 8))

# Variabel: tempat penyimpanan sementara di dalam memori komputer untuk menampung data/nilai
nama_buah = ["apel", "jeruk", "mangga", "anggur", "pisang"]
print(nama_buah)

# Tipe Data pada Python
## Integer (int): bilangan bulat
angka = 90
print(angka)
## Float (float): bilangan pecahan
desimal = 0.7
print(desimal)
## String (str): teks/urutan karakter
negara = "Indonesia"
print(negara)
## Boolean (bool): nilai kebenaran
laki_laki_benar = False
print(laki_laki_benar)
## List (list): kumpulan nilai/objek yang dapat diubah, disusun dalam urutan tertentu
pakaian = ["kaos", "kemeja", "jas"]
print(pakaian)
## Tuple (tuple): kumpulan nilai/objek yang tidak dapat diubah, disusun dalam urutan tertentu
nama_hari = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
print(nama_hari)
## Dictionary (dict): kumpulan pasangan kunci-nilai (key-value) yang tidak berurutan
hardware = {"processor": "intel", "ram": 8, "storage": "SSD"}
print(hardware)
## Set (set): himpunan nilai unik yang tanpa urutan tertentu
kata_kata = {"urip", "iku", "urup", "tapi", "dompetku", "redup"}
print(kata_kata)

# Assignment: instruksi membuat variabel dan memasukkan data ke dalam variabel tersebut
## Assignment operator: proses assignment pada variabel dengan menggunakan operator tanda sama dengan (=)
nilai_kkm = input("Silakan masukkan nilai kkm: ")
print("Nilai kkm:", nilai_kkm)
## Multiple assignment: memasukkan nilai ke dalam beberapa variabel sekaligus
murid1 = murid2 = murid3 = 80 # menghasilkan nilai sama
print("murid1:", murid1)
print("murid2:", murid2)
print("murid3:", murid3)

nama_murid, nilai_murid, mata_pelajaran = "Agus", 75, "Matematika" # menghasilkan nilai berbeda
print("Nama:", nama_murid, "|", "Nilai:", nilai_murid, "|", "Mapel:", mata_pelajaran)

# Swap variables: proses menukar data antara beberapa variabel
x = 10
y = 20
print("x:", x, "|", "y:", y)

x,y = y,x
print("x:", x, "|", "y:", y)

# Fungsi print(): untuk menampilkan/mencetak nilai di layar monitor
## Menampilkan nilai di dalam variabel
z = 1000
print(z)
## Antara fungsi print() dan string:
### Menggunakan tanda kutip tunggal dan tanda kutip ganda
print("Ini hari Selasa")
print('Besok hari apa?')
### Menggunakan escape character: karakter khusus untuk merubah makna dari karakter berikutnya
print("Ini Budi \nItu Bapak Budi")
### Menggunakan escape code: ANSI code
print("\033[1;32;40m Tulisan ini berwarna \033[0m Tulisan ini kembali normal")
### Menggunakan argument end: berfungsi menghilangkan karakter newline (baris baru) aturan default dari fungsi print()
print("Halo", end="")
print(" Dunia!")
### Bekerja dengan Raw String: menampilkan string apa adanya
print(r"Ini hari: \nSelasa")
### Menggunakan tanda kutip tiga
print('''Mawar itu merah
Violet itu ungu''')
### Memanfaatkan .format: meletakkan nilai/data ke dalam placeholder {...}
print("Halo, nama saya {0} ini ayah saya {1}". format("Budi", "Adi"))
print("Usia saya {1} tahun, hobi saya {0}". format("voli", 20))
harga = "Ini harganya Rp{:,}" # separator pada angka
print(harga . format(200000))

# Tipe data numerik
## Integer (int): bilangan bulat, contoh: 1, 2, 100
## Float (float): bilangan pecahan, contoh: 0.1, 1.4, 3.14
## Complex number: bilangan kompleks/bilangan imajiner, contoh: 10j, 5j, 1j

# Bekerja dengan int, selain bilangan bulat dapat digunakan untuk membuat angka dengan tujuan khusus
## Binary / Biner | Base 2 | Angka 0 dan 1
base_2 = 0b100
print("100 binary dari angka:", base_2)
# base_2 = 0b2 # Error: karena binary hanya menggunakan angka 0 dan 1 saja
# print("2 binary dari angka:", base_2)

## Oct / Octal | Base 8 | Angka 0 hingga 7
base_8 = 0o777
print("777 octal dari angka:", base_8)
# base_8 = 0o8 # Error: karena octal menggunakan angka 0 hingga 7
# print("8 octal dari angka:", base_8)

## Hexadecimal | Base 16 | Angka 0 hingga 9 dan huruf A hingga F
base_16 = 0x9AF
print("9AF hexadecimal dari angka:", base_16)
# base_16 = 0x9G # Error: karena hexadecimal menggunakan angka 0 hingga 9 dan huruf A hingga F
# print("9G hexadecimal dari angka:", base_16)

## Menggunakan fungsi bin(), oct(), hex() untuk mengubah angka biasa menjadi binary, octal, atau hexadecimal
print("Angka 9 binary-nya adalah: ", bin(9))
print("Angka 9 octal-nya adalah: ", oct(9))
print("Angka 9 hexadecimal-nya adalah: ", hex(9))

# Bekerja dengan Bilangan Pecahan (float)
angka_float = 255.0
print("angka float yang ditulis langsung: ", angka_float)
## memanfaatkan scientific notation
angka_float = 2.55e2
print("angka float menggunakan scietific notation: ", angka_float)
angka_float = 2.55e-2
print("angka float menggunakan pangkat negatif: ", angka_float)

# Type conversion (typecasting): proses mengubah tipe data variabel
## Konversi tipe data integer menjadi string
usia = 21
usia_str = str(usia)
print("Usia dia sekarang", usia_str)
print("Tipe data usia_str:", type(usia_str), "sebelumnya:", type(usia))
## Konversi tipe data string menjadi integer
nilai = "70"
nilai_int = int(nilai)
print("Nilai:", nilai_int)
print("Tipe data nilai_int:", type(nilai_int), "sebelumnya:", type(nilai))
## Konversi tipe data string menjadi float
pi = "3.14"
pi_float = float(pi)
print("PI:", pi_float)
print("Tipe data pi_float:", type(pi_float), "sebelumnya:", type(pi))

