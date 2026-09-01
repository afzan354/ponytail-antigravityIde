# Ponytail Installer for Antigravity IDE

Repositori ini berisi sekumpulan *tools* dan dokumentasi untuk mempermudah pemasangan plugin **Ponytail (Lazy Senior Dev Mode)** ke dalam **Antigravity IDE**. 

Ponytail akan mengubah perilaku AI Assistant Anda menjadi sangat efisien dengan memaksa prinsip YAGNI (*You Aren't Gonna Need It*). Ia akan selalu menghasilkan kode seminimal mungkin—demi menghemat *token*, menekan biaya, mempercepat *response*, serta menghindari *over-engineering*.

## 📂 Isi Repositori

Repositori ini memuat tiga buah file utama:

1. **[`install_ponytail.py`](./install_ponytail.py)**
   Skrip CLI (berbasis Python) yang secara **otomatis** mengunduh, mengekstrak, dan memasang plugin Ponytail beserta aturan *always-on* ke konfigurasi global Antigravity di sistem Anda. Skrip lintas platform ini bisa dijalankan di Windows, Linux, maupun macOS.
   
2. **[`docs_ponytail.md`](./docs_ponytail.md)**
   Dokumentasi serta referensi mendalam tentang apa itu Ponytail, prinsip kerjanya (*The Ladder*), hingga penjelasan tentang cara menggunakan perintah (*skills*) bawaannya seperti `/ponytail-review` dan `/ponytail-audit`.

3. **[`docs_install_ponytail_antigrav_ide.md`](./docs_install_ponytail_antigrav_ide.md)**
   Panduan langkah demi langkah jika Anda lebih memilih melakukan instalasi secara **manual** (tanpa menggunakan skrip otomatis di atas). Panduan ini juga menjabarkan di mana saja letak folder konfigurasi Antigravity pada sistem operasi Anda.

---

## 🚀 Cara Menggunakan Skrip Instalasi Otomatis

Anda hanya perlu memastikan bahwa [Python](https://www.python.org/downloads/) telah terinstal di komputer Anda.

1. Buka Terminal (Linux/Mac) atau Command Prompt / PowerShell (Windows).
2. Unduh (*clone*) repositori ini dan masuk ke dalam foldernya.
3. Jalankan perintah berikut:
   ```bash
   python install_ponytail.py
   ```
4. Skrip akan berjalan selama beberapa detik untuk mengonfigurasi direktori `~/.gemini/config` (folder profil Antigravity) milik Anda.
5. Setelah skrip memberikan pesan *Instalasi Selesai*, tutup dan buka ulang (Restart) Antigravity IDE Anda.

---

## ✅ Verifikasi Instalasi

Untuk memastikan Ponytail sudah bekerja dengan sempurna:
1. Buka sesi *chat* baru di Antigravity IDE.
2. Ketik perintah `/ponytail-help` di kotak pesan. 
3. Jika AI membalas dengan panduan cepat mengenai mode Ponytail, berarti instalasi telah sukses 100%! Anda siap menggunakannya untuk meninjau *bloat code* di proyek Anda.

---
*"He says nothing. He writes one line. It works."*
