# gaji_john_v1.py
# Soal John Travolta: gaji mingguan + lembur, lalu cek tabungan

jam = int(input("Jam kerja minggu ini: "))
rate = 15000

# --- Soal 1: hitung gaji ---
if jam > 40:
    gaji = jam * rate + (jam - 40) * rate * 1.5
else:
    gaji = jam * rate
print("Gaji John:", gaji)

# --- Soal 2: cek tabungan ---
pengeluaran = 600000
if gaji >= pengeluaran:
    print("bisa menabung")
    print("Tabungan:", gaji - pengeluaran)
elif gaji < pengeluaran:
    print("cari tambahan")
