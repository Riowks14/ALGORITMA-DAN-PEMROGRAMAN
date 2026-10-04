Mobil = ["BMW", "MERCEDES", "PORSCHE", "TOYOTA", "HONDA"]

masukan = input("cari mobil: ").upper()

if masukan in Mobil:
    print("mobil tersedia")
else:
    print("mobil tidak tersedia")