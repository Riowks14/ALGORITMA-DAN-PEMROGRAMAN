kecepatan = float(input("Masukkan kecepatan (m/s): "))

if kecepatan >= 80:
    gas = 0.0
    rem = 1.0
    print("gas:", gas)
    print("rem:", rem)
    print("kecepatan terlalu tinggi, rem diaktifkan")

elif kecepatan <= 20:
    gas = 1.0
    rem = 0.0
    print("gas:", gas)
    print("rem:", rem)
    print("kecepatan terlalu rendah, gas diaktifkan")

elif kecepatan > 20 and kecepatan < 80:
    gas = 0.0
    rem = 0.0
    print("gas:", gas)
    print("rem:", rem)
    print("kecepatan normal")