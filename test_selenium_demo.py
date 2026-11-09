import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def jalankan_pengujian_selenium():
    print("=" * 60)
    print("MEMULAI PENGUJIAN OTOMATIS SELENIUM WEBDRIVER")
    print("=" * 60)

    # 1. Konfigurasi Browser Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Catatan: Jangan gunakan --headless saat merekam video agar browser terlihat!

    # Inisialisasi WebDriver (Selenium 4 otomatis mengelola ChromeDriver)
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # 2. Navigasi ke Halaman Target Pengujian (SauceDemo)
        url_target = "https://www.saucedemo.com/"
        print(f"[STEP 1] Membuka halaman web: {url_target}")
        driver.get(url_target)
        time.sleep(1.5)  # Jeda visual agar mudah diamati saat rekaman presentasi

        # Verifikasi Judul Halaman (Assertion 1)
        judul_halaman = driver.title
        print(f"         Judul halaman terdeteksi: '{judul_halaman}'")
        assert "Swag Labs" in judul_halaman, "Judul halaman tidak sesuai!"

        # 3. Proses Input Kredensial Login secara Otomatis
        print("[STEP 2] Mengisi form Username dan Password...")
        input_user = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        input_pass = driver.find_element(By.ID, "password")
        tombol_login = driver.find_element(By.ID, "login-button")

        input_user.clear()
        input_user.send_keys("standard_user")
        time.sleep(1)

        input_pass.clear()
        input_pass.send_keys("secret_sauce")
        time.sleep(1)

        print("[STEP 3] Mengklik tombol Login...")
        tombol_login.click()
        time.sleep(2)

        # 4. Validasi Berhasil Masuk ke Halaman Katalog Produk (Assertion 2)
        header_produk = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        teks_header = header_produk.text
        print(f"[STEP 4] Verifikasi halaman setelah login -> Header: '{teks_header}'")
        assert teks_header == "Products", "Gagal masuk ke halaman katalog produk!"

        # 5. Interaksi Tambah Produk ke Keranjang Belanja
        print("[STEP 5] Menambahkan produk 'Sauce Labs Backpack' ke keranjang...")
        tombol_beli = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        tombol_beli.click()
        time.sleep(1.5)

        # 6. Verifikasi Badge Keranjang Belanja Bertambah (Assertion 3)
        badge_keranjang = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        jumlah_item = badge_keranjang.text
        print(f"[STEP 6] Jumlah item di keranjang saat ini: {jumlah_item} item")
        assert jumlah_item == "1", "Jumlah item di keranjang tidak sesuai!"

        # 7. Mengambil Bukti Tangkapan Layar (Screenshot)
        nama_screenshot = "hasil_uji_selenium.png"
        driver.save_screenshot(nama_screenshot)
        print(f"[STEP 7] Bukti pengujian berhasil disimpan ke: {nama_screenshot}")

        print("-" * 60)
        print("STATUS AKHIR: SEMUA TEST CASE BERHASIL (PASSED 100%)")
        print("-" * 60)

    except AssertionError as e:
        print(f"[TEST FAILED] Kegagalan Validasi: {e}")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan sistem saat eksekusi: {e}")
    finally:
        time.sleep(2)
        print("[INFO] Menutup sesi browser Selenium WebDriver...")
        driver.quit()

if __name__ == "__main__":
    jalankan_pengujian_selenium()