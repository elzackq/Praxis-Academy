#tambah
def tambah(a,b):
    return a+b

#kurang
def kurang(a,b):
    return a-b

#bagi
def bagi(a,b):
    return a/b
#kali
def kali(a,b):
    return a*b

#hasil=tambah(10,10)
#hasil=kurang(10,3)
#hasil=bagi(21,3)
#hasil=kali(3,9)

# Menu Operasi
print('Silahkan Pilih yang anda butuhkan')
print('1.Penambahan(+)')
print('2.Pengurangan(-)')
print('3.Pembagian(/)')
print('4.Perkalian(*)')

# Meminta input pemakai
milih = input("Silahkan Pilih(1/2/3/4): ")

bil1 = int(input("Masukkan angka pertama: "))
bil2 = int(input("Masukkan angka kedua: "))

if milih =='1':
    print(bil1,"+", bil2,"=", tambah(bil1,bil2))

elif milih =='2':
    print(bil1,"-", bil2,"=", kurang(bil1,bil2))

elif milih =='3':
    print(bil1,":", bil2,"=", bagi(bil1,bil2))

elif milih =='4':
    print(bil1,"x", bil2,"=", kali(bil1,bil2))

else:
    print('Input Salah')