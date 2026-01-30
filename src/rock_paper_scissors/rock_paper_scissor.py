import random
# Mengimpor modul random
# Digunakan untuk membuat pilihan komputer secara acak agar permainan tidak selalu sama

# Konstanta untuk pilihan permainan
ROCK = 'r'      
# ROCK merepresentasikan pilihan "Rock" dengan input huruf 'r'

SCISSORS = 's'  
# SCISSORS merepresentasikan pilihan "Scissors" dengan input huruf 's'

PAPER = 'p'     
# PAPER merepresentasikan pilihan "Paper" dengan input huruf 'p'

# Dictionary untuk memetakan pilihan ke emoji
emojis = {
    ROCK: '🪨',        # Jika memilih rock, tampilkan emoji batu
    SCISSORS: '✂️',    # Jika memilih scissors, tampilkan emoji gunting
    PAPER: '📃'        # Jika memilih paper, tampilkan emoji kertas
}
# Dictionary digunakan agar tampilan lebih menarik dan kode lebih rapi

# Tuple berisi semua pilihan yang valid
choices = tuple(emojis.keys())
# Tuple digunakan karena bersifat read-only (tidak bisa diubah)
# Berguna untuk validasi input dan pilihan acak komputer

def get_user_choice():
    # Fungsi untuk meminta dan memvalidasi input pengguna
    # Fungsi ini memastikan pengguna hanya bisa memasukkan pilihan yang benar

    while True:
        # Loop akan terus berjalan sampai pengguna memasukkan input yang valid

        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        # Meminta input dari pengguna
        # .lower() memastikan huruf besar dan kecil diperlakukan sama

        if user_choice in choices:
            # Mengecek apakah input pengguna termasuk pilihan yang valid
            return user_choice
            # Jika valid, kembalikan pilihan pengguna dan keluar dari fungsi
        else:
            print('Invalid choice!')
            # Jika input tidak valid, tampilkan pesan error dan ulangi input

def display_choices(user_choice, computer_choice):
    # Fungsi untuk menampilkan pilihan pengguna dan komputer dalam bentuk emoji

    print(f'You chose {emojis[user_choice]}')
    # Menampilkan emoji sesuai pilihan pengguna

    print(f'Computer chose {emojis[computer_choice]}')
    # Menampilkan emoji sesuai pilihan komputer

def determine_winner(user_choice, computer_choice):
    # Fungsi untuk menentukan hasil permainan (menang, kalah, atau seri)

    if user_choice == computer_choice:
        # Jika pilihan pengguna dan komputer sama
        print('Tie!')
        # Permainan berakhir seri

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
        # Jika tidak memenuhi kondisi menang dan bukan seri
        print('You lose')
        # Berarti komputer menang

def play_game():
    # Fungsi utama yang mengatur jalannya permainan

    while True:
        # Loop utama agar permainan bisa dimainkan berulang kali

        user_choice = get_user_choice()
        # Memanggil fungsi untuk mendapatkan input pengguna yang valid

        computer_choice = random.choice(choices)
        # Komputer memilih salah satu pilihan secara acak dari tuple choices

        display_choices(user_choice, computer_choice)
        # Menampilkan pilihan pengguna dan komputer

        determine_winner(user_choice, computer_choice)
        # Menentukan dan menampilkan hasil permainan

        should_continue = input('Continue? (y/n): ').lower()
        # Menanyakan apakah pengguna ingin melanjutkan permainan

        if should_continue == 'n':
            # Jika pengguna memilih tidak melanjutkan
            break
            # Menghentikan loop dan mengakhiri permainan

play_game()
# Memanggil fungsi play_game()
# Baris ini merupakan titik awal eksekusi program
