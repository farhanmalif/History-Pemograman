'''Membuka File'''
objek_file = open('Tubes_2021_1301213401_Farhan_Muhammad_Alif.txt','r')


''' Jawaban A '''
#Dictionary Kosong
daftar_mobil = {}
#list kosong
list1 = []
# Variabel
tipe = 0
warna = 1
bahan_bakar = 2
stok = 3
# input
a = objek_file.readline()

# Perulangan
while a != '':
#Mengubah String menjadi List
    isi_file = a.split('#')
    isi_file[-1] = isi_file[-1].strip()
#Menambahkan elemen yang ada di isi_file ke dalam list1
    list1.extend(isi_file)
    #Perulangan
    while stok <= len(list1):
    #Membuat Value
        v = [list1[warna],list1[bahan_bakar],int(list1[stok])]
    #Menambahkan pasangan key-value ke dalam dictonary kosong
        daftar_mobil[list1[tipe]]=v
    #Increment
        tipe +=4
        warna += 4
        bahan_bakar +=4
        stok += 4
#Pengulangan input
    a = objek_file.readline()

'''Jawaban B'''
def report(daftar_mobil):
    #dictionary kosong
    banyak_stok = {}
    #Menghilangkan warna dan bahan bakar dari pasangan key-value
    for a,b in daftar_mobil.items():
    #mengisi dictionary kosong dengan pasagan key-value baru
        banyak_stok[a]=b[2]
    # Mencari stok minimal
    min_key = min(banyak_stok, key=banyak_stok.get)
    #Mencari stok maksimal
    max_key = max(banyak_stok, key=banyak_stok.get)
    #return fungsi
    return min_key,max_key

'''Jawaban C'''
def bahan_bakar(dictionary,jenis):
    #Mereturnkan tipe mobil dan jenis bahan bakar
    return jenis,dictionary[jenis][1]



'''Menutup File'''
objek_file.close()








