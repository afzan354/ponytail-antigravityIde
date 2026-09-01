import os
import urllib.request
import zipfile
import shutil
import tempfile
import sys

def main():
    print("==================================================")
    print("   Ponytail Installer untuk Antigravity IDE       ")
    print("==================================================")
    print("[1/4] Mencari lokasi konfigurasi Antigravity...")

    # Tentukan path konfigurasi global
    user_home = os.path.expanduser("~")
    config_dir = os.path.join(user_home, ".gemini", "config")
    plugins_dir = os.path.join(config_dir, "plugins")
    rules_dir = os.path.join(config_dir, "rules")
    
    # Path target
    ponytail_plugin_dir = os.path.join(plugins_dir, "ponytail")
    ponytail_rule_file = os.path.join(rules_dir, "ponytail.md")

    # Buat direktori jika belum ada
    os.makedirs(plugins_dir, exist_ok=True)
    os.makedirs(rules_dir, exist_ok=True)

    # URL Source Code Ponytail
    zip_url = "https://github.com/dietrichgebert/ponytail/archive/refs/heads/main.zip"
    
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, "ponytail.zip")
        extract_path = os.path.join(temp_dir, "extracted")
        
        print(f"[2/4] Mengunduh repository Ponytail terbaru...")
        try:
            urllib.request.urlretrieve(zip_url, zip_path)
        except Exception as e:
            print(f"Error: Gagal mengunduh file. Pastikan internet Anda jalan. Detail: {e}")
            sys.exit(1)
            
        print("[3/4] Mengekstrak file dan memindahkan *skills*...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            
        # Folder di dalam zip dari github biasanya bernama "[repo_name]-[branch]"
        extracted_folder = os.path.join(extract_path, "ponytail-main")
        
        if not os.path.exists(extracted_folder):
            print("Error: Struktur file zip tidak sesuai harapan (folder 'ponytail-main' tidak ditemukan).")
            sys.exit(1)

        # Jika sebelumnya sudah terinstal, hapus dulu agar menimpa yang lama
        if os.path.exists(ponytail_plugin_dir):
            shutil.rmtree(ponytail_plugin_dir)

        # Pindahkan folder utuh ke folder plugins
        shutil.move(extracted_folder, ponytail_plugin_dir)

    print("[4/4] Mengaktifkan mode *Always-On* (Lazy Senior Dev)...")
    agents_md_path = os.path.join(ponytail_plugin_dir, "AGENTS.md")
    if os.path.exists(agents_md_path):
        shutil.copy2(agents_md_path, ponytail_rule_file)
    else:
        print(f"Peringatan: File AGENTS.md tidak ditemukan di {agents_md_path}. Aturan global mungkin tidak aktif.")

    print("\n==================================================")
    print(" INSTALASI SELESAI & BERHASIL!")
    print("==================================================")
    print(f"- Folder Plugin/Skills: {ponytail_plugin_dir}")
    print(f"- Rules Global aktif di: {ponytail_rule_file}")
    print("\nLangkah selanjutnya:")
    print("1. Tutup dan buka ulang (Restart) Antigravity IDE Anda.")
    print("2. Ketik '/ponytail-help' di chat baru untuk tes.")
    print("==================================================")

if __name__ == "__main__":
    main()
