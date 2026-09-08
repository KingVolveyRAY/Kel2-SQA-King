# Portfolio Muhammad Rayhan Ramadhan

Website portfolio statis berbasis HTML, CSS, dan JavaScript vanilla. Tidak membutuhkan proses build sehingga mudah dijalankan dan dideploy.

## Menjalankan secara lokal

Buka `index.html` langsung di browser, atau gunakan server lokal sederhana:

```bash
python -m http.server 8000
```

Lalu buka [http://localhost:8000](http://localhost:8000).

## Mengaktifkan GitHub Pages

Workflow `.github/workflows/deploy-pages.yml` akan otomatis melakukan deploy setiap ada push ke branch `main`. Di repository GitHub, buka **Settings → Pages**, pilih **GitHub Actions** sebagai source, lalu push perubahan ke `main`. Workflow menggunakan artifact Pages resmi sehingga aman untuk repository project maupun situs pada subpath.
