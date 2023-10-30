# Nama Toko
print("======================================")
print('      Selamat Datang Dipizza Hut      ')
print("======================================")

# Daftar Menu dan harga
print("""==============Pizza Menu==============
-------------------------------------
|No|     Nama Makanan    |Harga      |
-------------------------------------
|1 |Frankfurter BBQ      |Rp 45.000  |
|2 |Meat Monsta          |Rp 46.000  |
|3 |Super Supreme        |Rp 47.000  |
|4 |Super Supreme Chicken|Rp 48.000  |
      """)
# Input
pesan_pizza = input("Pilih jenis pizza : ").lower()

# Harga pizza
if pesan_pizza == "frankfurter bbq":
    harga_pizza = 45000
elif pesan_pizza == "meat monsta":
    harga_pizza = 46000
elif pesan_pizza == "super supreme":
    harga_pizza = 47000
elif pesan_pizza == "super supreme chicken":
    harga_pizza = 48000
else:
    print("Jenis pizza tidak valid.")
    exit()
#Daftar Menu Crust
print("""=============Crust Pizza=============
-------------------------------------------
|No|        Nama Makanan       |Harga     |
-------------------------------------------
|1 |Original                   |Rp Free   |
|2 |Pan                        |Rp 2.000  |
|3 |Cheesy Bite Crust          |Rp 3.000  |
|4 |Chilli Cheesy Stuffed Crust|Rp 4.000  |
|5 |Stuffed Crust              |Rp 8.000 |
      """)
#Input Crust Pizza
crust_pizza = input("Tambahkan topping : ").lower()

# Biaya topping
if crust_pizza == "original":
    harga_crust = 0
elif crust_pizza == "pan":
    harga_crust = 2000
elif crust_pizza == "cheesy bite crust":
    harga_crust = 3000
elif crust_pizza == "chilli cheesy stuffed crust":
    harga_crust = 4000
elif crust_pizza == "stuffed crust":
    harga_crust = 8000
else:
    print("Jenis Crust tidak valid.")
    exit()
#Membedakan Ukuran Dan Menu Ukuran Pizza
if pesan_pizza == "frankfurter bbq":
     print("""==============Ukuran Pizza==============
     --------------------------------
     |No| Ukuran Makanan |Harga     |
     --------------------------------
     |1 |Small           |Rp 5.000  |
     |2 |Medium          |Rp 6.000  |
      """)
     ukuran_pizza = input("Pilih ukuran pizza : ").lower()
     if ukuran_pizza not in ["small", "medium"]:
        print("Ukuran pizza tidak valid.")
        exit()
elif pesan_pizza == "meat monsta":
    print("""==============Ukuran Pizza==============
     --------------------------------
     |No| Ukuran Makanan |Harga     |
     --------------------------------
     |1 |Small           |Rp 5.000  |
     |2 |Large           |Rp 6.000 |
      """)
    ukuran_pizza = input("Pilih ukuran pizza : ").lower()
    if ukuran_pizza not in ["small", "large"]:
        print("Ukuran pizza tidak valid.")
        exit()
elif pesan_pizza == "super supreme chicken":
    print("""==============Ukuran Pizza==============
     --------------------------------
     |No| Ukuran Makanan |Harga     |
     --------------------------------
     |1 |Medium          |Rp 5.000  |
     |2 |Large           |Rp 6.000 |
      """)
    ukuran_pizza = input("Pilih ukuran pizza : ").lower()
    if ukuran_pizza not in ["medium", "large"]:
        print("Ukuran pizza tidak valid.")
        exit()
else:
    print("""==============Ukuran Pizza==============
     --------------------------------
     |No| Ukuran Makanan |Harga     |
     --------------------------------
     |1 |Small           |Rp 5.000  |
     |2 |Medium          |Rp 6.000  |
     |3 |Large           |Rp 8.000 |
      """)
    ukuran_pizza = input("Pilih ukuran pizza : ").lower()


# Biaya ukuran
if ukuran_pizza == "small":
    ukuran_price = 5000
elif ukuran_pizza == "medium":
    ukuran_price = 6000
elif ukuran_pizza == "large":
    ukuran_price = 8000
else:
    print("Ukuran pizza tidak valid.")
    exit()

nambah_keju = (input("Tambah 13000 untuk Extra Keju (ya/tidak): ")).lower() == "y"

# Biaya tambahan keju
harga_keju = 12000 if nambah_keju else 0

# Total biaya
total_cost = harga_pizza + harga_crust + ukuran_price + harga_keju

# Menampilkan pesanan dan total biaya
print("Thank you for choosing Pizza Hut Delivery!")
print("Your final bill will be: Rp", total_cost)