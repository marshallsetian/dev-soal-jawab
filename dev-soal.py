
import os,sys,time,os,json,requests,datetime
import random
import colorama
from colorama import Fore,Back,init
from urllib import request
from requests import get,post


import locale

localtime=time.asctime(time.localtime(time.time()))
ip=requests.get('https://api.ipify.org').text

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

hijau="\033[0;92m "
putih="\033[0;97m"
abu="\033[0;90m"
kuning="\033[0;93m"
ungu="\033[0;95m"
merah="\033[0;91m"
biru="\033[0;96m"


def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def banner():
    print(f"""\n{putih}[{B}•{putih}] {biru}Developer{hijau}: MarshallSetian
{putih}[{B}•{putih}] {ungu}Instagram {putih}: @marshall_setian
{W}[{B}•{W}] Ip Kamu {putih}  :{Y} {ip}
{W}[{B}•{W}] Waktu/Jam {putih}:{merah} {localtime}
{putih}=======================================
{G}PROGRAM QUIZ SOAL-JAWAB TINGKAT LANJUT
{W}=======================================
Bahasa Program : Python
Fitur: Pilihan ganda, Perhitungan skor, Batas waktu 60 detik
============================================================""")


# Pertanyaan kuis
questions = [
    
    
    
     {
        "question": "Hewan yang disebut sebagai 'insinyur ekosistem' karena kemampuannya mengubah habitat adalah?",
        "choices": ["Berang-berang", "Gajah", "Serigala", "Babi Hutan"],
        "answer": "Berang-berang"
    },
    
     {
        "question": "Apa nama hewan darat yang dapat bertahan hidup tanpa air lebih dari 10 hari?",
        "choices": ["Unta", "Gajah", "Kanguru", "Kuda"],
        "answer": "Unta"
    },
    
    {
        "question": "Hewan tercepat di darat adalah?",
        "choices": ["Singa", "Cheetah", "Kuda", "Serigala"],
        "answer": "Cheetah"
    },
    
    {
        "question": "Taman Sari, yang juga dikenal sebagai Water Castle, dahulu digunakan sebagai apa oleh Sultan Yogyakarta?",
        "choices": ["Tempat tinggal", "Taman hiburan keluarga kerajaan", "Markas militer", "Tempat pertemuan para pejabat"],
        "answer": "Taman hiburan keluarga kerajaan"
    },
    
    {
        "question": "Apa nama alat musik tradisional yang berasal dari Yogyakarta dan biasa digunakan dalam pertunjukan gamelan?",
        "choices": ["Angklung", "Gamelan", "Kolintang", "Sasando"],
        "answer": "Gamelan"
    },
    
     {
        "question": "Apa nama makanan khas Yogyakarta yang terbuat dari ketan dan kelapa parut?",
        "choices": ["Gudeg", "Bakpia", "Klepon", "Krecek"],
        "answer": "Klepon"
    },
    
    {
        "question": "Apa bentuk energi yang dihasilkan oleh suatu benda yang sedang bergerak?",
        "choices": ["Energi potensial", "Energi kinetik", "Energi panas", "Energi listrik"],
        "answer": "Energi kinetik"
    },
    
    {
        "question": "Apa nama alat yang digunakan untuk mengukur arus listrik?",
        "choices": ["Voltmeter", "Amperemeter", "Ohmmeter", "Galvanometer"],
        "answer": "Amperemeter"
    },
    
     {
        "question": "Apa arti peribahasa 'Bagai air di daun talas'?",
        "choices": [
            "Perasaan yang tidak tetap",
            "Orang yang tidak berpendirian",
            "Kebahagiaan yang datang sebentar",
            "Kekayaan yang mudah hilang"
        ],
        "answer": "Perasaan yang tidak tetap"
    },
    
    
     {
        "question": "Apa arti dari peribahasa 'Sepandai-pandai tupai melompat, akhirnya jatuh juga'?",
        "choices": [
            "Orang yang pintar akan selalu berhasil",
            "Orang yang berhati-hati akan terhindar dari masalah",
            "Orang yang sangat pandai pun bisa melakukan kesalahan",
            "Orang yang ceroboh pasti gagal"
        ],
        "answer": "Orang yang sangat pandai pun bisa melakukan kesalahan"
    },
    
    {
        "question": "Apa arti peribahasa 'Air beriak tanda tak dalam'?",
        "choices": [
            "Orang yang banyak bicara biasanya tidak berilmu",
            "Orang yang bijak selalu diam",
            "Orang yang kaya raya",
            "Orang yang tenang pasti pintar"
        ],
        "answer": "Orang yang banyak bicara biasanya tidak berilmu"
    },
    
    {
        "question": "Bunaken terkenal sebagai tempat untuk apa?",
        "choices": ["Gunung Berapi", "Taman Nasional", "Peninggalan Sejarah", "Menyelam"],
        "answer": "Menyelam"
    },
    
    {
        "question": "Sungai terpanjang di Indonesia adalah?",
        "choices": ["Sungai Mahakam", "Sungai Musi", "Sungai Bengawan Solo", "Sungai Kapuas"],
        "answer": "Sungai Kapuas"
    },
    
    
    {
        "question": "Siapa penulis buku 'Laskar Pelangi'?",
        "choices": ["Tere Liye", "Andrea Hirata", "Pramoedya Ananta Toer", "Habiburrahman El Shirazy"],
        "answer": "Andrea Hirata"
    },
    
    
    {
        "question": "Apa nama lagu kebangsaan Indonesia?",
        "choices": ["Indonesia Jaya", "Indonesia Pusaka", "Garuda Pancasila", "Indonesia Raya"],
        "answer": "Indonesia Raya"
    },
    {
        "question": "Pulau terbesar di Indonesia adalah?",
        "choices": ["Jawa", "Sumatra", "Kalimantan", "Sulawesi"],
        "answer": "Kalimantan"
    },
    
    
    {
        "question": "Negara manakah yang memiliki menara Eiffel?",
        "choices": ["Italia", "Jerman", "Spanyol", "Prancis"],
        "answer": "Prancis"
    },
    
    {
        "question": "Unsur kimia dengan simbol 'Fe' dikenal sebagai apa?",
        "choices": ["Emas", "Perak", "Besi", "Tembaga"],
        "answer": "Besi"
    },
    {
        "question": "Hewan apakah yang dikenal sebagai 'Raja Hutan'?",
        "choices": ["Singa", "Harimau", "Serigala", "Gajah"],
        "answer": "Singa"
    },
    {
    "question": "siapakah pencipta Bitcoin?",
    "choices": ["Elon musk", "Tom cruise", "Satoshi nakamoto", "Changpeng Zhao"],
    "answer": "Satoshi nakamoto"
},

    {
        "question": "Apa ibu kota dari Australia?",
        "choices": ["Sydney", "Canberra", "Melbourne", "Perth"],
        "answer": "Canberra"
    },
    {
        "question": "Siapa penulis novel '1984'?",
        "choices": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.K. Rowling"],
        "answer": "George Orwell"
    },
    {
        "question": "Berapa hasil dari 12 x 8?",
        "choices": ["96", "98", "100", "94"],
        "answer": "96"
    },
    {
        "question": "Apa unsur kimia dengan simbol 'O'?",
        "choices": ["Oksigen", "Osmium", "Oganesson", "Oksidasi"],
        "answer": "Oksigen"
    },
    {
        "question": "Siapa pelukis dari lukisan terkenal 'Mona Lisa'?",
        "choices": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    }
]

