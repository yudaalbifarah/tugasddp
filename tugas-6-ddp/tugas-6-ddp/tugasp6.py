a = 1
while a <=20:
    print(a)
    a += 2


index = 0
numbers = [
    13, 14, 16, 16, 17, 18, 19, 20, 21, 951, 402, 984, 651, 360, 69, 408, 319,
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
    942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
    626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
    843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857,
    440, 380, 126, 721, 328, 753, 470, 743, 527
]

# Menggunakan loop untuk mencetak bilangan ganjil sampai dengan 533
while index < len(numbers):
    if numbers[index] % 2 != 0:  # cek apakah bilangan ganjil
        print(numbers[index], end=" ")
    if numbers[index] == 553:
        # hentikan perulangan jika sudah mencapai 553
        break
    index += 1

print("")


for a in range(1, 21):
    if a % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(a)


# Mencetak header
print("")

# Mencetak penjumlahan dari bilangan ganjil
print("1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = ...")

# Inisialisasi variabel untuk menghitung jumlah bilangan ganjil
jumlah_total_bilangan_ganjil = 0
bilangan_ganjil = 1

# Menghitung jumlah bilangan ganjil
for i in range(10):  # Mengulangi 10 kali untuk 10 bilangan ganjil pertama
    jumlah_total_bilangan_ganjil += bilangan_ganjil
    bilangan_ganjil += 2

# Mencetak hasil
print(f"Jumlah total bilangan ganjil = {jumlah_total_bilangan_ganjil}")

print("")

# meminta input jumlah baris
baris = int(input("Masukkan jumlah baris: "))

# membuat pola bintang
for i in range(baris):
  for j in range(i+1):
    print("*", end="")
  print()
