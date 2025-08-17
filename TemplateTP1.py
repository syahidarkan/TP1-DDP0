import math

# Tugas Pemrograman 1 DDP-0
# Problem Setters: ARA, AYD, TAW, ICO

# Topik/Materi: Computational Thinking, Variable, Data Type, 
#               I/O, Basic Arithmetic, Math Library, 
#               Conditional Statement, dan Loop Statement

# Informasi perjalanan
jarak_tempuh = 0
koordinat_x_planet = 0
koordinat_y_planet = 0
durasi_perjalanan = 0
planet_saat_ini = "Bumi"
nama_rocket = ""
kecepatan_rocket = 0
menetap = False

# Informasi kriptografi
keyboard = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
len_keyboard = len(keyboard)

print(">>===================================================================<<")
print("||                                                                   ||")
print("||      🚀 SELAMAT DATANG DI DEK DEPE'S OUTER SPACE INTERFACE 🚀    ||")
print("||                                                                   ||")
print(">>===================================================================<<")

# Daftarkan roket
...

# Main program
while not menetap:

    print("=" * 29 + " Menu Utama " + "=" * 30)
    print()

    print("Lokasi saat ini:", planet_saat_ini) 
    print()
    print("Menu Utama:")
    print("1. Berangkat")
    print("2. Kirim Pesan")
    print("3. Baca Pesan")
    print("4. Lihat Laporan Perjalanan")
    print("5. Akhiri Perjalanan (keluar program)")

    print()
    pilihan = input("Masukkan pilihan: ")
    print()

    if pilihan == "1": # Berangkat ke planet tujuan

        print("=" * 30 + " Berangkat " + "=" * 30)
        print()

        while True:

            print("Pilih opsi navigasi:")
            print("1. Koordinat Kartesian (x, y)")
            print("2. Koordinat Polar (sudut, jarak)")
            print("3. Kembali ke Menu Utama")

            print()
            opsi_navigasi = input("Masukkan pilihan: ")
            print()

            if opsi_navigasi == "1": 
                # TODO: Navigasi menggunakan koordinat kartesian

                # TODO: Terima input berupa koordinat dan nama planet

                koordinat_x_planet_kertasian_input = int(input("Berapa Koordinat X: "))
                koordinat_y_planet_kertasian_input = int(input("Berapa Koordinat Y: "))
                planet_saat_ini_kertasian_input = input("Planet Saat Ini: ")
                ...
                    
                # TODO: Hitung jarak tempuh dari koordinat dengan rumus Pythagoras
                jarak_tempuh_kertasian_hasil = math.sqrt(abs(koordinat_x_planet_kertasian_input ** 2 - koordinat_y_planet_kertasian_input ** 2))
                ...

                # TODO: Update koordinat planet saat ini
                koordinat_x_planet = koordinat_x_planet_kertasian_input
                koordinat_y_planet = koordinat_y_planet_kertasian_input

                # TODO: Update planet saat ini
                planet_saat_ini = planet_saat_ini_kertasian_input

                print(jarak_tempuh_kertasian_hasil)
                print("✅ Berhasil mendarat di Planet", ...)
                print(planet_saat_ini_kertasian_input)
                ...
            
            elif opsi_navigasi == "2": 
                # TODO: Navigasi menggunakan koordinat polar

                # TODO: Terima input berupa nama planet, sudut, dan jarak
                sudut_planet_polar_input = int(input("Berapa Sudut: "))
                jarak_planet_polar_input = int(input("Berapa Jarak: "))
                planet_saat_ini_polar_input = input("Planet Saat Ini: ")
                ...

                # TODO: Konversi sudut ke radian
                konversi_sudut_radian = math.radians(sudut_planet_polar_input)
                konversi_jarak_radian = math.radians(jarak_planet_polar_input)
                ...
                
                # TODO: Hitung koordinat kartesian dari sudut dan jarak
                hasil_kertasian_sudut = konversi_jarak_radian * math.cos(konversi_sudut_radian)
                hasil_kertasian_jarak = konversi_jarak_radian * math.sin(konversi_sudut_radian)
                ...

                # TODO: Update jarak tempuh
                jarak_tempuh_polar_hasil = math.sqrt(abs((hasil_kertasian_sudut - sudut_planet_polar_input)**2 + (hasil_kertasian_jarak - jarak_planet_polar_input) ** 2))
                ...

                # TODO: Update koordinat planet saat ini
                koordinat_x_planet = hasil_kertasian_sudut
                koordinat_y_planet = hasil_kertasian_jarak

                # TODO: Update planet saat ini
                planet_saat_ini = planet_saat_ini_polar_input

                print(jarak_tempuh_polar_hasil)
                print("✅ Berhasil mendarat di Planet", planet_saat_ini)
                print()
                ...

            elif opsi_navigasi == "3": # TODO: Kembali ke menu utama
                print("=" * 29 + " Menu Utama " + "=" * 30)
                print()
                print("Lokasi saat ini:", planet_saat_ini) 
                print()
                print("Menu Utama:")
                print("1. Berangkat")
                print("2. Kirim Pesan")
                print("3. Baca Pesan")
                print("4. Lihat Laporan Perjalanan")
                print("5. Akhiri Perjalanan (keluar program)")

                print()
                pilihan = input("Masukkan pilihan: ")
                print()
    
                ...
            
            else:
                print("Mohon pilih opsi yang valid")
                print()

    elif pilihan == "2": # Kirim pesan menggunakan metode enkripsi
        
        print("=" * 25 + " Kirim Pesan Ke Bumi " + "=" * 25)
        print()

        while True:

            print("Metode Enkripsi:")
            print("1. Enkripsi berdasarkan Jarak Tempuh")
            print("2. Enkripsi berdasarkan Nama Planet Saat Ini")
            print("3. Enkripsi Biner")
            print("4. Enkripsi Heksadesimal")
            print("5. Enkripsi Membalik")
            print("6. Kembali ke Menu Utama")
            
            print()
            opsi_enkripsi = input("Masukkan pilihan: ")
            print()

            if opsi_enkripsi == "1": # TODO: Enkripsi berdasarkan jarak tempuh (integer)
                




                ...

                print()    
                print('Hasil Enkripsi : """' + ... + '"""')
                print()
                ...

            elif opsi_enkripsi == "2": # TODO: Enkripsi berdasarkan nama planet saat ini (string)

                ...

                print()
                print('Hasil Enkripsi : """' + ... + '"""')
                print()
                break

            elif opsi_enkripsi == "3": # TODO: Enkripsi Biner
                ...
            
            elif opsi_enkripsi == "4": # TODO: Enkripsi Heksadesimal
                ...
            
            elif opsi_enkripsi == "5": # TODO: Enkripsi Membalikkan String
                
                ...
            
            elif opsi_enkripsi == "6": # TODO: Kembali ke menu utama
                ...
            
            else:
                print("Mohon pilih opsi yang valid")
                print()
        
    elif pilihan == "3": # Baca pesan yang telah dikirim menggunakan metode dekripsi

        print("=" * 29 + " Baca Pesan " + "=" * 30)
        print()

        while True:

            print("Metode Dekripsi:")
            print("1. Dekripsi berdasarkan Jarak Tempuh")
            print("2. Dekripsi berdasarkan Nama Planet Saat Ini")
            print("3. Dekripsi Biner")
            print("4. Dekripsi Heksadesimal")
            print("5. Dekripsi Membalik")
            print("6. Dekripsi Brute Force (Jarak Tempuh)")
            print("7. Dekripsi Brute Force (Nama Planet (String))")
            print("8. Kembali ke Menu Utama")
            
            print()
            opsi_dekripsi = input("Masukkan pilihan: ")
            print()

            if opsi_dekripsi == "1": # TODO: Dekripsi berdasarkan jarak tempuh (integer)

                ...

                print()    
                print('Hasil Dekripsi: """' + ... + '"""')
                print()
                ...
            
            elif opsi_dekripsi == "2": # TODO: Dekripsi berdasarkan nama planet saat ini (string)

                ...

                print()
                print('Hasil Dekripsi: """' + ... + '"""')
                print()
                ...
            
            elif opsi_dekripsi == "3": # TODO: Dekripsi Biner

                ...

            elif opsi_dekripsi == "4": # TODO: Dekripsi Heksadesimal

                ...

            elif opsi_dekripsi == "5": # TODO: Dekripsi Membalikkan String
                ...
            
            elif opsi_dekripsi == "6": # TODO: Algoritma dekripsi brute force berdasarkan jarak tempuh (integer) [Soal Bonus]
                ...
            
            elif opsi_dekripsi == "7": # TODO: Algoritma dekripsi brute force berdasarkan nama planet (string) [Soal Bonus]
                ...
            
            elif opsi_dekripsi == "8": # TODO: Kembali ke menu utama
                ...
            
            else:
                print("Mohon pilih opsi yang valid")
                print()
                continue
        
    elif pilihan == "4":

        # TODO: Tampilkan output laporan perjalanan
        ...

        # TODO: Hitung jarak planet saat ini dari Bumi dengan pythagoras
        ...

        # TODO: Hitung sudut planet (derjat) saat ini dari Bumi
        ...

        # TODO: Tampilkan informasi lokasi saat ini
        ...
        
    elif pilihan == "5": # TODO: Akhiri perjalanan
        
        menetap = True
        print("=" * 26 + " Akhiri Perjalanan " + "=" * 26)
        print()
        print("Selamat menetap di Planet", ...)
        print()
        print("=" * 71)
        print()
    
    else: # TODO: Apabila input tidak valid
        ...