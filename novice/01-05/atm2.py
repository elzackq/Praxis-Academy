import string
import getpass
import os


user_id = 0
loop = "n"
user = [ 
            {
                "id":"1234",
                "no_rekening":"000123",
                "username":"Ahmad",
                "pin":"4321",
                "saldo":0     
            },
            {
                "id":"1234",
                "no_rekening":"000124",
                "username":"Muhammad",
                "pin":"1234",
                "saldo":99999    
            }
        ]
status_login = False
pakai_atm = "y"

def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False

def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1

def cek_rek(no):
    for i in range(len(user)):
        if str(user[i]['id']) == str(no):
            return int(i)
    return -1

def tf_uang(uang, no_rek):
    index1 = cek_user(user_id)
    index2 = cek_rek(no_rek)
    if index1 >=0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] = user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] = user[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp. " +str(uang)+"ke Rekening" +no_rek)
            print("Sisa saldo anda adalah Rp. ", user[index1]['saldo'])
        else:
            print("Wadidauw Saldo anda tidak cukup Coyyyy")
            
def tarik_tun(uang):
    index1 = cek_user(user_id)
    if index1 >=0:
        if user[index1]['Saldo'] >= int(uang):
            user[index1]['Saldo'] = user[index1]['Saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp. "+str(uang))
            print("Sisa saldo anda adalah Rp. ", user[index1]['Saldo'])
        else:
            print("Endeddeeeeh eeee saldo anda tidak cukupji")

while pakai_atm == "y":
    while status_login == False:
        print("Selamat Datang di Bank Syariah of El'Institute")
        print("Silahkan Masukkan pin anda")   
        pin = input("Masukkan PIN : ")
        
        cl = cek_login(pin)
        if cl != False:
            print("Selamat Datang"+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Salahki PIN ta ")
            print("")
            print("")
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        print("Selamat Datang di Bank Syariah of El'Institute")
        print("1. Cek Saldo")
        print("2. Transfer Uang")
        print("3. Tarik Tunai")
        print("4. Logout")
        print("5. Keluar ATM")
        a = int(input("Silahkan Pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp. ", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukkan No Rekening Tujuan")
            no_rek = input("Masukkan No Rekening Tujuan : ")
            cnk = cek_rek(no_rek)
            
            if cnk >=0:
                print("Nomor rekening ditemukan, Silahkan Masukkan nominal yang akan ditransferkan ")
                nominal = input("Nominal yang Akan di Transfer : ")
                tf_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
        elif a == 3:
            nominal = input("Nominal yang akan di Tarik :")
            tarik_tun(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
            
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("Pilihan tidak tersedia")
        if status_login == True:
            input("Kembali Ke Menu (ENTER) ")
            print("")
            loop = "y"