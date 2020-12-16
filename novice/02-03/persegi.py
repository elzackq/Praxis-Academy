from bangundatar import Bangundatar

# Penurunan Sifat (INHARITANCE)

class Persegi(Bangundatar):
    # override
    def __init__(self):
        super( ).__init__()
        self.sisi = 0
        
    # override
    def hitung_luas(self):
        self.panjang = self.sisi
        self.lebar = self.sisi
        return super().hitung_luas()
    
kotak = Persegi()
kotak.sisi = 5
hasil = kotak.hitung_luas()
print(hasil)