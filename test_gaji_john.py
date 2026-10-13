import unittest
from decimal import Decimal as D
from unittest.mock import patch

from gaji_john import baca_angka, cek_tabungan, format_rupiah, hitung_gaji


class TestHitungGaji(unittest.TestCase):
    def test_data_soal_52_jam(self):
        normal, lembur, total = hitung_gaji(52)
        self.assertEqual((normal, lembur, total), (D("600000"), D("270000"), D("870000")))

    def test_tepat_40_jam_tanpa_lembur(self):
        self.assertEqual(hitung_gaji(40)[2], D("600000"))

    def test_41_jam_lembur_1_jam(self):
        self.assertEqual(hitung_gaji(41)[2], D("622500"))

    def test_kurang_dari_40_jam(self):
        self.assertEqual(hitung_gaji(30)[2], D("450000"))

    def test_nol_jam(self):
        self.assertEqual(hitung_gaji(0)[2], D("0"))

    def test_jam_desimal(self):
        self.assertEqual(hitung_gaji("42.5")[2], D("656250"))

    def test_tarif_berbeda(self):
        self.assertEqual(hitung_gaji(45, 20000)[2], D("950000"))

    def test_input_negatif_ditolak(self):
        with self.assertRaises(ValueError):
            hitung_gaji(-1)
        with self.assertRaises(ValueError):
            hitung_gaji(10, -15000)

    def test_regresi_temuan_cr_gaji_tidak_dihitung_dua_kali(self):
        # v1 menghasilkan 1.050.000 untuk 52 jam (jam normal terhitung 52, bukan 40)
        self.assertNotEqual(hitung_gaji(52)[2], D("1050000"))


class TestCekTabungan(unittest.TestCase):
    def test_bisa_menabung(self):
        self.assertEqual(cek_tabungan(870000, 600000), ("bisa menabung", D("270000")))

    def test_sama_tidak_bisa_menabung(self):
        # v1 salah: memakai >= sehingga kasus sama tercetak "bisa menabung"
        self.assertEqual(cek_tabungan(600000, 600000), ("tidak bisa menabung", D("0")))

    def test_cari_tambahan(self):
        self.assertEqual(cek_tabungan(450000, 600000), ("cari tambahan", D("-150000")))


class TestFormatDanInput(unittest.TestCase):
    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(D("870000")), "Rp 870.000")
        self.assertEqual(format_rupiah(D("0")), "Rp 0")

    def test_baca_angka_menolak_teks_dan_negatif_lalu_menerima(self):
        with patch("builtins.input", side_effect=["abc", "-5", "42"]), patch("builtins.print"):
            self.assertEqual(baca_angka("jam: "), D("42"))

    def test_baca_angka_rupiah_titik_ribuan(self):
        with patch("builtins.input", side_effect=["15.000"]):
            self.assertEqual(baca_angka("tarif: ", rupiah=True), D("15000"))

    def test_baca_angka_default_saat_enter(self):
        with patch("builtins.input", side_effect=[""]):
            self.assertEqual(baca_angka("jam: ", D("52")), D("52"))


if __name__ == "__main__":
    unittest.main()
