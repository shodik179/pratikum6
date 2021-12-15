datamahasiswa = {}
print("=" * 65)
print("|\tPROGRAM INPUT NILAI MAHASISWA\t|")
print("=" * 65)

def tambah ():
    nama = str (input("masukan nama : "))
    nim = int(input("masukan nim : "))
    tugas = int(input("masukan nilai tugas : "))
    uts = int(input("masukan nilai uts : "))
    uas = int(input("masukan nilai uas : "))
    akhir = (tugas /3) + (uts / 3.5) + (uas / 3.5)
    datamahasiswa[nama] = nim, tugas, uts, uas, akhir
    print("\nDATA BERHASIL DI TAMPILKAN!!")
def tampilkan():
    print("=" * 75)
    print("|" + "\t" * 3 + "DAFTAR NILAI MAHASISWA" +  "\t" * 3 + "|")
    print("=" * 75)
    print("| NO |   \tNAMA\t    |\tNIM\t|   TUGAS   |   UTS |   UAS |   AKHIR   |")
    print("=" * 75)
    for tampil in datamahasiswa.items():
        no = 0
        no += 1
        print ("| {6:2} |\t {0:15}  |{1:9} \t|  {2:5} | {3:3} | {4:3} | {5:5} |".format(tampil[0], tampil[1][0], tampil[1][1], tampil[1][2], tampil[1][3],"%.2f" % float(tampil[1][4]), no))
        print("=" * 75)
def hapus(nama):
    if nama in datamahasiswa.keys():
        nim = int(input("masukan nim : "))
        tugas = int(input("masukan nilai tugas : "))
        uts = int(input("masukan nilai uts : "))
        uas = int(input("masuka  nilai uas : "))
        akhir = (tugas /3) + (uts / 3.5) + (uas / 3.5)
        datamahasiswa[nama] = nim, tugas, uts, uas, akhir
        print("\nDATA BERHASIL DI UBAH!")
    else:
        print("\DATA TIDAK ADA")
while True:
    data = input(
        "\n 1 - tambah data,\t 2 - tampilkan data,\t 3 - hapus data,\t 4 - ubah data,\t 5 - keluar \n : "
    )
    if (data.lower() == '1'):
        tambah()

    elif (data.lower() == '2'):
        if datamahasiswa.items():
            tampilkan()
        else:
            print("=" * 75)
            print ("|" + "\t" * 3 + "DAFTAR NILAI MAHASISWA" + "\t" * 3 + "|")
            print("=" * 75)
            print("| NO |   \tNAMA\t    |\tNIM \t|  TUGAS   |   UTS |   UAS |   AKHIR   |")
            print("=" * 75)
            print("|    "+"\t" * 3 + "tidak ada data!" + "\t" * 4 + "   |")
            print("=" * 75)
    elif (data.lower() == '5'):
        print ("\nTERIMA KASIH!N \n")
    else:
        print("PILIHAN MENU TIDAK TE")

