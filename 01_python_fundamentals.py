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

