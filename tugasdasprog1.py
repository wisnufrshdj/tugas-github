angka = 0
jumlah_genap = 0
jumlah_ganjil = 0
while angka >= 0:
    angka = int(input("Inputkan bilangan : "))
    if angka < 0:
        break
    proses = angka % 2
    if proses == 0:
        jumlah_genap += angka
    else:
        jumlah_ganjil += angka
print("\nJumlah bilangan genap :", jumlah_genap)
print("Jumlah bilangan ganil :", jumlah_ganjil)