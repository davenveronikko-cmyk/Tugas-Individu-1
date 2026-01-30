import random
# Mengimpor modul random
# Digunakan untuk menentukan pilihan komputer secara acak

# Konstanta pilihan permainan
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
# Konstanta digunakan agar nilai pilihan tidak ditulis berulang
# serta meningkatkan keterbacaan kode (prinsip DRY)

# Dictionary untuk memetakan pilihan ke emoji
emojis = {
    ROCK: '🪨',      # Representasi batu
    SCISSORS: '✂️',  # Representasi gunting
    PAPER: '📃'      # Representasi kertas
}
# Dictionary digunakan untuk memisahkan logika permainan
# dari tampilan output

# Tuple berisi semua pilihan yang valid
choices = tuple(emojis.keys())
# Tuple dipilih karena bersifat immutable (tidak dapat diubah)
# dan aman digunakan sebagai referensi validasi input

def get_user_choice():
    # Fungsi untuk mengambil dan memvalidasi input pengguna
    # Program akan terus meminta input sampai pengguna
    # memasukkan pilihan yang valid

    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        # Mengambil input dari pengguna dan mengubahnya menjadi huruf kecil
        # untuk menghindari perbedaan antara huruf besar dan kecil

        if user_choice in choices:
            # Mengecek apakah input termasuk pilihan yang valid
            return user_choice
            # Mengembalikan pilihan pengguna jika valid
        else:
            print('Invalid choice!')
            # Menampilkan pesan kesalahan jika input tidak valid

def display_choices(user_choice, computer_choice):
    # Fungsi untuk menampilkan pilihan pengguna dan komputer

    print(f'You chose {emojis[user_choice]}')
    # Menampilkan emoji sesuai pilihan pengguna

    print(f'Computer chose {emojis[computer_choice]}')
    # Menampilkan emoji sesuai pilihan komputer

def determine_winner(user_choice, computer_choice):
    # Fungsi untuk menentukan hasil permainan
    # berdasarkan aturan Rock, Paper, Scissors

    if user_choice == computer_choice:
        # Kondisi jika pilihan pengguna dan komputer sama
        print('Tie!')
        # Hasil permainan seri

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        # Kondisi di mana pengguna menang:
        # Rock mengalahkan Scissors
        # Scissors mengalahkan Paper
        # Paper mengalahkan Rock
        print('You win')

    else:
        # Kondisi di mana komputer menang
        print('You lose')

def play_game():
    # Fungsi utama yang mengatur alur permainan

    while True:
        # Loop utama agar permainan dapat dimainkan berulang kali

        user_choice = get_user_choice()
        # Memanggil fungsi untuk mendapatkan input pengguna yang valid

        computer_choice = random.choice(choices)
        # Komputer memilih salah satu pilihan secara acak

        display_choices(user_choice, computer_choice)
        # Menampilkan pilihan pengguna dan komputer

        determine_winner(user_choice, computer_choice)
        # Menentukan dan menampilkan hasil permainan

        should_continue = input('Continue? (y/n): ').lower()
        # Menanyakan apakah pengguna ingin melanjutkan permainan

        if should_continue == 'n':
            # Jika pengguna memilih untuk berhenti
            break
            # Menghentikan perulangan dan mengakhiri program

# Memanggil fungsi utama sebagai titik awal eksekusi program
play_game()
