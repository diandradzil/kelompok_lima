# KELOMPOK 5

# ANGGOTA KELOMPOK
# Diandra Dzil Sayyid Az-Zulwa Syam (Coding, Penjelasan Line Code) (250907501025)
# Andi Alfatia Salsabila (Pengertian Syntx Dan Beberapa Fungsi Fungsi) (250907502020)

# Virtual Environment atau ENV adalah lingkungan Python terpisah untuk setiap proyek. Tujuannya agar library antar proyek tidak saling konflik.

# Tutorial Set Up Env
# 1. python -m venv envkelompok <-- (nama env kalian bebas)
# 2. envkelompok\Scripts\activate (untuk mengaktifkan env)
# 3. Jika berhasil maka muncul "(envkelompok)" pada terminal

# Library adalah kumpulan kode siap pakai yang membantu kita menyelesaikan tugas tertentu tanpa harus menulis semuanya dari awal. Berikut beberapa contoh penerapan library yang umum digunakan.

# Tutorial menggunakan PIP:
# pip install requests <-- (Nama Liblary yang di inginkan)

# Penerapan LIB
# import requests <-- (Memanggil LIB yang sudah di ambil melalui PIP)

# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.text)

# Conditional Statements adalah struktur kendali (control flow) dalam pemrograman yang digunakan untuk mengambil keputusan berdasarkan kondisi tertentu. Program akan mengeksekusi blok kode tertentu jika kondisi bernilai True, dan melewati atau menjalankan blok lain jika kondisi bernilai False.

# Contoh (Menggunakan Random):

# nilai = random.randint(10, 50)
# print("Nilai:", nilai)

# if nilai >= 30:
#    print("Lulus")
# else:
#    print("Mengulang")

# Program akan memilih nomor acak mulai dari 10 ingga 50, jika nilai lebih dari 30 maka program akan print "Lulus", dan jika kurang dari 30 maka program print "Mengulang"

# Contoh jika ada IF, ELIF, ELSE
# nilai = 60
# if nilai >= 95:
#    print("Nilai A")
# elif nilai >= 90:
#    print("Nilai B+")
# elif nilai >= 85:
#    print("Nialai B")
# elif nilai >= 80:
#    print("Nialai B-")
# elif nilai >= 75:
#    print("Nialai C")
# elif nilai >= 70:
#    print("Nialai C-")
# else:
#    print("Anda Mengulang Semester Ini")

# jadi jika nilai dari 95 maka nilai adalah A, nilai lebih dari 90 B+, nilai lebih dari 85 B, nilai lebih dari 80 B-, nilai lebih dari 75 C, nilai lebih dari 70 C-, dan jika nilai kurang dari 70 maka output keluar adalah "Anda Mengulang Semester Ini"

# Penerapan IF ELIF ELSE STATMENT:
# def user_check(role):
#    if role == 1:
#        print("Admin")
#    elif role == 2:
#        print("Moderator")
#    elif role == 3:
#        print("Member VIP")
#    elif role == 4:
#        print("Member Biasa")
#    elif role == 5:
#        print("Member Baru")
#    else:
#        print("Orang Asing")
# user_check(1)
# user_check(2)
# user_check(3)
# user_check(4)
# user_check(5)

# Jadi setiap baris if dan elif memiliki variable "Role" menjadi penanda, seperti code di atas jika "Role" 1 adalah "Admin" "Role" 2 Adalah "Moderator" dan seterusnya, kecuali "else" yaitu tidak terdapat dari bagian "Role" tersebut maka di labelkan sebagai "Orang Asing

# Penerapan nasted IF:
# umur = int(input("Untuk caleg, silahkan masukkan umur: "))
# punya_ktp = True

# if umur >= 17:
#    if punya_ktp:
#        print("Boleh memilih")
#    else:
#        print("Harus punya KTP dulu")
# else:
#    print("Belum cukup umur")

# Nasted code adalah code yang bersarang, seperti code yang di atas, dimana jika input umur kurang dari 17 maka langsung ke else atau "Belum cukup umur", tapi kalau umur yang di input lebih dari 17 maka bisa caleg, namu disini harus ada syarat lagi yaitu apakah sudah ada ktp atau belum? "punya_ktp = True", jika "punya_ktp = False" maka outputnya adalah "Harus punya KTP dulu" walaupun input umur lebih dari 17

# Iterative Statement adalah perintah dalam Python yang digunakan untuk mengulang suatu blok kode berkali-kali selama kondisi tertentu terpenuhi.

# Contoh Break:

# for i in range(35):
#    if i == 25:
#        break
#    print(i)

# output nya adalah 0 hingga 24, berhenti pada 25 karena ada "break" dan tidak dilanjutkan

# Contoh Continue

# for i in range(15):
#    if i == 10:
#        continue
#    print(i)

# output nya adalah 0 hingga 14 (karena penghitungan python di mulai dari angka 0, 0 - 14 adalah 15 range) namun angka 10 tidak ada atau di skip