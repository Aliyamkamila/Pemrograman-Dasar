Nama = input ("Masukkan nama anda: ")
Suhu_tubuh = float (input("Masukkan suhu tubuh anda: "))
Detak_jantung = int(("Masukkan detak jantung per menit anda: "))

print(f"\nNama: {Nama}")
print(f"Suhu tubuh: {Suhu_tubuh} derajat")
print(f"Detak jantung: {Detak_jantung}")

kondisi_suhu = " "
kondisi_detak_jantung = " "

if Suhu_tubuh > 3.5:
    kondisi_akhir = ("Suhu tubuh di atas normal")

    if 39 < Suhu_tubuh < 50:
        kondisi_akhir = "Suhu tubuh anda tinggi, Butuh perhatian medis segera dan harus segera dirawat!"
        kondisi_akhir ="Cukup istirahat saja"

if Detak_jantung > 100:
    kondisi_detak_jantung = "Detak jantung anda terlalu tinggi, butuh pemeriksaan lebih lanjut"
else: 
    kondisi_detak_jantung = "Deak jantung anda normal, tetap jaga kesehatan"

print(f"Hasil kondisi akhir anda yang harus diambil adalah:\n{kondisi_akhir} dan {kondisi_detak_jantung}")