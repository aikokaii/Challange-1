import math
nama = input("Masukan nama anda : ")
while True:
    total = int(input("Masukan jumlah tempat wisata yang telah dikunjungi: "))
    if total <= 0:
        print("Jumlah tempat wisata harus tepat")
    else:
        wisata_list = []  
        rating_list = []  

        for i in range(1, total + 1):
            wisata = input(f"Masukan nama tempat wisata ke-{i}: ")
            while True:
                rating = int(input(f"Masukan rating tempat wisata ke-{i} (1-10): "))
                if rating < 1 or rating > 10:
                    print("Rating tidak valid")
                else:
                    break

            wisata_list.append(wisata)
            rating_list.append(rating)

        max_rating = max(rating_list)
        index_max = rating_list.index(max_rating)
        print(f"\nTempat wisata paling berkesan bagi {nama} adalah {wisata_list[index_max]}!")

        average_rating = sum(rating_list) / total
        average_rating = round(average_rating, 2)
        print(f"Rata-rata rating dari semua tempat wisata adalah: {average_rating}")
        if 8 <= average_rating <= 10:
            print(f"{nama} merasa sangat senang dan puas karena pengalamnya sangat menyenangkan :D")
        elif 5 <= average_rating < 8:
            print(f"{nama} merasa senang dengan pengalaman yang didapatkan :)")
        else:
            print(f"Huhu, {nama} sedih karena pengalaman kurang memuaskan :(")
        break
    print ("\n Terima kasih telah menggunakan Holiday Tracker!")
    break
