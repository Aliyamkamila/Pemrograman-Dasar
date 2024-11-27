for i in range(3):
    Nama = input("Masukkan nama anda: ")
    Angka = int(input("Masukkan Angka 1-4: "))

    match Angka:
        case 1:
            Suhu_tubuh = float(input("Masukkan suhu tubuh anda: "))
            Detak_jantung = int(input("Masukkan detak jantung per menit anda: "))

            if Suhu_tubuh > 37.5:
                kondisi_akhir = "Suhu tubuh di atas normal"
                if 39 < Suhu_tubuh < 50:
                    kondisi_akhir = "Suhu tubuh anda tinggi, butuh perhatian medis segera dan harus segera dirawat!"
                else:
                    kondisi_akhir = "Suhu tubuh cukup tinggi, sebaiknya istirahat"
                    if Detak_jantung > 100:
                        kondisi_detak_jantung = "Detak jantung anda terlalu tinggi, butuh pemeriksaan lebih lanjut"
                    else:
                        kondisi_detak_jantung = "Detak jantung anda normal, tetap jaga kesehatan"
            else :
                kondisi_akhir = "Suhu tubuh normal"
                kondisi_detak_jantung = "Jantung Anda sehat"


            print(f"\nNama: {Nama}")
            print(f"Suhu tubuh: {Suhu_tubuh} derajat")
            print(f"Detak jantung: {Detak_jantung}")
            print(f"Hasil kondisi akhir anda yang harus diambil adalah:\n{kondisi_akhir} dan {kondisi_detak_jantung}")

        case 2:
            Sistolik = int(input("Masukkan tekanan darah sistolik (mmHg): "))
            Diastolik = int(input("Masukkan tekanan darah diastolik (mmHg): "))
            Denyut_nadi = int(input("Masukkan denyut nadi (bpm): "))

            if Sistolik > 180 or Diastolik > 120:
                kondisi_tekanan_darah = "Krisis hipertensi! Segera cari bantuan medis."
            elif Sistolik > 140 or Diastolik > 90:
                kondisi_tekanan_darah = "Anda memiliki hipertensi. Disarankan konsultasi dengan dokter."
            elif 120 <= Sistolik <= 139 or 80 <= Diastolik <= 89:
                kondisi_tekanan_darah = "Anda berada dalam kategori prehipertensi."
            elif Sistolik < 120 and Diastolik < 80:
                kondisi_tekanan_darah = "Tekanan darah Anda normal."
                if Denyut_nadi > 100:
                    kondisi_denyut_nadi = "Detak jantung anda terlalu tinggi, butuh pemeriksaan lebih lanjut."
                elif Denyut_nadi < 60:
                    kondisi_denyut_nadi = "Detak jantung anda rendah. Periksa apakah ada gejala lain."
                else:
                    kondisi_denyut_nadi = "Detak jantung anda normal, tetap jaga kesehatan."
                
            print(f"\nNama: {Nama}")
            print(f"Tekanan darah sistolik: {Sistolik} mmHg")
            print(f"Tekanan darah diastolik: {Diastolik} mmHg")
            print(f"Denyut nadi: {Denyut_nadi} BPM")
            print(f"Hasil kondisi akhir anda yang harus diambil adalah:\n{kondisi_denyut_nadi} dan \n{kondisi_tekanan_darah}")

        case 3:
            print("Tidak ada")

        case 4:
            print("Kosong.")

        case _:
            print("Masukkan angka yang valid (1-4).")
