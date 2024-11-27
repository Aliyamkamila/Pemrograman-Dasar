# Asupan Air Harian
Usia = int(input("Masukkan usia Anda: "))

if Usia < 2:
    print("Masih diberi ASI")
else:
    while True:
        Gender = input("Masukkan jenis kelamin Anda (L/P): ")
        if Gender in ["L", "P"]:
            break  # Keluar dari loop jika input valid
        else:
            print("Jenis kelamin tidak valid. Silakan masukkan L untuk laki-laki atau P untuk perempuan.")

    if Usia < 18:
        if Gender == "L":
            recommendation = 1.6 
        elif Gender == "P":
            recommendation = 1.4 
        
    elif 18 <= Usia <= 64:
        if Gender == "L":
            recommendation = 2.5
        elif Gender == "P":
            recommendation = 2.0
        
    elif Usia > 64:
        if Gender == "L":
            recommendation = 2.0
        elif Gender == "P":
            recommendation = 1.8
        
    if 'recommendation' in locals():  # Pastikan recommendation sudah didefinisikan
        print(f"Rekomendasi asupan air harian Anda adalah {recommendation} liter.")
