nilai = int(input("Masukkan nilai: "))

if nilai > 100:
    print("nilai tidak valid atau error")
elif nilai == 100:
    print("nilai anda A (lulus)")    
elif nilai >= 90:
    print("nilai anda B (lulus)")
elif nilai >= 80:
    print("nilai anda C (lulus)")
elif nilai >= 70:
    print("nilai anda D (mengulang)")
elif nilai < 60: 
    print("nilai anda E (mengulang)")