# Panduan Lengkap Instalasi Manual Ponytail di Antigravity IDE

Panduan ini akan menjelaskan langkah-langkah manual untuk memasang plugin **Ponytail (Lazy Senior Dev Mode)** di Antigravity IDE agar sifat efisien dan hemat token ini berlaku secara global di semua proyek/percakapan Anda.

## Prasyarat
- Anda telah menginstal Antigravity IDE.
- Anda memiliki koneksi internet untuk mengunduh *source code* Ponytail.
- Anda mengerti cara membuka File Explorer atau Terminal.

---

## Langkah 1: Akses Direktori Konfigurasi Global Antigravity
Antigravity IDE menyimpan konfigurasi, plugin, dan aturannya di dalam direktori tersembunyi (hidden directory) pada profil komputer Anda.

- **Windows:** `C:\Users\<Username_Anda>\.gemini\config`
- **Mac/Linux:** `~/.gemini/config`

*(Ganti `<Username_Anda>` dengan nama profil di komputer yang Anda gunakan)*

Buka direktori tersebut. Jika di dalamnya belum terdapat folder bernama `plugins` dan `rules`, buatlah kedua folder tersebut secara manual.

---

## Langkah 2: Unduh dan Pasang Plugin Ponytail
Plugin Ponytail akan memberikan sekumpulan *skills* seperti `/ponytail-review` dan `/ponytail-audit`.

1. Kunjungi repositori resmi Ponytail di GitHub: [https://github.com/dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail)
2. Klik tombol **Code** yang berwarna hijau, lalu pilih **Download ZIP**.
3. Ekstrak file ZIP yang berhasil diunduh. Anda akan mendapatkan folder bernama `ponytail-main`.
4. Ganti nama folder tersebut (Rename) menjadi hanya **`ponytail`**.
5. Pindahkan folder `ponytail` tersebut ke dalam direktori `plugins` yang telah Anda siapkan di Langkah 1.
   - Hasil akhir path-nya: `.../.gemini/config/plugins/ponytail/`
   - Pastikan di dalam folder tersebut Anda bisa melihat file bernama `plugin.json`, `AGENTS.md`, dan folder `skills/`.

**Alternatif Jika Menggunakan Terminal (Git):**
```bash
# Masuk ke folder plugins
cd ~/.gemini/config/plugins

# Kloning repositori
git clone https://github.com/dietrichgebert/ponytail
```

---

## Langkah 3: Aktifkan Aturan "Selalu Aktif" (Always-On)
Langkah ini sangat penting agar AI otomatis membaca instruksi "bekerja efisien ala Senior Developer" setiap kali Anda membuka *chat* baru, tanpa perlu Anda ingatkan terus-menerus.

1. Buka folder `ponytail` yang baru saja Anda pindahkan (di dalam folder `plugins`).
2. Cari file bernama **`AGENTS.md`**.
3. Salin (Copy) file tersebut.
4. Kembali ke atas (ke folder `config`), lalu masuk ke dalam folder **`rules`**.
5. Tempel (Paste) file tersebut ke dalam folder `rules`.
6. Ganti nama (Rename) file yang baru di-paste tersebut dari `AGENTS.md` menjadi **`ponytail.md`**.
   - Hasil akhir path-nya: `.../.gemini/config/rules/ponytail.md`

*(Dengan ini, Antigravity akan memperlakukan instruksi tersebut sebagai aturan wajib global)*.

---

## Langkah 4: Mulai Ulang (Restart) Antigravity IDE
Agar Antigravity dapat memindai folder global yang baru Anda modifikasi, Anda wajib memuat ulang IDE tersebut. 
- Anda bisa menutup dan membuka kembali Antigravity IDE.
- Atau, Anda bisa membuat sesi obrolan (Chat Session) yang benar-benar baru.

---

## Langkah 5: Uji Coba dan Verifikasi
Untuk memastikan Ponytail sudah bekerja 100%:
1. Buka Chat, lalu ketikkan: `/ponytail-help`
2. Jika terinstal dengan benar, AI akan membalas dengan daftar panduan singkat mengenai fungsi *skills* Ponytail.
3. Anda juga bisa mencoba mengujinya dalam konteks *coding*. Misalnya katakan ke AI: *"Buatkan saya HTML input untuk date picker"*. 
   - Jika AI merespons dengan satu baris `<input type="date">` alih-alih membuatkan komponen besar dengan library *Javascript* atau *React*, berarti **Mode Ponytail telah aktif sempurna!**

Selamat, Anda dan teman-teman Anda sekarang siap memangkas *bloat code* dan menghemat penggunaan token!
