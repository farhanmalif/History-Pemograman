'''Jawaban D'''
from Tubes_2021_1301213401_Farhan_Muhammad_Alif import *

#Memunculkan ditionary
print('Daftar mobil:',daftar_mobil)
#Memunculkan fungsi report
x,y = report(daftar_mobil)
print('Mobil stok tersedikit:',x)
print('Mobil stok terbanyak:',y)
#Memunculkan fungsi bahan_bakar
n = input()
x,y = bahan_bakar(daftar_mobil,n)
print('Tipe mobil',x,'menggunakan',y)
