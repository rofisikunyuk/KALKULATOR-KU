print("\n")
print("-"*40)
print("\tKALKULATOR KU\t")
print("-"*40)
print(" a. Pertambahan")
print(" b. Pengurangan")
print(" c. Perkalian")
print(" d. Pembagian")
print("-"*40)
jenis = str(input(" > Jenis Operasi: "))
pertama = int(input(" > Bilangan Pertama: "))
kedua = int(input(" > Bilangan Kedua: "))
# Pertambahan
if jenis == "a":
    nama = "Pertambahan"
    hasil = pertama + kedua
    print("-" * 40)
    print(" > Hasil: ", hasil)
    print("-" * 40, "\n")
# Pengurangan
elif jenis == "b":
    nama = "Pengurangan"
    hasil = pertama - kedua
    print("-" * 40)
    print(" > Hasil: ", hasil)
    print("-" * 40, "\n")
# Perkalian
elif jenis == "c":
    nama = "Perkalian"
    hasil = pertama * kedua
    print("-" * 40)
    print(" > Hasil: ", hasil)
    print("-" * 40, "\n")
# Pembagian
elif jenis == "d":
    nama = "Pembagian"
    hasil = pertama / kedua
    print("-" * 40)
    print(" > Hasil: ", hasil)
    print("-" * 40, "\n")
else:
    print("-" * 40)
    print(" ! Sihkan Pilih Opersai Yang Tersedia")
    print("-" * 40, "\n")
# Selesai
