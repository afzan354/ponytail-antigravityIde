# Dokumentasi Lengkap Penggunaan Ponytail di Antigravity IDE

## Apa itu Ponytail?
Ponytail adalah plugin (sekaligus *ruleset*) untuk AI Assistant yang memaksakan mode **"Lazy Senior Developer"**. "Malas" di sini bukan berarti lalai, melainkan **efisien**. Pendekatannya adalah: *Kode terbaik adalah kode yang tidak pernah ditulis*.

Ponytail memaksa AI untuk memberikan solusi paling sederhana, paling pendek, dan paling minimalis yang dapat berfungsi dengan baik, tanpa memotong aspek validasi, keamanan, atau aksesibilitas.

## Prinsip Utama (The Ladder)
Sebelum menulis kode apa pun, AI akan mematuhi prinsip hierarki (tangga) berikut, dan berhenti di titik pertama yang berhasil menjawab masalah:

1. **YAGNI (You Aren't Gonna Need It)**: Apakah fitur ini benar-benar harus dibuat sekarang? Jika tidak, lewati.
2. **Reuse**: Apakah sudah ada utilitas, pola, atau helper di dalam *codebase* ini? Jangan buat ulang.
3. **Standar Library (Stdlib)**: Apakah library bawaan bahasa pemrograman sudah bisa melakukannya? Gunakan itu.
4. **Native Feature**: Apakah fitur bawaan platform (misalnya menggunakan HTML `<input type="date">` alih-alih menginstal library kalender Javascript berat) sudah menyediakannya? Gunakan itu.
5. **Dependency yang Terinstal**: Apakah dependency yang sudah ada di proyek bisa menyelesaikannya? Gunakan itu.
6. **One-Liner**: Bisakah diselesaikan hanya dalam satu baris? Jadikan satu baris.
7. **Batas Akhir**: Jika semua hal di atas tidak terpenuhi, barulah tulis kode fungsional yang minimal.

## Fitur dan Perintah (Skills)
Karena Ponytail terinstal sebagai plugin di Antigravity, Anda dapat memanfaatkan perintah-perintah khusus (Skills) berikut dengan mengetikkannya di *prompt* chat Anda:

### 1. `/ponytail-review`
**Fungsi:** Mengulas kode yang baru saja ditambahkan atau diubah (*diff*), dengan fokus mencari abstraksi yang berlebihan (*over-engineering*). AI akan mendaftar apa saja yang bisa dipotong.
**Kapan digunakan:** Saat Anda merasa kode yang baru ditulis terlalu kompleks.

### 2. `/ponytail-audit`
**Fungsi:** Memindai **seluruh repositori/proyek** Anda. AI akan memberikan daftar peringkat (*ranked list*) tentang kode mana yang berpotensi dihapus, disederhanakan, atau diganti dengan standar library.
**Kapan digunakan:** Saat ingin merampingkan proyek, mencari *bloat*, atau melakukan *refactoring* kode lawas.

### 3. `/ponytail-debt`
**Fungsi:** Mengumpulkan semua komentar dengan awalan `ponytail:` di dalam proyek Anda menjadi sebuah rangkuman utang teknis (*technical debt*). 
**Kapan digunakan:** Jika AI mengambil jalan pintas terukur (dengan menulis komentar `ponytail:` tentang keterbatasan kode), perintah ini memungkinkan Anda melacak bagian-bagian tersebut agar bisa diperbaiki nantinya.

### 4. `/ponytail-gain`
**Fungsi:** Menampilkan metrik estimasi keberhasilan mode Ponytail berupa penghematan jumlah kode (LOC), penghematan biaya, dan penambahan kecepatan (*benchmark medians*).

### 5. `/ponytail-help`
**Fungsi:** Menampilkan panduan cepat (*quick-reference card*) dari mode, skill, dan perintah Ponytail.

## Di Balik Layar (Struktur Instalasi)
Sebagai info, konfigurasi yang membuat ini berjalan di sistem Anda:
- **Aturan Permanen (Always-On):** Instruksi panduan *mindset* "Lazy Senior Dev" tertanam di file `C:\Users\hp\.gemini\config\rules\ponytail.md`. Karenanya, sifat pelit-kode ini akan selalu aktif di latar belakang.
- **Kumpulan Plugin (Skills):** Modul perintah (`/ponytail-audit`, dll) ada di folder `C:\Users\hp\.gemini\config\plugins\ponytail`.

## Tips Penggunaan
- **Katakan Saja:** Walau ia selalu berjalan, Anda juga bisa memicu *mindset* secara eksplisit dengan memasukkan kata kunci di *prompt*: *"ponytail"*, *"be lazy"*, *"simplest solution"*, *"minimal solution"*, *"yagni"*, atau *"shortest path"*.
- **Fokus Akar Masalah:** Saat memperbaiki bug, Ponytail akan mencari akar penyebab fungsi yang dipanggil, bukan sekadar menambal bug di permukaannya.
- **Dengarkan Pertanyaannya:** Jika AI tiba-tiba bertanya, *"Apakah Anda benar-benar membutuhkan fitur kompleks X ini, atau apakah fitur dasar Y sudah cukup mencakupnya?"*, itu tandanya mode YAGNI sedang bekerja. Pertimbangkan saran penyederhanaannya.

---
*"He says nothing. He writes one line. It works."*
