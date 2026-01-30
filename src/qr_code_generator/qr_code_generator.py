import qrcode
# Mengimpor library qrcode
# Library ini digunakan untuk membuat dan memproses QR Code
# berdasarkan data teks atau URL yang diberikan pengguna.

data = input('Enter the text or URL: ').strip()
# Meminta input berupa teks atau URL dari pengguna.
# Method strip() digunakan untuk menghapus spasi di awal dan akhir input
# agar data yang diproses lebih bersih dan konsisten.

filename = input('Enter the filename: ').strip()
# Meminta nama file untuk menyimpan QR Code.
# strip() digunakan untuk menghindari kesalahan akibat spasi tidak disengaja.

qr = qrcode.QRCode(box_size=10, border=4)
# Membuat objek QRCode.
# box_size menentukan ukuran setiap kotak pada QR Code.
# border menentukan ketebalan batas (quiet zone) di sekitar QR Code.
# Parameter ini memengaruhi kualitas dan keterbacaan QR Code.

qr.add_data(data)
# Menambahkan data (teks atau URL) ke dalam objek QR Code.
# Data ini akan dikodekan menjadi pola QR.

image = qr.make_image(fill_color='black', back_color='white')
# Menghasilkan gambar QR Code berdasarkan data yang telah ditambahkan.
# fill_color menentukan warna QR Code.
# back_color menentukan warna latar belakang QR Code.

image.save(filename)
# Menyimpan gambar QR Code ke dalam file sesuai nama yang diberikan pengguna.

print(f'QR code saved as {filename}')
# Menampilkan pesan konfirmasi bahwa QR Code berhasil dibuat dan disimpan.
