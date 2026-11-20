# PLP Tree-sitter 

## Projek Selesai
Repositori ini menyangkut coursework yang sudah selesai untuk materi Tree-sitter, mencakup 6 tugas praktik dan mini-proyek. Kinerja menunjukkan pemahaman terhadap trees syntaks, penulisan query, grammar development, dan analisis kode menggunakan tree-sitter.

## Struktur Pengumpulan
Setiap folder memiliki isi sebagai berikut:

- **`tugas1-3/`**  Skrip Python dan file `.scm`, serta output dalam `.txt` untuk Tugas 1–3.
- **`tree-sitter-filter/`** `grammar.js`, `test/corpus/`, `queries/highlights.scm` (Tugas 4–5).
- **`cek/`**  `cek.py` dan `README.md` (Tugas 6).
- **`laporan.pdf`**  Maksimal 3 halaman: tangkapan layar hasil, penjelasan tiap tugas, kendala & solusi, serta *catatan penggunaan AI*.
- **`proposal-draf.pdf`**  Draf proposal proyek (maksimal 1 halaman), tidak dinilai tetapi mendapat umpan balik.

## Struktur File
```text
.
├── tugas1-3/
├── tree-sitter-filter/
├── cek/
├── laporan.pdf
└── proposal-draf.pdf
```

## Instalasi Tree-sitter untuk Python dan Pembuatan Venv
Untuk menjalankan tugas-tugas ini, dibutuhkan environment Python dengan library tree-sitter. Ikuti langkah-langkah berikut:

#### 1. Install Tree-sitter CLI (wajib)
```bash
# Menggunakan pip (disarankan untuk Python 3.10+)
pip install tree-sitter-cli

# Atau menggunakan cargo (jika Anda menggunakan Rust)
cargo install tree-sitter-cli
```

#### 2. Install Library Python
```bash
pip install tree-sitter tree-sitter-python tree-sitter-javascript
```

#### 3. Buat Virtual Environment (venv)  Disarankan
Membuat venv mencegah konflik dependensi dengan proyek Python lain:

```bash
# Buat venv bernama .venv
python -m venv .venv

# Aktifkan venv
# Di Linux/macOS:
source .venv/bin/activate

# Di Windows:
.\.venv\Scripts\activate

# Setelah diaktifkan, install ulang library ke venv ini
pip install tree-sitter tree-sitter-python tree-sitter-javascript
```

#### 4. Verifikasi Instalasi
```bash
# Cek versi tree-sitter
tree-sitter --version

# Cek library Python bisa diimpor
python -c "import tree_sitter_python; print('Berhasil!')"
```

#### 5. Contoh Jalan Lengkap di Linux (Arch/Debian):
```bash
# Instal compiler C dan dependency
sudo apt install build-essential # di Debian
# atau
sudo pacman -S base-devel # di Arch Linux

# Install tree-sitter CLI
pip install tree-sitter-cli

# Install library Python
pip install tree-sitter tree-sitter-python tree-sitter-javascript

# Buat dan aktifkan venv
python -m venv .venv
source .venv/bin/activate

# Install ulang library ke venv (opsional tapi disarankan)
pip install -r requirements.txt  # jika ada file requirements

# Jalankan tugas
python cek.py test/
```
