kopi_yang_tersedia = [
    "latte",
    "americano",
    "butterscotch",
    "capucino",
    "kopi susu",
    "kopi gula aren"
]

pesanan_kopi = []
total_harga = 0
harga_per_kopi = 10

print("=== PROGRAM PEMESANAN KOPI ===")

while True:
    jawaban = input("Apakah ingin memesan kopi? (yes/no): ").strip().lower()

    if jawaban == "yes":
        print("\nKopi yang tersedia:")
        for i, kopi in enumerate(kopi_yang_tersedia, start=1):
            print(f"{i}. {kopi}")

        pilihan = input("Kopi apa yang kamu inginkan? Masukkan nama kopi: ").strip().lower()

        if pilihan in kopi_yang_tersedia:
            pesanan_kopi.append(pilihan)
            total_harga += harga_per_kopi
            print(f"Menambahkan {pilihan} ke pesanan.")
            print(f"Pesanan saat ini: {pesanan_kopi}")
            print(f"Total sementara: {total_harga}")
        else:
            print("Maaf, kopi tersebut tidak tersedia.")

    elif jawaban == "no":
        break

    else:
        print("Masukkan hanya 'yes' atau 'no'.")

print("\n=== RINGKASAN PESANAN ===")

if pesanan_kopi:
    print("Pesanan kamu:")
    for i, kopi in enumerate(pesanan_kopi, start=1):
        print(f"{i}. {kopi}")

    print(f"Total harga: {total_harga}")
    print("Terima kasih! Pesanan kamu sedang diproses.")
else:
    print("Kamu belum memesan kopi.")
    print("Terima kasih sudah menggunakan program ini.")