# Fungsi untuk mengajukan pertanyaan
def ask_question(question):
    print(f"\n{putih}{question['question']}\n")
    for i, choice in enumerate(question['choices']):
        print(f"{i + 1}.{choice}")
        
        # Mengacak urutan pilihan jawaban
    #random.SystemRandom(question['choices'])

    
    
    start_time = time.time()
    answer = input("\nPilih jawaban (masukkan nomor): ")
    elapsed_time = time.time() - start_time

    if elapsed_time > 60:
        autoketik("Waktu habis! Anda tidak mendapatkan poin.")
        
        os.system("clear")
        return banner()
        return False

    if question['choices'][int(answer) - 1].lower() == question['answer'].lower():
        autoketik(f"{G}Jawaban benar!{W}" +"\n"+question['question']+"\n=============>\n"+f"{Y}"""+ question['answer'])
        time.sleep(7)
        os.system("clear")
        return banner()
        return True
    else:
        autoketik(f"{R}Jawaban salah!{W} Jawaban yang benar adalah{Y} {question['answer']}.")
        time.sleep(5)
        os.system("clear")
        return banner()
        return False

# Main program
def run_quiz():
    random.shuffle(questions)
    banner()
    
    score = 0

    
    for question in questions:
        if ask_question(question):
            score += 1
        time.sleep(2)  # Jeda 2 detik sebelum melanjutkan ke pertanyaan berikutnya
    
    print(f"\nKuis selesai! Skor Anda adalah {score} dari {len(questions)}.")
    print("semoga hari anda menyenangkan!")

if __name__ == "__main__":
    run_quiz()

