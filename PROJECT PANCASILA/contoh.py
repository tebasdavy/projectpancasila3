input_barang = input("Masukkan Nama Barang: ")
barang = input_barang.split(',')

def hitung_inventaris(barang):
    inventaris = {}

    for item in barang:
        if item in inventaris:
            inventaris[item] +=1 
        else:
            inventaris[item] = 1 

    return inventaris  
    
output = hitung_inventaris(barang)
print (output)
