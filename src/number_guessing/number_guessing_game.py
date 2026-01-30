import random
# Mengimpor modul random
# Digunakan untuk menghasilkan angka acak yang akan ditebak oleh pengguna

number_to_guess = random.randint(1, 100)
# Menghasilkan satu angka acak antara 1 sampai 100
# Angka ini adalah target yang harus ditebak oleh pengguna

while True:
    # Loop tak hingga
    # Program akan terus berjalan sampai pengguna menebak angka dengan benar

    try:
        # Blok try digunakan untuk menangani kemungkinan error
        # Terutama saat input tidak bisa dikonversi menjadi angka

        guess = int(input('Guess the number between 1 and 100: '))
        # Meminta input dari pengguna
        # Input dikonversi menjadi integer menggunakan int()

        if guess < number_to_guess:
            # Jika tebakan lebih kecil dari angka target
            print('Too low!')
            # Memberi petunjuk bahwa angka terlalu kecil

        elif guess > number_to_guess:
            # Jika tebakan lebih besar dari angka target
            print('Too high!')
            # Memberi petunjuk bahwa angka terlalu besar

        else:
            # Jika tebakan sama dengan angka target
            print('Congratulations! You guessed the number.')
            # Menampilkan pesan kemenangan
            break
            # Menghentikan loop dan mengakhiri program

    except ValueError:
        # Blok except dijalankan jika terjadi error ValueError
        # Error ini terjadi ketika input bukan angka (misalnya huruf)
        print('Please enter a valid number')
        # Menampilkan pesan kesalahan tanpa menghentikan program
