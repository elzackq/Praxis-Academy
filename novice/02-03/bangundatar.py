from kalkulator import calculator

class Bangundatar:
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.alat_hitung = calculator()
        
    def hitung_luas(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        return self.alat_hitung.kali()
    
