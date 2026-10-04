#program pemesanan makanan 
#konsep: input, variable, operasi, boolean 

nama_makanan = input("masukan nama makanan: ") #string
harga_makanan = int(input("masukan harga makanan: ")) #integer
jumlah_pesanan = int(input("masukan jumlah pesanan: ")) #integer

#menghitung subtotal
subtotal = harga_makanan * jumlah_pesanan 

#menghitung diskon 10%
diskon = subtotal * 0.10

#menghitung total pembayaranan
total_pembayaran = subtotal - diskon

#menetukan apakah pesanan termasuk pesanan besar
pesanan_besar = total_pembayaran >= 100000

#menampilkan hasil
print("detail pesanan")
print("Nama Makanan:", nama_makanan)
print("Harga Makanan: Rp", harga_makanan)
print("Jumlah Pesanan:", jumlah_pesanan)
print("Subtotal: Rp", subtotal)
print("Diskon 10%: Rp", diskon)
print("Total Pembayaran: Rp", total_pembayaran)
print("Apakah Pesanan Besar?", pesanan_besar)