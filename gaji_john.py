"""
gaji_john.py -- VERSI 2 (setelah Code Review)

Soal John Travolta:
  1) Gaji mingguan: 40 jam pertama dibayar tarif normal (default Rp 15.000/jam),
     jam di atas 40 dibayar 1,5 x tarif normal (lembur).
  2) Bandingkan pemasukan (gaji) dengan pengeluaran:
       pemasukan >  pengeluaran -> "bisa menabung" (tampilkan besar tabungan)
       pemasukan == pengeluaran -> "tidak bisa menabung"
       pemasukan <  pengeluaran -> "cari tambahan"

Cara pakai:  python gaji_john.py
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

BATAS_JAM_NORMAL = Decimal("40")
FAKTOR_LEMBUR = Decimal("1.5")
TARIF_DEFAULT = Decimal("15000")
PENGELUARAN_DEFAULT = Decimal("600000")


# ----------------------------------------------------------------------
# Logika inti (tanpa input/print, supaya mudah diuji)
# ----------------------------------------------------------------------
def hitung_gaji(jam_kerja, tarif=TARIF_DEFAULT):
    """Return (gaji_normal, gaji_lembur, total_gaji) dalam Decimal."""
    jam_kerja = Decimal(str(jam_kerja))
    tarif = Decimal(str(tarif))
    if jam_kerja < 0 or tarif < 0:
        raise ValueError("Jam kerja dan tarif tidak boleh negatif.")

    jam_normal = min(jam_kerja, BATAS_JAM_NORMAL)
    jam_lembur = max(jam_kerja - BATAS_JAM_NORMAL, Decimal("0"))

    gaji_normal = jam_normal * tarif
    gaji_lembur = jam_lembur * tarif * FAKTOR_LEMBUR
    return gaji_normal, gaji_lembur, gaji_normal + gaji_lembur


def cek_tabungan(pemasukan, pengeluaran):
    """Return (pesan, selisih). selisih = pemasukan - pengeluaran."""
    pemasukan = Decimal(str(pemasukan))
    pengeluaran = Decimal(str(pengeluaran))
    selisih = pemasukan - pengeluaran
    if pemasukan > pengeluaran:
        return "bisa menabung", selisih
    if pemasukan == pengeluaran:
        return "tidak bisa menabung", selisih
    return "cari tambahan", selisih


def format_rupiah(nilai):
    bulat = Decimal(nilai).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return "Rp " + f"{bulat:,.0f}".replace(",", ".")


# ----------------------------------------------------------------------
# Input dari pengguna (dengan validasi)
# ----------------------------------------------------------------------
def baca_angka(prompt, default=None, rupiah=False):
    """Minta angka >= 0. Untuk rupiah, titik dianggap pemisah ribuan."""
    while True:
        teks = input(prompt).strip()
        if teks == "" and default is not None:
            return default
        if rupiah:
            teks = teks.lower().replace("rp", "").replace(" ", "").replace(".", "")
        teks = teks.replace(",", ".")
        try:
            angka = Decimal(teks)
        except InvalidOperation:
            print("  Input harus berupa angka. Coba lagi.")
            continue
        if not angka.is_finite() or angka < 0:
            print("  Angka harus berupa bilangan tidak negatif. Coba lagi.")
            continue
        return angka


def tampilkan_rincian_gaji(jam, tarif):
    normal, lembur, total = hitung_gaji(jam, tarif)
    jam_lembur = max(jam - BATAS_JAM_NORMAL, Decimal("0"))
    print(f"  Jam kerja        : {jam} jam (lembur {jam_lembur} jam)")
    print(f"  Tarif normal     : {format_rupiah(tarif)}/jam")
    print(f"  Tarif lembur     : {format_rupiah(tarif * FAKTOR_LEMBUR)}/jam")
    print(f"  Gaji normal      : {format_rupiah(normal)}")
    print(f"  Gaji lembur      : {format_rupiah(lembur)}")
    print(f"  TOTAL GAJI       : {format_rupiah(total)}")
    return total


# ----------------------------------------------------------------------
# Soal 1, Soal 2, dan demo variasi data
# ----------------------------------------------------------------------
def soal1():
    print("\n=== SOAL 1: HITUNG GAJI ===")
    jam = baca_angka("Jam kerja seminggu [52]: ", Decimal("52"))
    tarif = baca_angka("Tarif normal per jam [15000]: ", TARIF_DEFAULT, rupiah=True)
    tampilkan_rincian_gaji(jam, tarif)


def soal2():
    print("\n=== SOAL 2: CEK TABUNGAN ===")
    jam = baca_angka("Jam kerja seminggu [52]: ", Decimal("52"))
    tarif = baca_angka("Tarif normal per jam [15000]: ", TARIF_DEFAULT, rupiah=True)
    pengeluaran = baca_angka("Pengeluaran seminggu [600000]: ",
                             PENGELUARAN_DEFAULT, rupiah=True)
    total = tampilkan_rincian_gaji(jam, tarif)
    pesan, selisih = cek_tabungan(total, pengeluaran)
    print(f"  Pengeluaran      : {format_rupiah(pengeluaran)}")
    print(f"  Hasil            : {pesan}")
    if selisih > 0:
        print(f"  Tabungan minggu ini : {format_rupiah(selisih)}")
    elif selisih < 0:
        print(f"  Kekurangan dana     : {format_rupiah(-selisih)}")


def demo_variasi():
    print("\n=== DEMO VARIASI DATA ===")
    data = [  # (jam, tarif, pengeluaran)
        (52, 15000, 600000),   # data soal
        (40, 15000, 600000),   # tepat 40 jam (batas)
        (30, 15000, 600000),   # kurang dari 40 jam
        (45, 20000, 700000),   # tarif berbeda
        (60, 15000, 1050000),  # pemasukan = pengeluaran
        (42.5, 18000, 800000), # jam desimal
    ]
    judul = f"{'Jam':>5} {'Tarif':>9} {'Gaji':>12} {'Pengeluaran':>12}  Hasil"
    print(judul)
    print("-" * 70)
    for jam, tarif, keluar in data:
        _, _, total = hitung_gaji(jam, tarif)
        pesan, selisih = cek_tabungan(total, keluar)
        if selisih > 0:
            ket = f"{pesan} (tabungan {format_rupiah(selisih)})"
        elif selisih < 0:
            ket = f"{pesan} (kurang {format_rupiah(-selisih)})"
        else:
            ket = pesan
        print(f"{jam:>5} {format_rupiah(tarif):>9} {format_rupiah(total):>12} "
              f"{format_rupiah(keluar):>12}  {ket}")


def main():
    while True:
        print("\n===== PROGRAM GAJI & TABUNGAN MR. JOHN TRAVOLTA =====")
        print("1. Soal 1 - Hitung gaji")
        print("2. Soal 2 - Cek tabungan")
        print("3. Demo variasi data")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            soal1()
        elif pilihan == "2":
            soal2()
        elif pilihan == "3":
            demo_variasi()
        elif pilihan == "0":
            print("Selesai.")
            break
        else:
            print("Menu tidak dikenal.")


if __name__ == "__main__":
    main()
