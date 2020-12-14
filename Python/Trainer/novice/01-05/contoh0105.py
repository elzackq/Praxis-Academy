#function
#Biasa
'''
def sapa():
    print('=======================')
    print('halo, Selamat Datang')
    print('***********************')
sapa()

#Dengan Parameter

def sapa(nama):
    print('===========================')
    print('halo, Selamat Datang', nama)
    print('***************************')
sapa('Zaki')
'''
#Dengan Return

def total(a,b):
    return a+b

#bigtotal=total(total(4,5),total(3,7))


total_a=total(4,5)
total_b=total(3,7)
big_total=total(total_a, total_b)
print(big_total)
