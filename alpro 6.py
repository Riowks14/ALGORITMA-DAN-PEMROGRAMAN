def luaspersegi(sisi):
    return sisi * sisi
def kelilinglingkaran(jari_jari):
    return 2 * 3.14 * jari_jari 
def luaspersegi_panjang(panjang, lebar):
    return panjang * lebar

def main():
    while True:
        print("Pilih operasi:")
        print("1. LuasPersegi")
        print("2. KelilingLingkaran")
        print("3. LuasPersegiPanjang")
        print("4. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi persegi: "))
        hasil = luaspersegi(sisi)
        print(f"Luas persegi: {hasil}")
    elif pilihan == '2':
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        hasil = kelilinglingkaran(jari_jari)
        print(f"Keliling lingkaran: {hasil}")
    elif pilihan == '3':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        hasil = luaspersegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang: {hasil}")
    elif pilihan == '4':
        print("Keluar dari program.")

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
