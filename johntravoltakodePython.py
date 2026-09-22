/*Source Code Python (Kasus 1):*/

def hitung_gaji(jam_kerja):
    if jam_kerja > 40:
        gaji = (40 * 15000) + ((jam_kerja - 40) * 22500)
    else:
        gaji = jam_kerja * 15000
    print(f"Jam Kerja: {jam_kerja} Jam -> Total Gaji: Rp {gaji}")
    return gaji

# Eksekusi Sesuai Soal
hitung_gaji(52)
# Test Case Nilai Variatif
hitung_gaji(40)  
hitung_gaji(30)  

// ══════════════════════════════════════════════════════════

/*Source Code Python (Kasus 2):*/

def cek_tabungan(pemasukan, pengeluaran):
    print(f"Pemasukan: Rp {pemasukan} | Pengeluaran: Rp {pengeluaran}")
    if pemasukan > pengeluaran:
        print("Status: Bisa menabung")
        print(f"Tabungan: Rp {pemasukan - pengeluaran}\n")
    elif pemasukan == pengeluaran:
        print("Status: Tidak bisa menabung\n")
    else:
        print("Status: Cari tambahan\n")

# Eksekusi Sesuai Soal
cek_tabungan(870000, 600000)
# Test Case Nilai Variatif
cek_tabungan(600000, 600000) 
cek_tabungan(450000, 600000) 
