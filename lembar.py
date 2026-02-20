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

#Penggunaan operator logika dalam if
x = int(input("Masukkan nilai x: "))
if x > 0 and x % 2 == 0:
    print("x adalah bilangan positif dan genap")
elif x > 0 and x % 2 != 0:
    print("x adalah bilangan positif dan ganjil")
else:
    print("x bukan bilangan positif")

#Penggunaan Ternary Operator
x = int(input("Masukkan nilai x: "))
status = "Positif" if x > 0 else "Negatif atau Nol"
print(f"x adalah bilangan {status}")

#variable yang dapat digunakan dalam if, elif
is_active = True
if is_active:
    print("Selamat akun aktif")