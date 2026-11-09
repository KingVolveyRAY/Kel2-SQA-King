package com.rayhan.junit;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pengujian Unit Kelas Calculator dengan JUnit 5")
class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }

    @AfterEach
    void tearDown() {
        calculator = null;
    }

    @Test
    @DisplayName("1. Uji Penjumlahan Dua Bilangan Positif")
    void testTambah() {
        int hasil = calculator.tambah(15, 25);
        assertEquals(40, hasil, "15 + 25 seharusnya menghasilkan 40");
    }

    @Test
    @DisplayName("2. Uji Pengurangan dan Perkalian Berkelompok (assertAll)")
    void testKurangDanKali() {
        assertAll("Operasi Aritmatika Dasar",
            () -> assertEquals(10, calculator.kurang(25, 15)),
            () -> assertEquals(-5, calculator.kurang(10, 15)),
            () -> assertEquals(50, calculator.kali(10, 5)),
            () -> assertEquals(0, calculator.kali(99, 0))
        );
    }

    @Test
    @DisplayName("3. Uji Pembagian Normal")
    void testBagiNormal() {
        double hasil = calculator.bagi(10, 4);
        assertEquals(2.5, hasil, 0.0001, "10 / 4 seharusnya menghasilkan 2.5");
    }

    @Test
    @DisplayName("4. Uji Pembagian dengan Nol Harus Melempar Exception")
    void testBagiDenganNol() {
        IllegalArgumentException exception = assertThrows(
            IllegalArgumentException.class,
            () -> calculator.bagi(10, 0)
        );
        assertEquals("Pembagi tidak boleh bernilai nol (0)!", exception.getMessage());
    }

    @Test
    @DisplayName("5. Uji Pengecekan Bilangan Genap dan Ganjil")
    void testApakahGenap() {
        assertTrue(calculator.apakahGenap(12));
        assertFalse(calculator.apakahGenap(13));
    }

    @ParameterizedTest(name = "Nilai {0} menghasilkan Grade {1}")
    @CsvSource({
        "90.0, A",
        "80.0, B",
        "65.0, C",
        "55.0, D",
        "40.0, E"
    })
    @DisplayName("6. Uji Parameterized Penentuan Grade Nilai Mahasiswa")
    void testTentukanGradeValid(double nilaiInput, String expectedGrade) {
        assertEquals(expectedGrade, calculator.tentukanGrade(nilaiInput));
    }

    @Test
    @DisplayName("7. Uji Nilai Mahasiswa di Luar Rentang Valid")
    void testTentukanGradeTidakValid() {
        assertThrows(IllegalArgumentException.class, () -> calculator.tentukanGrade(-5));
        assertThrows(IllegalArgumentException.class, () -> calculator.tentukanGrade(105));
    }
}
