print("\n")
print("=" * 41)
print("              KALKULATOR-KU              ")
print("=" * 41)
print(" [>] Opersi")
print(" [+] Pertambahan")
print(" [-] Pengurangan")
print(" [*] Perkalian")
print(" [/] Pembagian")
print("=" * 41)
pertama = int(input(" [+] Bilangan Pertama : "))
jenis = str(input(" [+] Jenis Operasi: "))
kedua = int(input(" [+] Bilangan Kedua: "))
# Pertambahan
if jenis == "+":
    nama = "Pertambahan"
    hasil = pertama + kedua
    print("=" * 41)
    print(" [=] Hasil: ", hasil)
    print("=" * 41, "\n")
# Pengurangan
elif jenis == "-":
    nama = "Pengurangan"
    hasil = pertama - kedua
    print("=" * 41)
    print(" [=] Hasil: ", hasil)
    print("=" * 41, "\n")
# Perkalian
elif jenis == "*":
    nama = "Perkalian"
    hasil = pertama * kedua
    print("=" * 41)
    print(" [=] Hasil: ", hasil)
    print("=" * 41, "\n")
# Pembagian
elif jenis == "/":
    nama = "Pembagian"
    hasil = pertama / kedua
    print("=" * 41)
    print(" [=] Hasil: ", hasil)
    print("=" * 41, "\n")
else:
    print("=" * 41)
    print(" [!] Sihkan Pilih Opersai Yang Tersedia")
    print("=" * 41, "\n")
# Selesai
