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
