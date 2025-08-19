import math

# Tugas Pemrograman 1 DDP-0
# Problem Setters: ARA, AYD, TAW, ICO

# Topik/Materi: Computational Thinking, Variable, Data Type, 
#               I/O, Basic Arithmetic, Math Library, 
#               Conditional Statement, dan Loop Statement

# Informasi perjalanan
jarak_tempuh = 120
koordinat_x_planet = 60
koordinat_y_planet = 80
durasi_perjalanan = 30
planet_saat_ini = "Bumi"
nama_rocket = "Acong"
kecepatan_rocket = 50
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
                pesan_enkripsi_caecar_input = input(str("Masukan Pesan Yang Ingin Dikirim: "))
                list_huruf_pesan_enkripsi_caecar_input = list(pesan_enkripsi_caecar_input)
                hasil = []

                mapping = {
                    "a": "d",
                    "b": "e",
                    "c": "f",
                    "d": "g",
                    "e": "h",
                    "f": "i",
                    "g": "j",
                    "h": "k",
                    "i": "l",
                    "j": "m",
                    "k": "n",
                    "l": "o",
                    "m": "p",
                    "n": "q",
                    "o": "r",
                    "p": "s",
                    "q": "t",
                    "r": "u",
                    "s": "v",
                    "t": "w",
                    "u": "x",
                    "v": "y",
                    "w": "z",
                    "x": "a",
                    "y": "b",
                    "z": "c",
                    "A": "D",
                    "B": "E",
                    "C": "F",
                    "D": "G",
                    "E": "H",
                    "F": "I",
                    "G": "J",
                    "H": "K",
                    "I": "L",
                    "J": "M",
                    "K": "N",
                    "L": "O",
                    "M": "P",
                    "N": "Q",
                    "O": "R",
                    "P": "S",
                    "Q": "T",
                    "R": "U",
                    "S": "V",
                    "T": "W",
                    "U": "X",
                    "V": "Y",
                    "W": "Z",
                    "X": "A",
                    "Y": "B",
                    "Z": "C",
                    "0": "0",
                    "1": "1",
                    "2": "2",
                    "3": "3",
                    "4": "4",
                    "5": "5",
                    "6": "6",
                    "7": "7",
                    "8": "8",
                    "9": "9",
                    ".": ".",
                    ",": ",",
                    "!": "!",
                    "?": "?",
                }

                for i in list_huruf_pesan_enkripsi_caecar_input:
                    if i in mapping:
                        hasil.append(mapping[i])   

                encrypted_jarak = "".join(hasil)

                print()    
                print('Hasil Enkripsi : """' + encrypted_jarak + '"""')
                print()
                ...

            elif opsi_enkripsi == "2": # TODO: Enkripsi berdasarkan nama planet saat ini (string)
                pesan_enkripsi_chiper_input = input(str("Masukan Pesan Yang Ingin Dikirim: ")).upper()
                kata_kunci_chiper_input = input(str("Masukan Nama Plante Saat Ini (Panjang Huruf Planet Harus Sama Dengan Pesan Yang Dikirim): ")).upper()
                list_huruf_pesan_enkripsi_chiper_input = list(pesan_enkripsi_chiper_input)
                list_huruf_kata_kunci_enkripsi_chiper_input = list(kata_kunci_chiper_input)
                Hasil = []

                mapping = {
                    "A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3,
                    "E": 4,
                    "F": 5,
                    "G": 6,
                    "H": 7,
                    "I": 8,
                    "J": 9,
                    "K": 10,
                    "L": 11,
                    "M": 12,
                    "N": 13,
                    "O": 14,
                    "P": 15,
                    "Q": 16,
                    "R": 17,
                    "S": 18,
                    "T": 19,
                    "U": 20,
                    "V": 21,
                    "W": 22,
                    "X": 23,
                    "Y": 24,
                    "Z": 25
                }

                if len(list_huruf_kata_kunci_enkripsi_chiper_input) == len(list_huruf_pesan_enkripsi_chiper_input):
                    for p,k in zip(list_huruf_kata_kunci_enkripsi_chiper_input, list_huruf_pesan_enkripsi_chiper_input):
                       angka_pesan = mapping[p]
                       angka_kata_kunci = mapping[k]
                       jumlah_geser_chiper = (angka_pesan + angka_kata_kunci) % 26
                       reverse_angka_huruf = {v:k for k, v in mapping.items()}
                       huruf_hasil = reverse_angka_huruf[jumlah_geser_chiper]
                       Hasil.append(huruf_hasil)

                    hasil_kata = "".join(Hasil)
                    print()
                    print('Hasil Enkripsi : """' + hasil_kata + '"""')
                    print()

                else:
                     print("Masukan Kata Kunci Yang Jumlah Karakternya Sama Dengan Jumlah Karakter Pesan") 

                break

            elif opsi_enkripsi == "3": # TODO: Enkripsi Biner
                pesan_enkripsi_biner_input = input(str("Masukan Pesan Yang Ingin Kamu Kirim: "))
                list_huruf_pesan_biner = list(pesan_enkripsi_biner_input)
                hasil = []

                mapping = {
                    " ": "00000000",
                    "!": "00000001",
                    "\"": "00000010",
                    "#": "00000011",
                    "$": "00000100",
                    "%": "00000101",
                    "&": "00000110",
                    "'": "00000111",
                    "(": "00001000",
                    ")": "00001001",
                    "*": "00001010",
                    "+": "00001011",
                    ",": "00001100",
                    "-": "00001101",
                    ".": "00001110",
                    "/": "00001111",
                    "0": "00010000",
                    "1": "00010001",
                    "2": "00010010",
                    "3": "00010011",
                    "4": "00010100",
                    "5": "00010101",
                    "6": "00010110",
                    "7": "00010111",
                    "8": "00011000",
                    "9": "00011001",
                    ":": "00011010",
                    ";": "00011011",
                    "<": "00011100",
                    "=": "00011101",
                    ">": "00011110",
                    "?": "00011111",
                    "@": "00100000",
                    "A": "00100001",
                    "B": "00100010",
                    "C": "00100011",
                    "D": "00100100",
                    "E": "00100101",
                    "F": "00100110",
                    "G": "00100111",
                    "H": "00101000",
                    "I": "00101001",
                    "J": "00101010",
                    "K": "00101011",
                    "L": "00101100",
                    "M": "00101101",
                    "N": "00101110",
                    "O": "00101111",
                    "P": "00110000",
                    "Q": "00110001",
                    "R": "00110010",
                    "S": "00110011",
                    "T": "00110100",
                    "U": "00110101",
                    "V": "00110110",
                    "W": "00110111",
                    "X": "00111000",
                    "Y": "00111001",
                    "Z": "00111010",
                    "[": "00111011",
                    "\\": "00111100",
                    "]": "00111101",
                    "^": "00111110",
                    "_": "00111111",
                    "`": "01000000",
                    "a": "01000001",
                    "b": "01000010",
                    "c": "01000011",
                    "d": "01000100",
                    "e": "01000101",
                    "f": "01000110",
                    "g": "01000111",
                    "h": "01001000",
                    "i": "01001001",
                    "j": "01001010",
                    "k": "01001011",
                    "l": "01001100",
                    "m": "01001101",
                    "n": "01001110",
                    "o": "01001111",
                    "p": "01010000",
                    "q": "01010001",
                    "r": "01010010",
                    "s": "01010011",
                    "t": "01010100",
                    "u": "01010101",
                    "v": "01010110",
                    "w": "01010111",
                    "x": "01011000",
                    "y": "01011001",
                    "z": "01011010",
                    "{": "01011011",
                    "|": "01011100",
                    "}": "01011101",
                    "~": "01011110",
                }

                for p in (list_huruf_pesan_biner):
                    hasil_huruf_biner = mapping[p]
                    hasil.append(hasil_huruf_biner)

                huruf_hasil_biner = ("".join(hasil))

                print()
                print('Hasil Enkripsi : """' + huruf_hasil_biner + '"""')
                print()
                ...
            
            elif opsi_enkripsi == "4": # TODO: Enkripsi Heksadesimal
                pesan_enkripsi_haksadesimal_input = input(str("Masukan Pesan Yang Ingin Kamu Kirim: "))
                list_huruf_pesan_enkripsi_haksadesimal = list(pesan_enkripsi_haksadesimal_input)
                hasil = []

                mapping = {
                    "A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3,
                    "E": 4,
                    "F": 5,
                    "G": 6,
                    "H": 7,
                    "I": 8,
                    "J": 9,
                    "K": 10,
                    "L": 11,
                    "M": 12,
                    "N": 13,
                    "O": 14,
                    "P": 15,
                    "Q": 16,
                    "R": 17,
                    "S": 18,
                    "T": 19,
                    "U": 20,
                    "V": 21,
                    "W": 22,
                    "X": 23,
                    "Y": 24,
                    "Z": 25,
                    "a": 26,
                    "b": 27,
                    "c": 28,
                    "d": 29,
                    "e": 30,
                    "f": 31,
                    "g": 32,
                    "h": 33,
                    "i": 34,
                    "j": 35,
                    "k": 36,
                    "l": 37,
                    "m": 38,
                    "n": 39,
                    "o": 40,
                    "p": 41,
                    "q": 42,
                    "r": 43,
                    "s": 44,
                    "t": 45,
                    "u": 46,
                    "v": 47,
                    "w": 48,
                    "x": 49,
                    "y": 50,
                    "z": 51,
                    "0": 52,
                    "1": 53,
                    "2": 54,
                    "3": 55,
                    "4": 56,
                    "5": 57,
                    "6": 58,
                    "7": 59,
                    "8": 60,
                    "9": 61,
                    "!": 62,
                    "@": 63,
                    "#": 64,
                    "$": 65,
                    "%": 66,
                    "^": 67,
                    "&": 68,
                    "*": 69,
                    "(": 70,
                    ")": 71,
                    "-": 72,
                    "_": 73,
                    "=": 74,
                    "+": 75,
                    "[": 76,
                    "]": 77,
                    "{": 78,
                    "}": 79,
                    "|": 80,
                    "\\": 81,
                    ";": 82,
                    ":": 83,
                    "'": 84,
                    "\"": 85,
                    ",": 86,
                    ".": 87,
                    "<": 88,
                    ">": 89,
                    "/": 90,
                    "?": 91,
                    " ": 92
                }

                for p in (list_huruf_pesan_enkripsi_haksadesimal):
                    huruf_angka = mapping[p]
                    hasil.append(huruf_angka)

                hasil_haksadesimal = ("".join(str(x) for x in hasil))

                print()
                print('Hasil Enkripsi : """' + hasil_haksadesimal + '"""')
                print()
                ...
            
            elif opsi_enkripsi == "5": # TODO: Enkripsi Membalikkan String
                pesan_enkripsi_balik_string = input(str("Masukan Pesan Yang Ingin Kamu Kirim: "))
                hasil = []
                
                balik_huruf = reversed(pesan_enkripsi_balik_string)
                hasil_balik = ("".join(balik_huruf))

                print()
                print('Hasil Enkripsi : """' + hasil_balik + '"""')
                print()
                
                ...
            
            elif opsi_enkripsi == "6": # TODO: Kembali ke menu utama
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
                pesan_deskripsi_caecar_input = input(str("Masukan Kode Yang Ingin Dibaca: "))
                list_huruf_deskripsi_caecar = list(pesan_deskripsi_caecar_input)
                hasil = []

                mapping = {
                    "a": "x",
                    "b": "y",
                    "c": "z",
                    "d": "a",
                    "e": "b",
                    "f": "c",
                    "g": "d",
                    "h": "e",
                    "i": "f",
                    "j": "g",
                    "k": "h",
                    "l": "i",
                    "m": "j",
                    "n": "k",
                    "o": "l",
                    "p": "m",
                    "q": "n",
                    "r": "o",
                    "s": "p",
                    "t": "q",
                    "u": "r",
                    "v": "s",
                    "w": "t",
                    "x": "u",
                    "y": "v",
                    "z": "w",
                    "A": "X",
                    "B": "Y",
                    "C": "Z",
                    "D": "A",
                    "E": "B",
                    "F": "C",
                    "G": "D",
                    "H": "E",
                    "I": "F",
                    "J": "G",
                    "K": "H",
                    "L": "I",
                    "M": "J",
                    "N": "K",
                    "O": "L",
                    "P": "M",
                    "Q": "N",
                    "R": "O",
                    "S": "P",
                    "T": "Q",
                    "U": "R",
                    "V": "S",
                    "W": "T",
                    "X": "U",
                    "Y": "V",
                    "Z": "W",
                    "0": "0",
                    "1": "1",
                    "2": "2",
                    "3": "3",
                    "4": "4",
                    "5": "5",
                    "6": "6",
                    "7": "7",
                    "8": "8",
                    "9": "9",
                    ".": ".",
                    ",": ",",
                    "!": "!",
                    "?": "?",
                }

                for i in list_huruf_deskripsi_caecar:
                    if i in mapping:
                        hasil.append(mapping[i])
                
                hasil_balik_caecar = ("".join(hasil))

                print()    
                print('Hasil Dekripsi: """' + hasil_balik_caecar + '"""')
                print()
                ...
            
            elif opsi_dekripsi == "2": # TODO: Dekripsi berdasarkan nama planet saat ini (string)
                pesan_deskripsi_cipher_input = input(str("Masukan Kode Yang Ingin Dibaca: "))
                kunci_deskripsi_chiper_input = input(str("Masukan Kata Kunci: "))
                list_huruf_deskripsi_cipher = list(pesan_deskripsi_cipher_input)
                list_huruf_kunci_deskripsi_chiper = list(kunci_deskripsi_chiper_input)
                hasil = []

                mapping = {
                    "A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3,
                    "E": 4,
                    "F": 5,
                    "G": 6,
                    "H": 7,
                    "I": 8,
                    "J": 9,
                    "K": 10,
                    "L": 11,
                    "M": 12,
                    "N": 13,
                    "O": 14,
                    "P": 15,
                    "Q": 16,
                    "R": 17,
                    "S": 18,
                    "T": 19,
                    "U": 20,
                    "V": 21,
                    "W": 22,
                    "X": 23,
                    "Y": 24,
                    "Z": 25
                }

                if len(list_huruf_deskripsi_cipher) == len(list_huruf_kunci_deskripsi_chiper):
                    for p,k in zip(list_huruf_deskripsi_cipher, list_huruf_kunci_deskripsi_chiper):
                        angka_huruf = mapping[p]
                        angka_kunci = mapping[k]
                        jumlah_geser = (angka_huruf - angka_kunci) % 26
                        reverse_angka_huruf = {v:k for k,v in mapping.items()}
                        hasil_balik = reverse_angka_huruf[jumlah_geser]
                        hasil.append(hasil_balik)

                hasil_kata = ("".join(hasil))

                print()
                print('Hasil Dekripsi: """' + hasil_kata + '"""')
                print()
                ...
            
            elif opsi_dekripsi == "3": # TODO: Dekripsi Biner
                pesan_deskripsi_biner = input(str("Masukan Kode Yang Ingin Kamu Baca: "))
                import textwrap
                list_huruf_deskripsi_biner = textwrap.wrap(pesan_deskripsi_biner, 8)
                hasil = []

                mapping = {
					"00000000": " ",
					"00000001": "!",
					"00000010": "\"",
					"00000011": "#",
					"00000100": "$",
					"00000101": "%",
					"00000110": "&",
					"00000111": "'",
					"00001000": "(",
					"00001001": ")",
					"00001010": "*",
					"00001011": "+",
					"00001100": ",",
					"00001101": "-",
					"00001110": ".",
					"00001111": "/",
					"00010000": "0",
					"00010001": "1",
					"00010010": "2",
					"00010011": "3",
					"00010100": "4",
					"00010101": "5",
					"00010110": "6",
					"00010111": "7",
					"00011000": "8",
					"00011001": "9",
					"00011010": ":",
					"00011011": ";",
					"00011100": "<",
					"00011101": "=",
					"00011110": ">",
					"00011111": "?",
					"00100000": "@",
					"00100001": "A",
					"00100010": "B",
					"00100011": "C",
					"00100100": "D",
					"00100101": "E",
					"00100110": "F",
					"00100111": "G",
					"00101000": "H",
					"00101001": "I",
					"00101010": "J",
					"00101011": "K",
					"00101100": "L",
					"00101101": "M",
					"00101110": "N",
					"00101111": "O",
					"00110000": "P",
					"00110001": "Q",
					"00110010": "R",
					"00110011": "S",
					"00110100": "T",
					"00110101": "U",
					"00110110": "V",
					"00110111": "W",
					"00111000": "X",
					"00111001": "Y",
					"00111010": "Z",
					"00111011": "[",
					"00111100": "\\",
					"00111101": "]",
					"00111110": "^",
					"00111111": "_",
					"01000000": "`",
					"01000001": "a",
					"01000010": "b",
					"01000011": "c",
					"01000100": "d",
					"01000101": "e",
					"01000110": "f",
					"01000111": "g",
					"01001000": "h",
					"01001001": "i",
					"01001010": "j",
					"01001011": "k",
					"01001100": "l",
					"01001101": "m",
					"01001110": "n",
					"01001111": "o",
					"01010000": "p",
					"01010001": "q",
					"01010010": "r",
					"01010011": "s",
					"01010100": "t",
					"01010101": "u",
					"01010110": "v",
					"01010111": "w",
					"01011000": "x",
					"01011001": "y",
					"01011010": "z",
					"01011011": "{",
					"01011100": "|",
					"01011101": "}",
					"01011110": "~",
                }
                
                for p in (list_huruf_deskripsi_biner):
                    hasil_huruf_biner = mapping[p]
                    hasil.append(hasil_huruf_biner)

                hasil_kata = ("".join(hasil))

                print()
                print('Hasil Dekripsi: """' + hasil_kata + '"""')
                print()

                ...

            elif opsi_dekripsi == "4": # TODO: Dekripsi Heksadesimal
                pesan_deskripsi_heksadesimal = input(str("Masukan Kode Yang Ingin Kamu Baca (Harus diberi jarak spasi dari setiap pasang angka): "))
                list_huruf_heksadesimal = pesan_deskripsi_heksadesimal.split()
                hasil = []

                mapping = {
                    0: "A",
                    1: "B",
                    2: "C",
                    3: "D",
                    4: "E",
                    5: "F",
                    6: "G",
                    7: "H",
                    8: "I",
                    9: "J",
                    10: "K",
                    11: "L",
                    12: "M",
                    13: "N",
                    14: "O",
                    15: "P",
                    16: "Q",
                    17: "R",
                    18: "S",
                    19: "T",
                    20: "U",
                    21: "V",
                    22: "W",
                    23: "X",
                    24: "Y",
                    25: "Z",
                    26: "a",
                    27: "b",
                    28: "c",
                    29: "d",
                    30: "e",
                    31: "f",
                    32: "g",
                    33: "h",
                    34: "i",
                    35: "j",
                    36: "k",
                    37: "l",
                    38: "m",
                    39: "n",
                    40: "o",
                    41: "p",
                    42: "q",
                    43: "r",
                    44: "s",
                    45: "t",
                    46: "u",
                    47: "v",
                    48: "w",
                    49: "x",
                    50: "y",
                    51: "z",
                    52: "0",
                    53: "1",
                    54: "2",
                    55: "3",
                    56: "4",
                    57: "5",
                    58: "6",
                    59: "7",
                    60: "8",
                    61: "9",
                    62: "!",
                    63: "@",
                    64: "#",
                    65: "$",
                    66: "%",
                    67: "^",
                    68: "&",
                    69: "*",
                    70: "(",
                    71: ")",
                    72: "-",
                    73: "_",
                    74: "=",
                    75: "+",
                    76: "[",
                    77: "]",
                    78: "{",
                    79: "}",
                    80: "|",
                    81: "\\",
                    82: ";",
                    83: ":",
                    84: "'",
                    85: "\"",
                    86: ",",
                    87: ".",
                    88: "<",
                    89: ">",
                    90: "/",
                    91: "?",
                    92: " "
                }


                for i in (list_huruf_heksadesimal):
                    huruf_hekadesimal = mapping[int(i)]
                    hasil.append(huruf_hekadesimal)
                
                hasil_kata = ("".join(str(x) for x in hasil))

                print()
                print('Hasil Dekripsi: """' + hasil_kata + '"""')
                print()

                ...

            elif opsi_dekripsi == "5": # TODO: Dekripsi Membalikkan String
                pesan_enkripsi_balik_string = input(str("Masukan Pesan Yang Ingin Kamu Kirim: "))
                hasil = []
                
                balik_huruf = reversed(pesan_enkripsi_balik_string)
                hasil_balik = ("".join(balik_huruf))

                print()
                print('Hasil Enkripsi : """' + hasil_balik + '"""')
                print()
                ...
            
            elif opsi_dekripsi == "6": # TODO: Algoritma dekripsi brute force berdasarkan jarak tempuh (integer) [Soal Bonus]

                print("Maaf Fitur Ini Masih Dalam Riset dan Pengembangan, Anda Dapat Kembali Ke Menu Utama")

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
            
            elif opsi_dekripsi == "7": # TODO: Algoritma dekripsi brute force berdasarkan nama planet (string) [Soal Bonus]

                print("Maaf Fitur Ini Masih Dalam Riset dan Pengembangan, Anda Dapat Kembali Ke Menu Utama")

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
            
            elif opsi_dekripsi == "8": # TODO: Kembali ke menu utama
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
                continue
        
    elif pilihan == "4":

        # TODO: Tampilkan output laporan perjalanan
        print("Jarak Tempuh: ", jarak_tempuh)
        print("Koordinat X: ", koordinat_x_planet)
        print("Koordinat Y: ", koordinat_y_planet)
        print("Durasi Perjalanan: ", durasi_perjalanan)
        print("Planet Saat Ini: ", planet_saat_ini)
        print("Nama Roket: ", nama_rocket)
        print("Kecepatan Roket: ", kecepatan_rocket)
        ...

        # TODO: Hitung jarak planet saat ini dari Bumi dengan pythagoras
        koordinat_x_planet_kertasian_input = int(input("Berapa Koordinat X: "))
        koordinat_y_planet_kertasian_input = int(input("Berapa Koordinat Y: "))
        planet_saat_ini_kertasian_input = input("Planet Saat Ini: ")
                    
        jarak_tempuh_kertasian_hasil = math.sqrt(abs(koordinat_x_planet_kertasian_input ** 2 - koordinat_y_planet_kertasian_input ** 2))
        
        print("Jarak Planet dari Bumi: ", jarak_tempuh_kertasian_hasil)
        ...

        # TODO: Hitung sudut planet (derjat) saat ini dari Bumi
        sudut_planet_polar_input = int(input("Berapa Sudut: "))
        jarak_planet_polar_input = int(input("Berapa Jarak: "))
        planet_saat_ini_polar_input = input("Planet Saat Ini: ")
        konversi_sudut_radian = math.radians(sudut_planet_polar_input)
        print("Sudut: ", konversi_sudut_radian)
        ...

        # TODO: Tampilkan informasi lokasi saat ini
        print("Planet Saat Ini: ", planet_saat_ini)
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
        print("Mohon pilih opsi yang valid")
        print()
        continue
        ...