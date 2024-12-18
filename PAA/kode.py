from itertools import combinations

barang = ['smartphone', 'laptop', 'headphone', 'mouse', 'keyboard']
permintaan = [250,100,50,120,80]
stok = [20,50,10,30,40]
batas_barang = 3
batas_kandidat = 4

def seleksi_kandidat(barang,permintaan,stok,batas_kandidat):
    barang_data = sorted(zip(barang,permintaan,stok), key=lambda x: (x[1],x[2]), reverse=True)
    kandidat = barang_data[:batas_kandidat]
    return kandidat

def optimasi_brute_force(kandidat,batas_barang):
    n = len(kandidat)
    kombinasi_terbaik = []
    nilai_terbaik = 0

    for i in range (1, batas_barang + 1):
        for kombinasi in combinations(range(n), 1):
            total_permintaan = 0
            total_stok = 0
            for index in kombinasi:
                total_permintaan += kandidat[index][1]
                total_stok += kandidat[index][2]

            nilai=total_permintaan * total_stok

            if nilai > nilai_terbaik:
                nilai_terbaik = nilai
                kombinasi_terbaik = kombinasi 

    return [kandidat[i][0]for i in kombinasi_terbaik], nilai_terbaik
        
kandidat = seleksi_kandidat(barang,permintaan,stok,batas_kandidat)
barang_terpilih,nilai =optimasi_brute_force(kandidat,batas_barang)
print(f"Kandidat Barang: {[b[0] for b in kandidat]}")
print(f"Barang yang dipromosikan: {barang_terpilih}, Nilai: {nilai}")