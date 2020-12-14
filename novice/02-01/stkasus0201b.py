'''
Buat Studi Kasus yang berisi struktur data dan fungsi
'''
# Hitung Volume
pi = 22/7
baleni = "n"
masuk = False
pakai_app = "y"

#cara masuk

# Tabung
def vol_tabung(pi,r,t):
    voltab = pi*r*r*t
    return voltab

#print(vol_tabung(pi,5,7))

# Balok
def vol_balok(p,l,t):
    volbal = p*l*t
    return volbal
# Kubus
def vol_kubus(s):
    volkub = s*s*s
    return volkub

# Bola
def vol_ball(pi,r):
    volball = 4/3*pi*r*r*r
    return volball

# Kerucut
def vol_kerucut(pi,r,t):
    volkrucut = 1/3*pi*r*r*t
    return volkrucut
while pakai_app == "y":
    while masuk == False:
        
        melbu = input("Tekan Sembarang ji pale : ")
        
        if melbu != False:
            masuk = True
            baleni = "y"
        else:
            print("")         
            
    while baleni == "y" and masuk == True:
        
        # Menu Operasi
        print('Silahkan Pilih Apa ki mau na Hitung')
        print('1. Volume Tabung')
        print('2. Volume Balok')
        print('3. Volume Kubus')
        print('4. Volume Bola')
        print('5. Volume Kerucut')
        print('Kita tekan "0" Pastimi keluar itu')

        # Meminta masukkan Pemakai
        milih = input("Pilih Ja ki Nomernya : ")
        if milih == '1': #tabung
            bil1 = int(input("Masukkan jari-jari (r): "))
            bil2 = int(input("Masukkan tinggi (t): "))
            print("Volume Tabung = pi x (r*r) x t")
            print("Volume Tabung = ", vol_tabung(pi,bil1,bil2))
            baleni = "n"
            
        elif milih == '2': #balok
            bil1 = int(input("Masukkan panjang (p): "))
            bil2 = int(input("Masukkan lebar (l): "))
            bil3 = int(input("Masukkan tinggi (t): "))
            print("Volume Balok = p x l x t")
            print("Volume Balok = ", vol_balok(bil1,bil2,bil3))
            baleni = "n"
            
        elif milih == '3': #kubus
            bil1 = int(input("Masukkan sisi kubus (s): "))
            print("Volume Kubus = S x S x S")
            print("Volume Kubus = ", vol_kubus(bil1))
            baleni = "n"
            
        elif milih == '4': #Bola
            bil1 = int(input("Masukkan jari-jari (r): "))
            print("Volume Bola = 4/3 x pi x (r*r*r) ")
            print("Volume Bola = ", vol_ball(pi,bil1))
            baleni = "n"
        
        elif milih == '5': #kerucut
            bil1 = int(input("Masukkan jari-jari (r): "))
            bil2 = int(input("Masukkan tinggi (t): "))
            print("Volume Kerucut = 1/3 x pi x r x t ")
            print("Volume Kerucut = ", 1/3, "x", pi, "x", bil1, "x", bil2, "=", vol_kerucut(pi,bil1,bil2))
            baleni = "n"
        
        elif milih == '0':
            masuk = False
            baleni = "n"
            pakai_app = "n"
        else:
            print('Salahki, inputta')
        if masuk == True:
            input("Tekan lagi sembarang untuk kembali ke Menu : ")
            print("")
            baleni = "y"