ytta = int(input("Masukan berapa angka yang mau dirubah : "))
while True:
    if ytta <= 0:
        print("Jumlah angka harus lebih dari 0")
    else:
        for i in range (ytta):
            angka = int(input(f"Masukan angka ke-{i+1} yang mau dirubah : ")) 
            hasil = ""
            while angka > 0:
                sisa = angka % 8
                hasil = str(sisa) + hasil
                angka //= 8
            print(f"angka yang sudah di konfersi ke basis 8 : {hasil}")

    print("Terima kasih telah menggunakan Bunker Hacker!")
    break