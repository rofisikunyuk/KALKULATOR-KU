print("\n")
print("=" * 41)
print("              KALKULATOR-KU              ")
print("=" * 41)
print(" [>] Opersi")
print(" [a] Pertambahan")
print(" [b] Pengurangan")
print(" [c] Perkalian")
print(" [d] Pembagian")
print("=" * 41)
jenis = str(input(" [+] Jenis Operasi: "))
pertama = int(input(" [+] Bilangan Pertama: "))
kedua = int(input(" [+] Bilangan Kedua: "))
# Pertambahan
if jenis == "a":
    nama = "Pertambahan"
    hasil = pertama + kedua
    print("=" * 41)
    print(" [>] Hasil: ", hasil)
    print("=" * 41, "\n")
# Pengurangan
elif jenis == "b":
    nama = "Pengurangan"
    hasil = pertama - kedua
    print("=" * 41)
    print(" [>] Hasil: ", hasil)
    print("=" * 41, "\n")
# Perkalian
elif jenis == "c":
    nama = "Perkalian"
    hasil = pertama * kedua
    print("=" * 41)
    print(" [>] Hasil: ", hasil)
    print("=" * 41, "\n")
# Pembagian
elif jenis == "d":
    nama = "Pembagian"
    hasil = pertama / kedua
    print("=" * 41)
    print(" [>] Hasil: ", hasil)
    print("=" * 41, "\n")
else:
    print("=" * 41)
    print(" [!] Sihkan Pilih Opersai Yang Tersedia")
    print("=" * 41, "\n")
# Selesai
