# Portfolio Muhammad Rayhan Ramadhan

Website portfolio statis Muhammad Rayhan Ramadhan. Situs ini menampilkan profil, pengalaman organisasi dan robotika, pendidikan, sertifikat, keahlian, serta informasi kontak dalam layout yang responsif.

## Fitur

- Hero section dan ringkasan profil.
- Pengalaman, pendidikan, sertifikat, keahlian, dan kontak.
- Navigasi mobile tanpa dependensi JavaScript tambahan.
- Deploy otomatis ke GitHub Pages melalui GitHub Actions.

## Teknologi

- HTML5
- CSS3
- JavaScript vanilla
- Google Fonts: Manrope dan DM Mono
- GitHub Actions dan GitHub Pages

## Prasyarat

- Browser modern untuk membuka situs.
- Python 3 jika ingin menjalankan server lokal dengan perintah di bawah.

Tidak ada package manager, dependency lokal, database, atau konfigurasi environment yang diperlukan.

## Menjalankan secara lokal

Buka `index.html` langsung di browser, atau jalankan server lokal:

```bash
python -m http.server 8000
```

Lalu buka [http://localhost:8000](http://localhost:8000).

## Struktur folder

```text
.
├── index.html                       # Markup dan konten portfolio
├── styles.css                       # Layout, warna, tipografi, dan responsive design
├── script.js                        # Toggle navigasi pada layar kecil
├── .github/workflows/
│   └── deploy-pages.yml             # Workflow deploy ke GitHub Pages
└── README.md                        # Dokumentasi proyek
```

## Mengaktifkan GitHub Pages

1. Buka **Settings → Pages** pada repository GitHub.
2. Pilih **GitHub Actions** sebagai source.
3. Push perubahan ke branch `main`.

Workflow `.github/workflows/deploy-pages.yml` akan menjalankan `actions/configure-pages`, membuat artifact dari root repository, lalu mendeploy artifact tersebut dengan `actions/deploy-pages`. Workflow menggunakan permission `pages: write` dan `id-token: write` yang dibutuhkan oleh GitHub Pages.

## Kontribusi dan lisensi

Perubahan dapat diajukan melalui pull request ke branch `main`. Repository ini belum menyediakan file lisensi.
