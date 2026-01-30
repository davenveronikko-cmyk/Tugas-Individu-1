# Python Mini Projects  
## Replikasi dan Dokumentasi

---

## 1. Pendahuluan
Repositori ini berisi kumpulan **mini project Python** yang dikerjakan sebagai bagian dari **tugas individu** dengan pendekatan *replikasi berbasis pemahaman*. Proyek-proyek di dalam repositori ini mengacu pada materi video dan handbook *Python Projects for Beginners*.

Seluruh kode program yang di replikasi

- Disusun ulang agar lebih terstruktur
- Diberi komentar penjelasan


Repositori ini juga berfungsi sebagai **portofolio pembelajaran** untuk menunjukkan kemampuan dasar pemrograman Python dan praktik awal rekayasa perangkat lunak.

---

## 2. Tujuan Pengerjaan
Tujuan utama pengerjaan repositori ini adalah:
1. Memahami alur logika dan proses problem solving dalam proyek Python sederhana  
2. Melatih penggunaan struktur kontrol seperti percabangan dan perulangan  
3. Membiasakan penggunaan fungsi dan modularisasi kode  
4. Menerapkan struktur data yang sesuai (tuple, dictionary)  
5. Mengelola dependency menggunakan virtual environment  
6. Menyusun dokumentasi teknis dalam Bahasa Indonesia  

---

## 3. Daftar Proyek dan Penjelasan

### 3.1 Dice Rolling Game
Program simulasi lempar dadu yang meminta input pengguna untuk melanjutkan atau menghentikan permainan. Setiap lemparan menghasilkan dua angka acak antara 1 hingga 6.

**Tujuan Pembelajaran:**
- Memahami perulangan tak terbatas (`while`)
- Menggunakan input pengguna
- Menghasilkan bilangan acak

**Konsep Utama:**
- Loop
- Input/Output
- Modul 

---

### 3.2 Number Guessing Game
Permainan menebak angka di mana komputer memilih angka acak antara 1 sampai 100. Program memberikan umpan balik apakah tebakan terlalu kecil, terlalu besar, atau benar.

**Tujuan Pembelajaran:**
- Melatih logika percabangan
- Menangani kesalahan input pengguna

**Konsep Utama:**
- `if / elif / else`
- Perulangan
- Exception handling (`try-except`)

---

### 3.3 Rock, Paper, Scissors Game
Permainan Batu–Gunting–Kertas antara pengguna dan komputer. Pilihan komputer ditentukan secara acak dan hasil permainan ditampilkan menggunakan emoji.

Program ini disusun secara modular dengan fungsi-fungsi terpisah agar mudah dibaca dan dipelihara.

**Tujuan Pembelajaran:**
- Membiasakan penggunaan fungsi
- Memisahkan logika dan tampilan
- Validasi input pengguna

**Konsep Utama:**
- Fungsi
- Dictionary
- Tuple
- Modularisasi

---

### 3.4 QR Code Generator
Program untuk menghasilkan QR Code dari teks atau URL yang dimasukkan oleh pengguna. QR Code disimpan dalam bentuk file gambar.

Program ini menggunakan **library pihak ketiga** dan dijalankan di dalam **virtual environment**.

**Tujuan Pembelajaran:**
- Menggunakan library eksternal
- Mengelola dependency proyek
- Bekerja dengan file output

**Konsep Utama:**
- Virtual environment
- Dependency management
- Third-party library (`qrcode`)

---

### 3.5 Refactoring – Applying the DRY Principle
Tahap refactoring dilakukan pada program **Rock, Paper, Scissors** dengan tujuan menghilangkan duplikasi kode dan meningkatkan keterbacaan.

**Refactoring yang dilakukan:**
- Menggunakan konstanta sebagai satu sumber nilai
- Menghindari pengulangan kondisi logika
- Menggunakan dictionary untuk aturan permainan
- Menyederhanakan fungsi penentuan pemenang

**Tujuan Pembelajaran:**
- Memahami pentingnya refactoring
- Menerapkan prinsip DRY
- Menulis kode yang lebih mudah dirawat

---

## 4. Struktur Repositori
Struktur repositori disusun agar rapi dan mudah dipahami.



## Dokumentasi hasil ada di struktur folder docs/



## Cara Menjalankan Program

Bagian ini menjelaskan langkah-langkah untuk menjalankan seluruh program yang ada di repositori ini.

---

### 1. Persyaratan Sistem
Pastikan perangkat telah memenuhi persyaratan berikut:
- Python versi **3.8 atau lebih baru**
- Sistem operasi Windows, macOS, atau Linux
- Terminal / Command Prompt / PowerShell

(python --version)

2. Clone Repositori
Clone repositori ini ke komputer lokal:

bash
Copy code
git clone <url-repository-github>
Masuk ke folder proyek:

bash
Copy code
(cd python-mini-projects)

3. Membuat Virtual Environment
Virtual environment digunakan untuk mengisolasi dependency proyek.

bash
Copy code
(python -m venv venv)
Folder venv/ akan dibuat secara lokal dan tidak diunggah ke GitHub karena tercantum di .gitignore.

4. Mengaktifkan Virtual Environment
Windows (PowerShell / CMD)
bash
Copy code
(venv\Scripts\activate)
macOS / Linux
bash
Copy code
(source venv/bin/activate)
Jika berhasil, terminal akan menampilkan:

scss
Copy code
(venv)

5. Instalasi Dependency
Install seluruh library yang dibutuhkan menggunakan requirements.txt:

bash
Copy code
(pip install -r requirements.txt)
Dependency utama yang digunakan antara lain:

qrcode[pil] (untuk QR Code Generator)

6. Menjalankan Program
Setiap program dapat dijalankan secara terpisah dari folder src/.

a. Dice Rolling Game
bash
Copy code
(python src/dice_rolling/main.py)

b. Number Guessing Game
bash
Copy code
(python src/number_guessing/main.py)

c. Rock, Paper, Scissors Game
bash
Copy code
(python src/rock_paper_scissors/main.py)

d. QR Code Generator
## QR Code Generator – Cara Menjalankan

### Langkah Menjalankan
 Aktifkan virtual environment:
   (venv\Scripts\activate)
   
Install dependency:

bash
Copy code
(pip install -r requirements.txt)
Jalankan program:

bash
Copy code
(python src/qr_code_generator/qr_code_generator.py)
Masukkan teks atau URL, lalu nama file (contoh: qrcode.png).

Output
Program akan menghasilkan file QR Code dalam bentuk gambar yang dapat dipindai menggunakan kamera atau aplikasi QR scanner.

7. Menonaktifkan Virtual Environment

Setelah selesai menjalankan program, virtual environment dapat dinonaktifkan dengan perintah:

bash
Copy code
(deactivate)

8. Catatan Penting
Jika program tampak berhenti, kemungkinan sedang menunggu input pengguna
Jangan menekan Ctrl + C kecuali ingin menghentikan program
File hasil (misalnya QR Code) akan tersimpan di folder proyek sesuai nama file yang dimasukkan
