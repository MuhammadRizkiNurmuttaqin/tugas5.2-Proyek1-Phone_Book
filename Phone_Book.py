import os
import re

# modul untuk menampilkan menu fitur
def display_menu() :
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Update Kontak")
    print("4. Hapus Kontak")
    print("5. Tampilkan seluruh kontak")
    print("6. Keluar Program")

# modul untuk menambahkan kontak
def tambah_kontak(nama, nomor) :
    phone_book[nama] = nomor
    if os.path.isfile("Kontak.txt") :
        with open("Kontak.txt",'a') as file:
            file.write("{}\n".format(nama+"\t\t\t"+nomor))
        
    else :
        with open("Kontak.txt",'w') as file:
            file.write("{}\n".format(nama+"\t\t\t"+nomor))

    print(f"# {nama} sudah di tambahkan kedalam kontak #")
# modul untuk mencari kontak
def cari_kontak(nama) :
    cek = False
    with open("Kontak.txt",'r') as file:
        for line in file:
            if nama in line:
                print(line)
                cek = True
    
    if cek != True:
        print("Kontak yang dicari tidak ada")

# modul untuk menghapus kontak        
def hapus_kontak(nama):
    hapus = nama
    with open("Kontak.txt",'r') as file:
        cari = file.readlines()
    
    with open("Kontak.txt",'w') as file:
        for line in cari:
            if not line.startswith(hapus):
                file.write(line)
# modul untuk menampilkan semua kontak
def tampil_semuakontak():
    with open("Kontak.txt",'r') as file:
        print(file.read())

# modul untuk mengupdate kontak 
def update_kontak(nama,nomor):
    pilih = input("apakah anda ingin mengganti Nama atau Nomor?")
    if pilih == "Nama":
        with open("Kontak.txt",'r') as file:
            isiFile = file.read()
        
        baru = input ("masukan nama yang baru : ")
        isiFile = isiFile.replace(nama,baru)

        with open("Kontak.txt",'w') as file:
            file.write(isiFile)
    elif pilih == "Nomor":
        with open("Kontak.txt",'r') as file:
            isiFile = file.read()

        baru = input("masukan nomor yang baru : ")
        isiFile = isiFile.replace(nomor,baru)

        with open("Kontak.txt",'w') as file:
            file.write(isiFile)


# Main Program    
phone_book = {}
repeat = True
while repeat == True:
    display_menu()
    i = input("Masukan angka sesuai yang ingin dipilih : ")

    if i == '1' :
        print("\nMasukan kontak yang ingin ditambahkan : ")
        Nama = input ("Nama :")
        Nomor = input("Nomor :")
        tambah_kontak(Nama, Nomor)
    elif i == '2' :
        Nama = input("\nMasukan nama kontak yang dicari : ")
        print("\n===============Kontak===============")
        cari_kontak(Nama)
    elif i == '3' :
        tampil_semuakontak()
        Nama = input("Masukan nama kontak yang ingin anda ubah : ")
        Nomor = input("Masukan nomor yang ingin anda ubah : ")
        update_kontak(Nama, Nomor)

    elif i == '4' :
        tampil_semuakontak()
        Nama = input("Masukan nama kontak yang ingin anda hapus : ")
        hapus_kontak(Nama)
        print("\n")
    elif i == '5':
        print("\n\tTampilkan semua kontak")
        print("====================================")
        tampil_semuakontak()

    elif i == '6':
        repeat = False