#Conditional Statements

#penggunaan random
import random

nilai = random.randint(10, 50)
print("Nilai:", nilai)

if nilai >= 30:
    print("Lulus")
else:
    print("Mengulang")

#penggunaan date
from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang adalah:", sekarang)

#penggunaan if,elif,else
nilai = 60
if nilai >= 95:
    print("Nilai A")
elif nilai >= 90:
    print("Nilai B+")
elif nilai >= 85:
    print("Nialai B")
elif nilai >= 80:
    print("Nialai B-")
elif nilai >= 75:
    print("Nialai C")
elif nilai >= 70:
    print("Nialai C-")
else:
    print("Anda Mengulang Semester Ini")

#contoh penggunaan if-elif-else statment
def user_check(role):
    if role == 1:
        print("Admin")
    elif role == 2:
        print("Moderator")
    elif role == 3:
        print("Member VIP")
    elif role == 4:
        print("Member Biasa")
    elif role == 5:
        print("Member Baru")
    else:
        print("Orang Asing")
user_check(1)
user_check(2)
user_check(3)
user_check(4)
user_check(5)

#Penggunaan if else menggunakan Input
password = input('Masukkan Kata Sandi: ')
if password == "diandrakeren":
    print("Password Benar!")
elif password == "diandrakalcer":
    print("Selamat Datang")
elif password == "diandraadmin":
    print("Selamat Datang Admin")
else:
    print("Kata Sandi Salah!")

#Penggunaan nested if
x = int(input("Masukkan nilai x: "))
if x > 0:
    print("x adalah bilangan positif")
    if x % 2 == 0:
        print("x juga bilangan genap")
    else:
        print("x adalah bilangan ganjil")
elif x == 0:
    print("x adalah nol")
else:
    print("x adalah bilangan negatif")

#Penggunaan nested if kasus lain
umur = int(input("Untuk caleg, silahkan masukkan umur: "))
punya_ktp = True

if umur >= 17:
    if punya_ktp:
        print("Boleh memilih")
    else:
        print("Harus punya KTP dulu")
else:
    print("Belum cukup umur")

#Penggunaan operator logika dalam if
y = int(input("Masukkan nilai Y: "))
if y > 0 and y % 2 == 0:
    print("Y adalah bilangan positif dan genap")
elif y > 0 and y % 2 != 0:
    print("Y adalah bilangan positif dan ganjil")
else:
    print("Y bukan bilangan positif")

#Penggunaan Ternary Operator
z = int(input("Masukkan nilai Z: "))
status = "Positif" if z > 0 else "Negatif atau Nol"
print(f"Z adalah bilangan {status}")

#variable yang dapat digunakan dalam if, elif
is_active = True
if is_active:
    print("Selamat akun aktif")

#Iterative Statements

#Perbedaan for dan while
# Kasus for (jumlah sudah pasti 5 kali)
for i in range(7):
    print("(For)Perulangan ke-", i)

# Kasus while
i = 0
while i < 9:
    print("(While)Perulangan ke-", i)
    i += 1

#Break
for i in range(35):
    if i == 25:
        break
    print(i)

#Continue
for i in range(15):
    if i == 10:
        continue
    print(i)

#Else di loop
for i in range(7):
    print(i)
else:
    print("Loop selesai, tidak ada break")

#Nested di loop
for i in range(5):
    for j in range(5):
        print(i, j)

#Aplikasi literasi dalam algoritma
#Membuat pola bintang
for i in range(10):
    for j in range(i+1):
        print("*", end="")
    print()

#Pembuatan Piramid
tinggi = int(input("Masukkan tinggi piramida yang anda inginkan: "))

for i in range(tinggi):
    print(" " * (tinggi - i - 1) + "* " * (i + 1))

#Menghitung Jumlah Total
angka = [14, 29, 31, 65]
total = 0
for nilai in angka:
    total += nilai

print("(Penghitungan Jumlah Total) Total:", total)

#Faktorial
n = int(input("Masukkan nilai yang ingin di faktorkan: "))
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)

#Validasi input dengan while
nilai = -1
while nilai < 0:
    nilai = int(input("Masukkan angka positif: "))

print("Input diterima")

#Transfer Statment
nilai = int(input("Masukkan Nilai Rapor: "))
if nilai > 75:
    pass
else:
    print("Anda Mengulang")

#Return Statment
hasil = 0

def hitung(a, b):
    global hasil
    hasil = a + b

hitung(27, 9)
print(hasil)