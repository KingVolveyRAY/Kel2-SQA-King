# 🧪 Implementasi Unit Testing JUnit 5 & Analisis Pengujian Perangkat Lunak

[![Java](https://img.shields.io/badge/Java-17%2B-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.oracle.com/java/)
[![JUnit 5](https://img.shields.io/badge/JUnit-5.10.2-25A162?style=for-the-badge&logo=junit5&logoColor=white)](https://junit.org/junit5/)
[![Apache Maven](https://img.shields.io/badge/Apache%20Maven-3.6%2B-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)](https://maven.apache.org/)
[![Status](https://img.shields.io/badge/Tests-11%20Passed-brightgreen?style=for-the-badge)]()

Repositori pada branch **`junit-sample-testing`** ini berisi implementasi sampel pengujian unit (*unit testing*) menggunakan **JUnit 5 (JUnit Jupiter)** dan **Apache Maven** pada bahasa pemrograman Java, analisis mendalam konsep **5W + 1H JUnit**, studi literatur **6 tesis/skripsi internasional mengenai Selenium WebDriver**, serta dokumen laporan resmi kelompok.

Proyek ini disusun untuk memenuhi tugas mata kuliah **Pengujian Perangkat Lunak (Software Quality Assurance)**.

---

## 👥 Informasi Kelompok & Mata Kuliah

### Detail Mata Kuliah
| Keterangan | Informasi |
| :--- | :--- |
| **Mata Kuliah** | Pengujian Perangkat Lunak (Software Quality Assurance) |
| **Program Studi** | Teknik Informatika — Fakultas Sains dan Teknologi |
| **Institusi** | UIN Syarif Hidayatullah Jakarta |
| **Dosen Pengampu** | Pak Broer |
| **Repositori Utama** | [KingVolveyRAY/Kel2-SQA-King](https://github.com/KingVolveyRAY/Kel2-SQA-King) |
| **Branch Tugas** | [`junit-sample-testing`](https://github.com/KingVolveyRAY/Kel2-SQA-King/tree/junit-sample-testing) |
| **File Laporan PDF** | [Laporan Tugas Kelompok 2 SQA - JUnit.pdf](./Laporan%20Tugas%20Kelompok%202%20SQA%20-%20JUnit.pdf) |

### Daftar Anggota Kelompok 2
| No | Nama Mahasiswa | NIM | Peran & Kontribusi |
| :-: | :--- | :---: | :--- |
| 1 | **Muhammad Rayhan Ramadhan** | `12409011010003` | Analisis 5W+1H, Implementasi Kelas `Calculator` & Unit Test JUnit 5 |
| 2 | **Arya Putra Fachreza** | `12409011010005` | Studi Literatur Tesis Selenium Internasional & Penyusunan Laporan |
| 3 | **Azka Azfar** | `12409011010008` | Verifikasi Skenario Uji Parameterized, Maven Setup & Review Dokumentasi |

---

## 📄 Dokumen Laporan Tugas

File laporan resmi kelompok dalam format PDF telah disertakan langsung di dalam branch ini:
* 📑 **Unduh / Buka Laporan:** [`Laporan Tugas Kelompok 2 SQA - JUnit.pdf`](./Laporan%20Tugas%20Kelompok%202%20SQA%20-%20JUnit.pdf)

---

## 📂 Struktur Direktori Repositori

Proyek ini mengikuti konvensi tata letak standar direktori **Apache Maven** (*Standard Directory Layout*):

```text
Kel2-SQA-King (branch: junit-sample-testing)
├── pom.xml                                      # Konfigurasi Maven dependencies & Surefire plugin
├── README.md                                    # Dokumentasi komprehensif proyek & hasil uji
├── Laporan Tugas Kelompok 2 SQA - JUnit.pdf     # Laporan resmi tugas kelompok
├── .gitignore                                   # File pengabaian build artifacts (target/, .class, IDE)
└── src/
    ├── main/
    │   └── java/
    │       └── com/
    │           └── rayhan/
    │               └── junit/
    │                   └── Calculator.java      # Kelas utama sistem kalkulator & grade mahasiswa
    └── test/
        └── java/
            └── com/
                └── rayhan/
                    └── junit/
                        └── CalculatorTest.java  # 11 skenario unit testing berbasis JUnit 5
```

---

## 📖 Bagian 1: Analisis 5W + 1H tentang JUnit

### 1. What (Apa itu JUnit?)
**JUnit** adalah sebuah framework pengujian unit (*unit testing framework*) yang bersifat *open-source* untuk bahasa pemrograman Java dan menjadi standar *de facto* dalam ekosistem Java Virtual Machine (JVM). JUnit merupakan bagian inti dari keluarga arsitektur xUnit (seperti NUnit untuk .NET, PyUnit/unittest untuk Python, dan PHPUnit untuk PHP).

Pada generasi terbarunya, yaitu **JUnit 5**, arsitektur sistem dipecah menjadi tiga sub-proyek independen yang modular:
1. **JUnit Platform:** Bertindak sebagai fondasi peluncuran (*launching framework*) di atas JVM. Menyediakan antarmuka `TestEngine`, *Console Launcher*, serta jembatan integrasi dengan *build tools* (Maven/Gradle) dan IDE.
2. **JUnit Jupiter:** Menyediakan model pemrograman baru (*programming model*) beserta anotasi modern (`@BeforeEach`, `@DisplayName`, `@ParameterizedTest`, `@Nested`) dan *extension model* untuk menulis pengujian di JUnit 5.
3. **JUnit Vintage:** Menyediakan `TestEngine` khusus untuk menjalankan pengujian berbasis **JUnit 3** dan **JUnit 4** di atas platform JUnit 5 demi menjaga kompatibilitas mundur (*backward compatibility*).

---

### 2. Who (Siapa Pencipta dan Pengguna JUnit?)
* **Pencipta:** JUnit pertama kali diciptakan oleh **Kent Beck** (pelopor *Extreme Programming* dan *Test-Driven Development*) bersama **Erich Gamma** (salah satu penulis buku legendaris *Design Patterns: Elements of Reusable Object-Oriented Software* / *Gang of Four*). Pengembangan JUnit 5 dipimpin oleh tim inti seperti Marc Philipp, Sam Brannen, Johannes Link, Matthias Merdes, dan Christian Stein bersama ratusan kontributor komunitas *open-source*.
* **Pengguna Utama:**
  * **Software Engineer / Backend Developer (Java/Kotlin):** Menguji fungsionalitas unit kode terkecil (fungsi, *method*, dan *class*) secara terisolasi.
  * **QA Automation Engineer & SDET:** Memanfaatkan JUnit sebagai *test runner* dan *assertion engine* yang diintegrasikan dengan Selenium WebDriver, Appium, maupun REST Assured.
  * **DevOps Engineer:** Mengonfigurasi otomatisasi pengujian sebagai gerbang penjamin mutu (*quality gate*) di dalam *pipeline* CI/CD.

---

### 3. When (Kapan JUnit Diciptakan dan Kapan Digunakan?)
* **Sejarah Waktu Penciptaan & Evolusi:**
  * **1997:** Kent Beck dan Erich Gamma menulis versi purwarupa pertama JUnit di dalam penerbangan pesawat menuju konferensi OOPSLA 1997 di Atlanta, AS.
  * **2006 (JUnit 4):** Memperkenalkan perubahan revolusioner berbasis anotasi Java 5 (`@Test`, `@Before`, `@After`), menggantikan pewarisan kelas `TestCase` dari JUnit 3.
  * **September 2017 (JUnit 5 - Sekarang):** Dirilis resmi dengan arsitektur modular terpisah dan dukungan penuh terhadap fitur Java 8+ (*lambda expressions*, *functional interfaces*, *streams*).
* **Waktu Penggunaan dalam SDLC (*Software Development Life Cycle*):**
  * **Saat menerapkan TDD (*Test-Driven Development*):** Tes disusun sebelum kode produksi dibuat (*Red - Green - Refactor*).
  * **Saat fase Coding & Refactoring:** Dijalankan setiap kali pengembang menambahkan fitur baru atau mengubah logika internal kode agar kode lama tidak rusak (*anti-regression*).
  * **Saat proses Build & Integrasi Berkelanjutan (CI):** Dijalankan otomatis di server setiap kali pengembang melakukan *push* atau membuat *Pull Request* di repositori.

---

### 4. Where (Di mana JUnit Dijalankan dan Diintegrasikan?)
JUnit berjalan di lingkungan JVM (*Java Virtual Machine*) dan terintegrasi luas pada berbagai perangkat pengembang:
* **IDE (Integrated Development Environment):** Didukung penuh dengan visual runner bawaan di IntelliJ IDEA, Eclipse IDE, VS Code (*Extension Pack for Java*), dan Apache NetBeans.
* **Build Automation Tools:** Terintegrasi langsung dengan Apache Maven (`maven-surefire-plugin`) dan Gradle (`useJUnitPlatform()`).
* **Pipeline CI/CD:** Dieksekusi pada server otomasi seperti GitHub Actions, GitLab CI, Jenkins, CircleCI, dan Travis CI.
* **Integrasi Framework:** Bekerja harmonis bersama Mockito (untuk *mocking* dependensi database/API), Spring Boot Test (`@SpringBootTest`), Selenium WebDriver (pengujian web UI), serta JaCoCo (pengukuran *code coverage*).

---

### 5. Why (Mengapa Menggunakan JUnit?)
1. **Deteksi Bug Lebih Awal (*Early Bug Detection*):** Kesalahan logika dapat ditemukan langsung di level method sebelum kode dideploy ke *staging* atau produksi, menghemat biaya perbaikan (*cost of defect*).
2. **Mencegah Regresi (*Regression Prevention*):** Menjamin bahwa perbaikan bug atau penambahan modul baru tidak merusak fungsi-fungsi yang telah berjalan sebelumnya.
3. **Kecepatan Eksekusi Tinggi:** Ratusan hingga ribuan skenario uji dapat dieksekusi hanya dalam hitungan milidetik secara otomatis tanpa intervensi manusia.
4. **Meningkatkan Arsitektur Kode:** Kode yang dirancang agar *testable* secara alami menerapkan prinsip *loose coupling*, *high cohesion*, serta *Single Responsibility Principle* (SRP).
5. **Dokumentasi Hidup (*Living Documentation*):** Menjadi spesifikasi teknis riil yang memperlihatkan bagaimana sebuah kelas dan metode berperilaku terhadap variasi input tertentu.

---

### 6. How (Bagaimana Cara Kerja dan Penggunaan JUnit?)
JUnit bekerja dengan mengeksekusi metode bertanda `@Test`, lalu memvalidasi kondisi aktual menggunakan serangkaian fungsi **Assertions**. Alur pengujian menerapkan pola standar **AAA (*Arrange - Act - Assert*)**:
1. **Arrange (Persiapan):** Menginisialisasi objek yang akan diuji (*System Under Test*) dan menyiapkan nilai masukan (biasanya ditempatkan di metode `@BeforeEach`).
2. **Act (Aksi):** Mengeksekusi metode target yang sedang diuji dengan parameter yang disiapkan.
3. **Assert (Verifikasi):** Membandingkan nilai kembalian aktual (*actual result*) terhadap ekspektasi yang diharapkan (*expected result*) melalui fungsi `assertEquals`, `assertTrue`, `assertThrows`, dll.
4. **Reporting (Pelaporan):** Test runner menangkap hasil pengujian. Jika assertion lolos, status ditandai **PASSED** (Hijau). Jika gagal, sistem melempar `AssertionFailedError` dan status ditandai **FAILED** (Merah).

---

## 📚 Bagian 2: Studi Literatur Tesis Internasional tentang Selenium (6 Tesis)

Berikut rangkuman komprehensif 6 karya ilmiah internasional (Skripsi & Tesis Magister) yang meneliti penerapan otomatisasi pengujian berbasis Selenium WebDriver:

| No | Institusi & Negara | Judul Penelitian | Penulis & Tahun | Fokus & Hasil Utama |
| :-: | :--- | :--- | :---: | :--- |
| **1** | **Karlstad University** *(Swedia)* | *An Automated Test System for Functional Testing of a Web Application Using BDD: Implementation Using SpecFlow, Selenium WebDriver, and NUnit in a Real-World Web Application Context* | Imal Bismellah (2025) | Menggantikan pengujian manual platform *ServeIT Online* di industri optik menggunakan Selenium WebDriver, SpecFlow, dan BDD (Gherkin). Berhasil mewujudkan otomatisasi lintas peramban (*cross-browser*) dan mempermudah kolaborasi dengan pemangku kepentingan non-teknis. |
| **2** | **Lund University** *(Swedia)* | *Automated Functional Tests for a Web Application* | Johan Wulf & Mark (2022) | Mengotomatisasi pengujian fungsional UI aplikasi internal penjadwalan IKEA (*MIA*) yang memiliki autentikasi kompleks Single Sign-On (SSO). Memadukan Selenium WebDriver dengan Mocha & Chai untuk memastikan keandalan *locator* dan verifikasi fitur *time-slot*. |
| **3** | **Dalarna University** *(Swedia)* | *Comparison of GUI Test Automation Strategies in a Clearing System: A Case Study at Nasdaq Stockholm AB* | Peneliti Komputer Högskolan Dalarna (2021) | Membandingkan efisiensi strategi pengujian GUI manual versus otomatisasi Selenium WebDriver pada *Clearing System* Nasdaq Stockholm AB. Menemukan bahwa meskipun biaya investasi awal skrip Selenium lebih tinggi, efisiensi eksekusi regresi jangka panjang jauh melampaui metode manual. |
| **4** | **Linköping University** *(Swedia)* | *Building a Selenium-based Data Collection Tool: Used for Identification and Evaluation of Cross-Website Relationships and Information Leakage* | Henrik Wendt & Matteus Henriksson (2020) | Merancang crawler otomatis berbasis Selenium WebDriver untuk menganalisis risiko kebocoran privasi pada interaksi antarsitus yang melibatkan Identity Providers (IDP/SSO) dan elemen dinamis JavaScript dengan tingkat presisi dan *recall* tinggi. |
| **5** | **Blekinge Institute of Technology** *(Swedia)* | *A Search-Based Approach for Robustness Testing of Web Applications* | Chappidi (2019) — *Kerja sama dengan Ericsson* | Mengintegrasikan algoritma evolusioner *Search-Based Software Testing* (NSGA-II) dengan Selenium WebDriver untuk membangkitkan kasus uji ketahanan (*robustness testing*) aplikasi web skala industri berdasarkan log akses riil. |
| **6** | **Blekinge Institute of Technology** *(Swedia)* | *Comparison of Different Techniques of Web GUI-based Testing with the Representative Tools Selenium and EyeSel* | Haozhen Jiang & Yi Chen (2017) | Eksperimen komparatif pada 50 situs web yang membandingkan Selenium WebDriver (*DOM property-based*) dengan EyeSel (*visual image recognition-based*). Menyimpulkan Selenium lebih unggul dalam portabilitas dan fungsionalitas, sementara teknik berbasis gambar unggul pada estetika tata letak visual. |

---

## 💻 Bagian 3: Implementasi Kode Program & Skenario Pengujian

Proyek ini mengimplementasikan pengujian fungsional pada kelas `Calculator.java` yang mencakup 6 operasi utama serta kelas penguji `CalculatorTest.java` dengan 11 skenario pengujian komprehensif.

### 1. Fitur & Anotasi JUnit 5 yang Digunakan
1. **`@BeforeEach`:** Menginstansiasi objek `Calculator` baru sebelum setiap skenario uji dimulai untuk menjaga isolasi state (*Arrange*).
2. **`@AfterEach`:** Mereset referensi objek `calculator = null` setelah setiap pengujian selesai dieksekusi (*Teardown*).
3. **`@DisplayName`:** Memberikan label deskriptif berbahasa Indonesia yang mudah dipahami pada laporan eksekusi test runner.
4. **`@Test`:** Menandai metode Java sebagai metode pengujian unit standar.
5. **`assertAll`:** Menjalankan beberapa *assertions* aritmatika secara bersamaan (*grouped assertions*) menggunakan lambda expression, sehingga seluruh pengecekan tetap dievaluasi meski salah satu gagal.
6. **`assertThrows`:** Memverifikasi penanganan eksepsi `IllegalArgumentException` ketika pembagi bernilai nol (`0`) atau nilai mahasiswa di luar batas `0 - 100`.
7. **`@ParameterizedTest` & `@CsvSource`:** Mengeksekusi satu skenario pengujian penentuan grade nilai secara berulang dengan variasi himpunan data uji input dan ekspektasi output.

---

### 2. Kode Program Utama (`src/main/java/com/rayhan/junit/Calculator.java`)

```java
package com.rayhan.junit;

public class Calculator {

    // 1. Operasi Penjumlahan
    public int tambah(int a, int b) {
        return a + b;
    }

    // 2. Operasi Pengurangan
    public int kurang(int a, int b) {
        return a - b;
    }

    // 3. Operasi Perkalian
    public int kali(int a, int b) {
        return a * b;
    }

    // 4. Operasi Pembagian dengan Validasi Pembagian Nol
    public double bagi(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Pembagi tidak boleh bernilai nol (0)!");
        }
        return (double) a / b;
    }

    // 5. Pengecekan Bilangan Genap
    public boolean apakahGenap(int angka) {
        return angka % 2 == 0;
    }

    // 6. Penentuan Grade Nilai Mahasiswa
    public String tentukanGrade(double nilai) {
        if (nilai < 0 || nilai > 100) {
            throw new IllegalArgumentException("Nilai harus berada di rentang 0 hingga 100!");
        }
        if (nilai >= 85) return "A";
        if (nilai >= 75) return "B";
        if (nilai >= 60) return "C";
        if (nilai >= 50) return "D";
        return "E";
    }
}
```

---

### 3. Kode Pengujian Unit (`src/test/java/com/rayhan/junit/CalculatorTest.java`)

```java
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
        // Arrange: Diinisialisasi ulang sebelum setiap method @Test dijalankan
        calculator = new Calculator();
    }

    @AfterEach
    void tearDown() {
        // Membersihkan objek setelah setiap tes selesai
        calculator = null;
    }

    @Test
    @DisplayName("1. Uji Penjumlahan Dua Bilangan Positif")
    void testTambah() {
        // Act
        int hasil = calculator.tambah(15, 25);
        // Assert
        assertEquals(40, hasil, "15 + 25 seharusnya menghasilkan 40");
    }

    @Test
    @DisplayName("2. Uji Pengurangan dan Perkalian Secara Berkelompok (assertAll)")
    void testKurangDanKali() {
        assertAll("Operasi Aritmatika Dasar",
            () -> assertEquals(10, calculator.kurang(25, 15), "25 - 15 harus 10"),
            () -> assertEquals(-5, calculator.kurang(10, 15), "10 - 15 harus -5"),
            () -> assertEquals(50, calculator.kali(10, 5), "10 * 5 harus 50"),
            () -> assertEquals(0, calculator.kali(99, 0), "Perkalian dengan 0 harus 0")
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
            () -> calculator.bagi(10, 0),
            "Pembagian dengan nol harus melempar IllegalArgumentException"
        );
        assertEquals("Pembagi tidak boleh bernilai nol (0)!", exception.getMessage());
    }

    @Test
    @DisplayName("5. Uji Pengecekan Bilangan Genap dan Ganjil")
    void testApakahGenap() {
        assertTrue(calculator.apakahGenap(12), "12 adalah bilangan genap");
        assertFalse(calculator.apakahGenap(13), "13 adalah bilangan ganjil");
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
    @DisplayName("7. Uji Nilai Mahasiswa di Luar Rentang (Negatif atau Lebih dari 100)")
    void testTentukanGradeTidakValid() {
        assertThrows(IllegalArgumentException.class, () -> calculator.tentukanGrade(-5));
        assertThrows(IllegalArgumentException.class, () -> calculator.tentukanGrade(105));
    }
}
```

---

### 4. Konfigurasi Maven (`pom.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.rayhan.junit</groupId>
    <artifactId>junit-sample-testing</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.jupiter.version>5.10.2</junit.jupiter.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.jupiter.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.5</version>
            </plugin>
        </plugins>
    </build>
</project>
```

---

## 🚀 Panduan Menjalankan Pengujian

### Prasyarat (*Prerequisites*)
* **Java Development Kit (JDK):** Versi 17 atau lebih baru (`java -version`)
* **Apache Maven:** Versi 3.6+ (`mvn -version`) *(opsional jika menggunakan IDE)*

### 1. Menggunakan Apache Maven CLI
Jalankan perintah berikut di direktori utama repositori:
```bash
mvn clean test
```

### 2. Menggunakan Visual Studio Code / IntelliJ IDEA
1. Buka folder repositori di IDE.
2. Navigasikan ke file `src/test/java/com/rayhan/junit/CalculatorTest.java`.
3. Klik tombol **Run Test (▶️)** di sebelah nama kelas `CalculatorTest` untuk mengeksekusi seluruh 11 skenario pengujian sekaligus.

---

## 📊 Hasil Eksekusi Pengujian (Test Results)

Pengujian telah dijalankan dan seluruh **11 skenario pengujian** (6 metode `@Test` dan 5 kombinasi `@ParameterizedTest`) **100% lolos (PASSED)** tanpa kegagalan maupun error.

### 1. Log Eksekusi Maven Surefire Plugin
```text
[INFO] Scanning for projects...
[INFO] -------------------< com.rayhan.junit:junit-sample-testing >-------------------
[INFO] Building junit-sample-testing 1.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-surefire-plugin:3.2.5:test (default-test) @ junit-sample-testing ---
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.rayhan.junit.CalculatorTest
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.084 s -- in com.rayhan.junit.CalculatorTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.612 s
[INFO] Finished at: 2026-11-09T21:29:32+07:00
[INFO] ------------------------------------------------------------------------
```

### 2. Log Eksekusi Hierarkis JUnit 5 Platform
```text
+-- JUnit Jupiter [OK]
| '-- Pengujian Unit Kelas Calculator dengan JUnit 5 [OK]
|   +-- 1. Uji Penjumlahan Dua Bilangan Positif [OK]
|   +-- 2. Uji Pengurangan dan Perkalian Secara Berkelompok (assertAll) [OK]
|   +-- 3. Uji Pembagian Normal [OK]
|   +-- 4. Uji Pembagian dengan Nol Harus Melempar Exception [OK]
|   +-- 5. Uji Pengecekan Bilangan Genap dan Ganjil [OK]
|   +-- 6. Uji Parameterized Penentuan Grade Nilai Mahasiswa [OK]
|   | +-- Nilai 90.0 menghasilkan Grade A [OK]
|   | +-- Nilai 80.0 menghasilkan Grade B [OK]
|   | +-- Nilai 65.0 menghasilkan Grade C [OK]
|   | +-- Nilai 55.0 menghasilkan Grade D [OK]
|   | '-- Nilai 40.0 menghasilkan Grade E [OK]
|   '-- 7. Uji Nilai Mahasiswa di Luar Rentang (Negatif atau Lebih dari 100) [OK]
+-- JUnit Vintage [OK]
'-- JUnit Platform Suite [OK]

Test run finished after 163 ms
[         5 containers found      ]
[         0 containers skipped    ]
[         5 containers started    ]
[         0 containers aborted    ]
[         5 containers successful ]
[         0 containers failed     ]
[        11 tests found           ]
[         0 tests skipped         ]
[        11 tests started         ]
[         0 tests aborted         ]
[        11 tests successful      ]
[         0 tests failed          ]
```

### 3. Matriks Hasil Pengujian
| No | Skenario Uji | Anotasi JUnit 5 | Input | Expected Output | Status |
| :-: | :--- | :--- | :--- | :--- | :-: |
| 1 | Uji Penjumlahan Dua Bilangan Positif | `@Test` | `15, 25` | `40` | **PASSED** ✅ |
| 2 | Pengurangan (25 - 15) | `@Test` (`assertAll`) | `25, 15` | `10` | **PASSED** ✅ |
| 3 | Pengurangan (10 - 15) | `@Test` (`assertAll`) | `10, 15` | `-5` | **PASSED** ✅ |
| 4 | Perkalian (10 * 5) | `@Test` (`assertAll`) | `10, 5` | `50` | **PASSED** ✅ |
| 5 | Perkalian dengan Nol (99 * 0) | `@Test` (`assertAll`) | `99, 0` | `0` | **PASSED** ✅ |
| 6 | Uji Pembagian Normal (10 / 4) | `@Test` | `10, 4` | `2.5` | **PASSED** ✅ |
| 7 | Uji Pembagian dengan Nol | `@Test` (`assertThrows`) | `10, 0` | `IllegalArgumentException` | **PASSED** ✅ |
| 8 | Uji Bilangan Genap & Ganjil | `@Test` | `12`, `13` | `true`, `false` | **PASSED** ✅ |
| 9 | Uji Grade Nilai Mahasiswa | `@ParameterizedTest` (`@CsvSource`) | `90.0, 80.0, 65.0, 55.0, 40.0` | `A`, `B`, `C`, `D`, `E` | **PASSED** ✅ |
| 10 | Uji Nilai Negatif (< 0) | `@Test` (`assertThrows`) | `-5` | `IllegalArgumentException` | **PASSED** ✅ |
| 11 | Uji Nilai Melebihi Batas (> 100) | `@Test` (`assertThrows`) | `105` | `IllegalArgumentException` | **PASSED** ✅ |

---

## 📝 Lisensi

Proyek ini disusun untuk tujuan akademik pada mata kuliah **Pengujian Perangkat Lunak**, Program Studi Teknik Informatika, UIN Syarif Hidayatullah Jakarta.
