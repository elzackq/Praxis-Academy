class calculator:
    #Methods
    def __init__(self):
        self.a = 0
        self.b = 0
    
    #tambah   
    def tambah(self):
        return self.a

    #kurang
    def kurang(self):
        return self.a -self.b

    #bagi
    def bagi(self):
        return self.a / self.b
    #kali
    def kali(self):
        return self.a *self.b
    
# casio = calculator()
# hasil = casio.tambah(2,3)
# print(hasil)