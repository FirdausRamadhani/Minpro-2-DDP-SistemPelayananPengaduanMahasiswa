import time
import pwinput
import os

akun = {
    "mahasiswa": {
        "username" : "Mahasiswa",
        "password" : "inimahasiswa"
    },
    "admin" : {
        "username" : "Admin",
        "password" : "iniadmin"
    }
}

semua_pengaduan = []
status = ("Menunggu", "Sedang Diproses", "Selesai")
status_pengaduan = []

# FUNGSI LOGIN
def login():
    percobaan = 0 
    while True:
        print("=" * 40)
        print("             SILAHKAN LOGIN")
        print("      Masukkan Username dan Password")
        print("=" * 40)
        username = input("Masukkan Username : ")
        password = pwinput.pwinput("Masukkan Password : ")

        if username == akun["mahasiswa"]["username"] and password == akun ["mahasiswa"]["password"]:
            print("\nLogin Berhasil")
            return "mahasiswa"
        elif username == akun["admin"]["username"] and password == akun["admin"]["password"]:
            print("\nLogin Berhasil")
            return "admin"
        else:
            print("\nUsername atau Password salah. Silakan coba lagi.")
            percobaan += 1
            if percobaan == 3:
                print("\nTerlalu banyak percobaan login. Silahkan coba lagi dalam.")
                time.sleep(2)
                for i in range(10, 0, -1):
                    print(i)
                    time.sleep(1)
                    percobaan = 0

# MENU MAHASISWA
def menu_mahasiswa():
    while True:
        print("\nMenu Mahasiswa:")
        print("1. Buat Pengaduan")
        print("2. Lihat Status Pengaduan")
        print("3. Edit Pengaduan")
        print("4. Hapus Pengaduan")
        print("0. Logout")

        pilihan = input("Pilih menu (1/2/3/4/0): ")

        if pilihan == "1":
            pengaduan = input("\nMasukkan pengaduan: ")
            semua_pengaduan.append(pengaduan)
            status_pengaduan.append(status[0])
            print("Pengaduan berhasil ditambahkan.")
        elif pilihan == "2":
            print("\n=== Pengaduan Saya ===")
            if len(semua_pengaduan) == 0 :
                print("\nBelum ada pengaduan.")
            else:
                for i in range(len(semua_pengaduan)):
                    print(str(i + 1) + ". ", semua_pengaduan[i])
                    print("Status : ",status_pengaduan[i])
        elif pilihan == "3":
            if len(semua_pengaduan) == 0:
                print("\nBelum ada pengaduan.")
            else:
                print("\n=== Edit Pengaduan ===")
                for i in range(len(semua_pengaduan)):
                    print(str(i + 1) + ". ", semua_pengaduan[i])
                index = int(input("Masukkan nomor pengaduan yang ingin diedit : ")) - 1
                if 0 <= index < len(semua_pengaduan):
                    pengaduan_baru = input("Masukkan pengaduan baru : ")
                    semua_pengaduan[index] = pengaduan_baru
                    print("Pengaduan berhasil diubah.")
                else:
                    print("\nNomor pengaduan tidak valid. Silakan coba lagi.")
        elif pilihan == "4":
            if len(semua_pengaduan) == 0:
                print("\nBelum ada pengaduan.")
            else:
                print("\n=== Hapus Pengaduan ===")
                for i in range(len(semua_pengaduan)):
                    print(str(i + 1) + ". ", semua_pengaduan[i])
                index = int(input("Masukkan nomor pengaduan yang ingin dihapus : ")) - 1
                if 0 <= index < len(semua_pengaduan):
                    del semua_pengaduan[index]
                    del status_pengaduan[index]
                    print("Pengaduan berhasil dihapus.")
                else:
                    print("\nNomor pengaduan tidak valid. Silakan coba lagi.")
        elif pilihan == "0":
            print("\nAnda telah logout.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

# MENU ADMIN
def menu_admin():
    while True:
        print("\nMenu Admin:")
        print("1. Lihat Semua Pengaduan")
        print("2. Hapus Pengaduan")
        print("3. Ubah Status Pengaduan")
        print("0. Logout")
        pilihan = input("Pilih menu (1/2/3/0): ")
        if pilihan == "1":
            if semua_pengaduan:
                print("\nDaftar Pengaduan:")
                for i in range(len(semua_pengaduan)):
                    print(str(i + 1) + ". ", semua_pengaduan[i])
                    print("Status : ",status_pengaduan[i])
            else:
                print("Belum ada pengaduan.")
        elif pilihan == "2":
            if semua_pengaduan:
                print("\nDaftar Pengaduan:")
                for i in range(len(semua_pengaduan)):
                    print(str(i + 1) + ". ", semua_pengaduan[i])
                index = int(input("Masukkan nomor pengaduan yang ingin dihapus : ")) - 1
                if 0 <= index < len(semua_pengaduan):
                    del semua_pengaduan[index]
                    del status_pengaduan[index]
                    print("Pengaduan berhasil dihapus.")
                else:
                    print("\nNomor pengaduan tidak valid. Silakan coba lagi.")
            else:
                print("\nBelum ada pengaduan.")
        elif pilihan == "3":
            if len(semua_pengaduan) == 0:
                print("\nBelum ada Pengaduan.")
            else:
                print("\n=== Ubah Status Pengaduan ===")
                for i in range(len(semua_pengaduan)):
                    print(str(i + 1) + ". ", semua_pengaduan[i], "-", status_pengaduan[i])
                nomor = int(input("Pilih nomor pengaduan : "))
                if nomor < 1 or nomor > len(semua_pengaduan):
                    print("\nPilihan tidak valid. Silakan coba lagi.")
                else:
                    print("\nPilih Status : ")
                    print("1. Sedang Diproses")
                    print("2. Selesai")
                    pilihan_status = input("Pilih status : ")
                    if pilihan_status == "1":
                        status_pengaduan[nomor - 1] = status[1]
                        print("Status berhasil diubah")
                    elif pilihan_status == "2":
                        status_pengaduan[nomor - 1] = status[2]
                        print("Status berhasil diubah")
                    else:
                        print("\nPilihan tidak valid. Silakan coba lagi.")
        elif pilihan == "0" :
            print("\nAnda Telah Logout.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

# MAIN PROGRAM
def main():
    while True:
        print("=" * 40)
        print("  SISTEM PELAYANAN PENGADUAN MAHASISWA")
        print("=" * 40)
        print("Silakan login untuk melanjutkan.")
        print("1. Login")
        print("0. Keluar")
        pilihan = input("Pilih menu (1/0) : ")

        os.system("cls" if os.name == "nt" else "clear")
        if pilihan == "1":
            role = login()
            if role == "mahasiswa":
                menu_mahasiswa()
            elif role =="admin":
                menu_admin()
        elif pilihan == "0":
            print("=" * 70)
            print("  TERIMA KASIH TELAH MENGGUNAKAN SISTEM PELAYANAN PENGADUAN MAHASISWA.")
            print("=" * 70)
            break
        else:
            print("\nPilihan tidak valid. Silahkan coba lagi.")

main()