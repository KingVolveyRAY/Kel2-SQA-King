# 🧪 JUnit 5 Sample Testing Project

Repositori ini berisi implementasi sampel pengujian unit (*unit testing*) menggunakan **JUnit 5 (JUnit Jupiter)** dan **Apache Maven** pada bahasa pemrograman Java. Proyek ini disusun secara berkelompok untuk memenuhi tugas mata kuliah **Pengujian Perangkat Lunak**.

## 👥 Anggota Kelompok & Informasi Mata Kuliah

### Daftar Anggota Kelompok
| No | Nama Mahasiswa | NIM |
| :-: | :--- | :--- |
| 1 | **Muhammad Rayhan Ramadhan** | 12409011010003 |
| 2 | **Arya Putra Fachreza** | 12409011010005 |
| 3 | **Azka Azfar** | 12409011010008 |

### Detail Mata Kuliah
| Keterangan | Detail |
| :--- | :--- |
| **Program Studi** | Teknik Informatika — UIN Syarif Hidayatullah Jakarta |
| **Dosen Pengampu** | Pak Broer |
| **Topik Tugas** | Analisis 5W+1H JUnit, Studi Literatur Tesis Selenium, & Implementasi Sample JUnit 5 |
| **Repositori GitHub** | [https://github.com/KingVolveyRAY/junit-sample-testing](https://github.com/KingVolveyRAY) |

---

## ✨ Fitur & Konsep JUnit 5 yang Diimplementasikan

Proyek ini menguji kelas `Calculator.java` yang mencakup operasi aritmatika dasar, validasi pembagian dengan nol, pengecekan bilangan genap/ganjil, serta konversi nilai angka mahasiswa menjadi *grade* huruf (`A` hingga `E`).

Konsep dan fitur **JUnit 5** yang didemonstrasikan di dalam `CalculatorTest.java` meliputi:

1. **Test Lifecycle Annotations:**
   * `@BeforeEach`: Menginisialisasi objek `Calculator` baru sebelum setiap metode pengujian dieksekusi (*Arrange*).
   * `@AfterEach`: Membersihkan referensi objek setelah pengujian selesai dijalankan.
2. **Standard & Custom Display Annotations:**
   * `@Test`: Menandai metode sebagai unit pengujian.
   * `@DisplayName`: Memberikan nama deskriptif yang mudah dibaca pada laporan hasil pengujian.
3. **Grouped Assertions (`assertAll`):**
   * Mengeksekusi beberapa *assertion* sekaligus menggunakan *lambda expressions* sehingga seluruh pengujian dalam satu grup tetap dievaluasi meskipun salah satu gagal.
4. **Exception Testing (`assertThrows`):**
   * Memverifikasi bahwa metode melempar `IllegalArgumentException` dengan pesan kesalahan yang tepat ketika terjadi pembagian dengan angka nol (`0`) atau input nilai di luar rentang `0 - 100`.
5. **Parameterized Tests (`@ParameterizedTest` & `@CsvSource`):**
   * Menjalankan satu metode pengujian berulang kali dengan berbagai kombinasi data input dan ekspektasi output untuk menguji konversi *grade* nilai mahasiswa secara efisien.

---

## 📂 Struktur Direktori Proyek

```text
junit-sample-testing/
├── pom.xml
├── README.md
└── src/
    ├── main/
    │   └── java/
    │       └── com/
    │           └── rayhan/
    │               └── junit/
    │                   └── Calculator.java
    └── test/
        └── java/
            └── com/
                └── rayhan/
                    └── junit/
                        └── CalculatorTest.java
```

---

## ⚙️ Prasyarat (Prerequisites)

Pastikan perangkat Anda telah terinstal:
* **Java Development Kit (JDK):** Versi 17 atau lebih baru (`java -version`)
* **Apache Maven:** Versi 3.6+ (`mvn -version`)
* **IDE (Opsional):** IntelliJ IDEA, Visual Studio Code (*Extension Pack for Java*), atau Eclipse IDE

---

## 🚀 Cara Menjalankan Pengujian

### 1. Clone Repositori
```bash
git clone https://github.com/KingVolveyRAY/junit-sample-testing.git
cd junit-sample-testing
```

### 2. Jalankan Unit Test Melalui Terminal (Maven)
Jalankan perintah berikut pada direktori utama proyek:
```bash
mvn test
```

### 3. Jalankan Melalui IDE (VS Code / IntelliJ IDEA)
1. Buka folder `junit-sample-testing` di IDE Anda.
2. Buka file `src/test/java/com/rayhan/junit/CalculatorTest.java`.
3. Klik ikon **Run Test** (▶️) di sebelah deklarasi `class CalculatorTest` untuk menjalankan seluruh skenario uji sekaligus.

---

## 📊 Contoh Output Hasil Pengujian

Ketika seluruh 11 skenario pengujian (6 metode `@Test` reguler + 5 skenario `@ParameterizedTest`) dijalankan, Maven Surefire Plugin akan menampilkan hasil berikut:

```text
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.rayhan.junit.CalculatorTest
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.084 s -- in com.rayhan.junit.CalculatorTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
```

---

## 📚 Ringkasan Materi Tugas

### Ringkasan 5W + 1H JUnit
* **What:** *Framework unit testing open-source* standar untuk bahasa pemrograman Java di atas ekosistem JVM (terdiri atas *JUnit Platform*, *JUnit Jupiter*, dan *JUnit Vintage*).
* **Who:** Pertama kali dirancang oleh **Kent Beck** dan **Erich Gamma**, serta digunakan oleh *Software Developer*, *QA Automation Engineer*, dan *DevOps Engineer*.
* **When:** Diciptakan pada tahun 1997, berevolusi menjadi JUnit 4 (2006) dan JUnit 5 (2017–sekarang). Digunakan saat menerapkan TDD (*Test-Driven Development*), *coding/refactoring*, dan di *pipeline* CI/CD.
* **Where:** Dijalankan di atas JVM melalui IDE (IntelliJ, VS Code, Eclipse), *build tools* (Maven, Gradle), maupun server CI/CD (GitHub Actions, Jenkins).
* **Why:** Mendeteksi *bug* lebih dini, mencegah *regression bug*, mempercepat verifikasi kode secara otomatis, dan mendorong desain kode yang modular.
* **How:** Menerapkan pola **AAA (*Arrange - Act - Assert*)** menggunakan anotasi `@Test` dan memverifikasi ekspektasi output melalui metode *Assertions*.

### Daftar Referensi Skripsi / Tesis Internasional tentang Selenium
1. **Bismellah, I. (2025).** *An Automated Test System for Functional Testing of a Web Application Using BDD: Implementation Using SpecFlow, Selenium WebDriver, and NUnit in a Real-World Web Application Context*. Karlstad University, Sweden.
2. **Wulf, J., & Mark. (2022).** *Automated Functional Tests for a Web Application*. Lund University, Sweden.
3. **Dalarna University. (2021).** *Comparison of GUI Test Automation Strategies in a Clearing System: A Case Study at Nasdaq Stockholm AB*. Högskolan Dalarna, Sweden.
4. **Wendt, H., & Henriksson, M. (2020).** *Building a Selenium-based Data Collection Tool: Used for Identification and Evaluation of Cross-Website Relationships and Information Leakage*. Linköping University, Sweden.
5. **Chappidi. (2019).** *A Search-Based Approach for Robustness Testing of Web Applications*. Blekinge Institute of Technology (BTH), Sweden.
6. **Jiang, H., & Chen, Y. (2017).** *Comparison of Different Techniques of Web GUI-based Testing with the Representative Tools Selenium and EyeSel*. Blekinge Institute of Technology (BTH), Sweden.

---

## 📝 Lisensi

Proyek ini dibuat untuk tujuan akademik dan pembelajaran pada mata kuliah Pengujian Perangkat Lunak.
