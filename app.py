def tambah (a, b):
    return a + b
def kurang (a, b):
    return a - b
def kali (a, b):
    return a * b
def bagi (a, b):
    return a / b

print('Belajar Membuat Kalkulator')
print('Opsi')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')

milih = input('Mau milih apa (1/2/3/4): ')

angka1 = float(input('angka pertama masukkan : '))
angka2 = float(input('angka dua masukkan : '))

if milih == '1':
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
elif milih == '2':
    print(angka1, "-", angka2, "=", kurang(angka1, angka2))
elif milih == '3':
    print(angka1, "*", angka2, "=", kali(angka1, angka2))
elif milih == '4':
    if angka2 != 0:
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
    else:
        print("Pembagian dengan nol tidak valid.")
else:
    print("Pilihan tidak valid.")