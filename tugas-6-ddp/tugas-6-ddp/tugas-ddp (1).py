# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ketb-6GOjFjHUf9NTBPPyMYduR0vqqtM
"""

#soal 1: bilangan genap atau ganjil
bilangan_bulat =int(input("masukkan bilangan bulat: "))

if bilangan_bulat %2==0:
    print("bilangan" , bilangan_bulat, "adalah bilangan genap")
else:
    print("bilangan" , bilangan_bulat, "adalah bilangan ganjil")





#soal 2: nilai ujian
nilai_ujian_mhs =int(input('masukan nilai ujian:'))
if nilai_ujian_mhs>=75:
        print("Lulus")
else:
     print("tidak lulus")

#soal 3: cek usia dan status
usia =int(input("masukkan usia:"))
if usia>=18:
          print("dewasa")
elif usia>=13 and usia <=17:
    print("remaja")
else:
    print("anak anak")

#tugas 4

status_keanggotaan = input("masukan status ke anggotaan ").lower()
if status_keanggotaan == "gold" or status_keanggotaan == "silver":
    print("selamat! anda mendapatkan diskon")
else:
    print("maaf,anda tidak mendapatkan diskon")

#

#5: pembelian diskon
#Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
#example :
#minyak 25.000, indomie 5.000, beras 75.000, gula 25.000, kopi 20.000, teh 10.000

minyak =25000
indomie =5000

#input
jumlah_pembelian_minyak =int(input("masukan jumlah pembelian minyak:"))
jumlah_pembelian_indomie =int(input("masukan jumlah pembelian indomie:"))

#proses konidis
total_harga =(jumlah_pembelian_minyak*minyak)+(jumlah_pembelian_indomie*indomie)
diskon=0.1

#shortand if
total_diskon =total_harga*diskon if(jumlah_pembelian_minyak+jumlah_pembelian_indomie)>100 else 0
total_harga-=diskon

#cetak hasil
print("walaw eeee kamu dapat disc sebesar 10% Rp",diskon)
print("total harga:Rp",total_harga)