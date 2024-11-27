data_limbah = {
    'lokasi1': {
        'nama_lokasi': 'Area Kota 1',
        'jumlah_limbah': {
            'plastik': 500,
            'organik': 300,
            'logam': 200
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Area Kota 2',
        'jumlah_limbah': {
            'plastik': 700,
            'organik': 400,
            'logam': 250
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Area Kota 3',
        'jumlah_limbah': {
            'plastik': 600,
            'organik': 350,
            'logam': 300
        }
    }
}


# 1. Print semua data lokasi
print("Semua data lokasi:")
print(data_limbah)
print()

# 2. Print hanya jumlah limbah plastik dari lokasi 2
print("Jumlah limbah plastik dari lokasi 2:")
print(data_limbah['lokasi2']['jumlah_limbah']['plastik'])
print()

# 3. Print nama lokasi 3
print("Nama lokasi 3:")
print(data_limbah['lokasi3']['nama_lokasi'])
print()

# 4. Masukan jumlah limbah organik dan logam setiap lokasi ke dalam variabel yang berbeda
print("Jumlah limbah organik dan logam per lokasi:")

organik_lokasi1 = data_limbah['lokasi1']['jumlah_limbah']['organik']
logam_lokasi1 = data_limbah['lokasi1']['jumlah_limbah']['logam']
print(f"Lokasi 1 - Organik: {organik_lokasi1}, Logam: {logam_lokasi1}")

organik_lokasi2 = data_limbah['lokasi2']['jumlah_limbah']['organik']
logam_lokasi2 = data_limbah['lokasi2']['jumlah_limbah']['logam']
print(f"Lokasi 2 - Organik: {organik_lokasi2}, Logam: {logam_lokasi2}")

organik_lokasi3 = data_limbah['lokasi3']['jumlah_limbah']['organik']
logam_lokasi3 = data_limbah['lokasi3']['jumlah_limbah']['logam']
print(f"Lokasi 3 - Organik: {organik_lokasi3}, Logam: {logam_lokasi3}")

# 5. Buat percabangan untuk menentukan apakah memerlukan penanganan khusus


def cek_penanganan_khusus(nama_lokasi, organik, logam):
    if organik > 400 or logam > 250:
        print(f"{nama_lokasi} memerlukan penanganan khusus.")
    else:
        print(f"{nama_lokasi} dalam kondisi aman.")

# Iterasi menggunakan for i, j
for i, j in data_limbah.items():
    nama_lokasi = j['nama_lokasi']
    organik = j['jumlah_limbah']['organik']
    logam = j['jumlah_limbah']['logam']
    
    # Panggil fungsi cek_penanganan_khusus untuk setiap lokasi
    cek_penanganan_khusus(nama_lokasi, organik, logam)
