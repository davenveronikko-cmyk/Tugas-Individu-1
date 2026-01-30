import random  
# Mengimpor modul random
# Digunakan untuk menghasilkan angka acak (simulasi dadu)

while True:
    # Loop tak hingga
    # Program akan terus berjalan sampai dihentikan dengan perintah 'break'

    choice = input('Roll the dice? (y/n): ').lower()
    # Meminta input dari pengguna
    # .lower() digunakan agar input 'Y' atau 'y' dianggap sama

    if choice == 'y':
        # Kondisi jika pengguna memilih untuk melempar dadu

        die1 = random.randint(1, 6)
        # Menghasilkan angka acak antara 1 sampai 6 untuk dadu pertama

        die2 = random.randint(1, 6)
        # Menghasilkan angka acak antara 1 sampai 6 untuk dadu kedua

        print(f'({die1}, {die2})')
        # Menampilkan hasil lemparan dua dadu

    elif choice == 'n':
        # Kondisi jika pengguna memilih untuk berhenti bermain

        print('Thanks for playing!')
        # Menampilkan pesan penutup

        break
        # Menghentikan loop dan mengakhiri program

    else:
        # Kondisi jika input bukan 'y' atau 'n'

        print('Invalid choice!')
        # Menampilkan pesan kesalahan dan mengulang loop
