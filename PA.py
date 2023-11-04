import os
import pwinput
from prettytable import PrettyTable
import json

# Fungsi untuk menyimpan daftar kamar ke file JSON
def simpan_daftar_kamar():
    with open("daftar_kamar.json", "w") as kamar_file:
        daftar_kamar_json = {"kamar": daftar_kamar}
        json.dump(daftar_kamar_json, kamar_file)

def menu_admin():
        print("+---------------------------------------------------------+")
        print("| [1] MENAMBAH DAFTAR KAMAR                               |")
        print("| [2] MENAMPILKAN DAFTAR KAMAR                            |")
        print("| [3] MENGUBAH DAFTAR KAMAR                               |")
        print("| [4] MENGHAPUS DAFTAR KAMAR                              |")
        print("| [5] MENAMBAH SALDO CUSTOMER                             |")
        print("| [6] KELUAR                                              |")
        print("+---------------------------------------------------------+")
# Fungsi untuk menampilkan daftar kamar
def tampilkan_daftar_kamar():
            os.system("cls")
            print("+---------------------------------------------------------+")
            print("|                MENAMPILKAN DAFTAR KAMAR                 |")
            print("+---------------------------------------------------------+")
            if not daftar_kamar:
                print("Daftar kamar kosong.")
            else:
                print("Daftar Kamar:")
                daftar_kamar_table = PrettyTable()
                daftar_kamar_table.field_names = ["Nomor kamar", "Tipe kamar", "Harga kamar", "Status kamar"]
                for kamar in daftar_kamar:
                    daftar_kamar_table.add_row([kamar["nomor_kamar"], kamar["tipe_kamar"], f"Rp {kamar['harga_kamar']}",kamar["status"]])
                print(daftar_kamar_table)
                    
# Fungsi untuk menambah kamar
def tambah_kamar():
    while True:
        try:
            os.system("cls")
            print("+------------------------------------------------------------+")
            print("|                 MENAMBAHKAN DAFTAR KAMAR                   |")
            print("+------------------------------------------------------------+")
            no_kamar = int(input("Masukkan nomor kamar: "))
            print("+------------------------------------------------------------+")
            print("+------------------------------------------------------------+")
            print("|       TIPE KAMAR      |     HARGA KAMAR     |    STATUS    |")
            print("+-----------------------|---------------------|--------------+")
            print("|        STANDARD       |     Rp. 500.000     |   TERSEDIA   |")
            print("|        SUPERIOR       |     Rp. 750.000     |   TERSEDIA   |")
            print("|         SUITE         |    Rp. 1.000.000    |   TERSEDIA   |")
            print("|         DELUXE        |    Rp. 1.500.000    |   TERSEDIA   |")
            print("|      PRESIDENTIAL     |    Rp. 2.000.000    |   TERSEDIA   |")
            print("+-----------------------|------------------------------------+")
            
            pilih_tipe_kamar = int(input("Masukkan pilihan tipe kamar (1/2/3/4/5): "))      
            if pilih_tipe_kamar == 1:
                    jenis_kamar = "standard"
                    harga = 500000
                    status = "tersedia"
            elif pilih_tipe_kamar== 2:
                    jenis_kamar = "superior"
                    harga = 750000
                    status = "tersedia"
            elif pilih_tipe_kamar == 3:
                    jenis_kamar = "Suite"
                    harga = 1000000
                    status = "tersedia"
            elif pilih_tipe_kamar == 4:
                    jenis_kamar = "deluxe"
                    harga = 1500000
                    status = "tersedia"
            elif pilih_tipe_kamar == 5:
                    jenis_kamar = "Presidential"
                    harga = 2000000
                    status = "tersedia"
                    print(f"Anda memilih {jenis_kamar}. Harga: {harga} Status: {status}")
                    return
            else:
                print("Pilihan tipe kamar tidak valid. Silakan masukkan angka antara 1 hingga 5.")
                
            for kamar in daftar_kamar:
                if kamar["nomor_kamar"] == no_kamar:
                    print(f"Kamar dengan nomor {no_kamar} sudah ada.")
                    return
                daftar_kamar.append({"nomor_kamar": no_kamar, "tipe_kamar": jenis_kamar, "harga_kamar": harga, "status":status})
            simpan_daftar_kamar()
            print(f"Kamar {no_kamar} ({jenis_kamar}) telah ditambahkan.")
            break
    
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            input("Tekan Enter untuk mencoba lagi: ")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            break
            
            
        
# Fungsi untuk mengubah kamar
def ubah_daftar_kamar():
    while True:
        try: 
            os.system("cls")
            tampilkan_daftar_kamar()
            print("+---------------------------------------------------------+")
            print("|                MENAMBAHKAN DAFTAR KAMAR                 |")
            print("+---------------------------------------------------------+")
            no_kamar = int(input("Masukkan nomor kamar yang ingin diubah: "))
            for kamar in daftar_kamar:
                try:
                    if kamar["nomor_kamar"] == no_kamar:
                        jenis_kamar = input("Masukkan tipe kamar baru: ")
                        harga = int(input("Masukkan harga kamar baru: "))
                        status = ("tersedia")
                        print("+--------------------------------------------------------+")
                        kamar["tipe_kamar"] = jenis_kamar
                        kamar["harga_kamar"] = harga
                        kamar["status_kamar"] = status
                        simpan_daftar_kamar()
                        print(f"Kamar {no_kamar} telah diubah.")
                        return
                except Exception as e:
                    print(f"Terjadi kesalahan saat penginputan data {e}")
                    input("Tekan Enter untuk mencoba lagi: ")
                    break
                print(f"Kamar dengan nomor {no_kamar} tidak ditemukan.")
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            break
        
def hapus_kamar():
    while True:
        try:
            tampilkan_daftar_kamar()
            os.system("cls")
            print("+---------------------------------------------------------+")
            print("|                MENGHAPUS DAFTAR KAMAR                   |")
            print("+---------------------------------------------------------+")
            no_kamar = int(input("Masukkan nomor kamar yang ingin dihapus: "))
            for kamar in daftar_kamar:
                if kamar["nomor_kamar"] == no_kamar:
                    daftar_kamar.remove(kamar)
                    simpan_daftar_kamar()
                    print(f"Kamar {no_kamar} telah dihapus.")
                    return
                else:
                    print(f"Kamar dengan nomor {no_kamar} tidak ditemukan.")
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            break
        
# Fungsi untuk menambah saldo customer
def tambah_saldo_customer():
    while  True:
        try:
            os.system("cls")
            print("==============| MASUKKAN ID |=================")  
            customer_id = int(input("Masukkan ID customer: "))
            jumlah_topup = 0

            # Inisialisasi customer_data
            with open("customer_data.json", "r") as customer_file:
                    customer_data = json.load(customer_file)

            for customer_username, data in customer_data.items():
                    
                    if data["id"] == customer_id:
                        data["saldo"] >=0  
                        print(f"Nama Customer: {customer_username}")
                        print("==============================================")
                        while True:
                            konfirmasi = input("Apakah anda ingin melakukan top up? (y/t): ").strip().lower()
                            if konfirmasi == 'y':
                                os.system("cls")
                                print("+--------------------------------------------------+")
                                print("|               |  TOP UP SALDO  |                 |")
                                print("+--------------------------------------------------+")
                                print("| [1] Rp. 500.000                                  |")
                                print("| [2] Rp. 1.000.000                                |")
                                print("| [3] Rp. 1.500.000                                |")
                                print("| [4] Rp. 2.000.000                                |")
                                print("| [5] Rp. 2.500.000                                |")
                                print("| [6]  NOMINAL LAINNYA                             |")
                                print("+--------------------------------------------------+")
                                
                                while True:
                                    pilih_up = input("Pilih opsi top up anda : ")
                                    if pilih_up in ["1", "2", "3", "4", "5", "6"]: 
                                        
                                        pilihan = int(pilih_up)
                                        if pilihan == 1 and jumlah_topup >=0 :
                                            jumlah_topup = 500000
                                        elif pilihan == 2 and jumlah_topup >=0:
                                            jumlah_topup = 1000000
                                        elif pilihan == 3 and jumlah_topup >=0:
                                            jumlah_topup = 1500000
                                        elif pilihan == 4 and jumlah_topup >=0:
                                            jumlah_topup = 2000000
                                        elif pilihan == 5 and jumlah_topup >=0:
                                            jumlah_topup = 2500000
                                        elif pilihan == 6 and jumlah_topup >=0 :
                                            jumlah_topup = int(input("masukan nominal top up Rp."))
                                            if jumlah_topup <0:
                                                print("NOMINAL TOP UP TIDAK VALID")
                                                return
                                        else:
                                            print("Pilihan saldo tidak valid.")
                                            return
                                        if jumlah_topup >=0 :
                                            data["saldo"] += jumlah_topup
                                            print("Saldo Telah Ditambahkan")
                                            print(f"Id Customer: {customer_id}")
                                            print(f"Nama Customer: {customer_username}")
                                            print(f"Saldo: Rp {data['saldo']}")
                                            break
                            elif konfirmasi == 't':
                                break
                            else:
                                print("Masukkan 'y' untuk ya atau 't' untuk tidak.")
                        break
            else:
                print(f"Customer dengan ID {customer_id} tidak ditemukan.")

                # Simpan perubahan ke file
            with open("customer_data.json", "w") as customer_file:
                json.dump(customer_data, customer_file)
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            input("Tekan Enter untuk mencoba lagi: ")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            break
            
def check_in(daftar_kamar, customer_data):
    while True:
        try:
            os.system("cls")
            tampilkan_daftar_kamar()
            print("+---------------------------------------------------------+")
            print("|                  MENU CHECK IN KAMAR                    |")
            print("+---------------------------------------------------------+")
            no_kamar = int(input("Masukkan nomor kamar yang ingin di-check in: "))
            waktu_inap = int(input("Masukkan lama menginap (dalam hari ): "))

            for kamar in daftar_kamar:
                if kamar["nomor_kamar"] == no_kamar and kamar["status"] == "tersedia":
                    print(f"Kamar {no_kamar} ({kamar['tipe_kamar']}) telah di-check in.")
                    
                    customer_id = int(input("Masukkan ID customer: "))
                    for customer_username, data in customer_data.items():
                        if data["id"] == customer_id:
                            data["kamar_terpesan"] = no_kamar  
                            data["lama_menginap"] = waktu_inap
                            kamar["status"] = "terpesan" 
                            simpan_daftar_kamar()  
                            
                            with open("customer_data.json", "w") as customer_file:
                                json.dump(customer_data, customer_file)
                            return
                    print(f"Customer dengan ID {customer_id} tidak ditemukan.")
                    return
            print(f"Kamar dengan nomor {no_kamar} tidak tersedia atau sudah dipesan.")
            return
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            input("Tekan Enter untuk mencoba lagi: ")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            break
        
def check_out(daftar_kamar, customer_data):
    while True:
        try:
            os.system("cls")
            print("+---------------------------------------------------------+")
            print("|                    MENU CHECK OUT KAMAR                  |")
            print("+---------------------------------------------------------+")
            no_kamar = int(input("Masukkan nomor kamar yang ingin di-check out: "))
            waktu_inap = int(input("Masukkan lama menginap (dalam hari ): "))
            
            for kamar in daftar_kamar:
                if kamar["nomor_kamar"] == no_kamar and kamar["status"] == "terpesan":
                    print(f"Kamar {no_kamar} ({kamar['tipe_kamar']}) telah di-check out.")
                    
                    customer_id = int(input("Masukkan ID customer: "))
                    for customer_username, data in customer_data.items():
                        if data["id"] == customer_id:
                            data["kamar_terpesan"] = no_kamar  
                            data["lama_menginap"] = waktu_inap
                            kamar["status"] = "tersedia" 
                            simpan_daftar_kamar()
                            with open("customer_data.json", "w") as customer_file:
                                json.dump(customer_data, customer_file)
                            print("==========================================================")
                            print("                      INVOICE CHECK OUT                    ")
                            print("==========================================================")
                            print(f"Nama Customer: {customer_username}")
                            print(f"Nomor Kamar: {no_kamar}")
                            print(f"Tipe Kamar: {kamar['tipe_kamar']}")
                            print(f"Harga Kamar per hari: Rp {kamar['harga_kamar']}")
                            print(f"Lama Menginap: {data['lama_menginap']} hari")
                            total_biaya = kamar['harga_kamar'] * data['lama_menginap']
                            print(f"Total Biaya: Rp {total_biaya}")
                            print("==========================================================")
                            
                            konfirmasi = input("Apakah Anda yakin ingin check out? (y/t): ").strip().lower()
                            if konfirmasi == 'y':
                                kamar["status"] = "tersedia"
                                kamar["customer_id"] = None
                                data["kamar_terpesan"] = None
                                data["lama_menginap"] = None
                                data["saldo"] -= total_biaya  
                            
                            # Kurangi saldo customer dengan total biaya
                            
                                print("Check out berhasil. Terima kasih!")
                                simpan_daftar_kamar()
                                with open("customer_data.json", "w") as customer_file:
                                    json.dump(customer_data, customer_file)
                            else:
                                print("Check out dibatalkan.")
                            return
                    print(f"Customer dengan ID {customer_id} tidak ditemukan.")
                    return
            print(f"Kamar dengan nomor {no_kamar} tidak dalam status terpesan.")
            # Simpan perubahan ke file
            with open("customer_data.json", "w") as customer_file:
                json.dump(customer_data, customer_file)
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            input("Tekan Enter untuk mencoba lagi: ")
            continue
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            break
        
# Inisialisasi daftar kamar dari file JSON
try:
    with open("daftar_kamar.json", "r") as kamar_file:
        daftar_kamar_json = json.load(kamar_file)
        daftar_kamar = daftar_kamar_json["kamar"]
except FileNotFoundError:
    daftar_kamar = []

logged_in_as_admin = False
while True:
        try:
            os.system("cls")
            print("#================================================#")
            print("|    <><><><><><><><><><><><><><><><><><><>      |")
            print("|    <>  +----------------------------+  <>      |")
            print("|    <>  |            THE             |  <>      |")
            print("|    <>  |      MANNEQUEEN HOTEL      |  <>      |")
            print("|    <>  +----------------------------+  <>      |")
            print("|    <><><><><><><><><><><><><><><><><><><>      |")
            print("#================================================#")
            print()
            print("#================================================#")
            print("|       SELAMAT DATANG DI MANNEQUEEN HOTEL       |")
            print("|           SILAHKAN PILIH ROLE ANDA             |")
            print("#================================================#")
            print("|[1]. ADMIN HOTEL                                |")
            print("|[2]. CUSTOMER HOTEL                             |")
            print("|[3]. KELUAR                                     |")
            print("#================================================#")

            role = int(input("Masukkan pilihan anda : "))
            if role == 1:
                while True:
                    os.system("cls")
                    print("+--------------------------------+")
                    print("|      SELAMAT DATANG ADMIN      |")
                    print("+--------------------------------+")
                    if not logged_in_as_admin:
                        print("| [1] LOGIN ADMIN                |")
                        print("| [2] BUAT AKUN ADMIN BARU       |")
                        print("+--------------------------------+")

                        pilih_admin = int(input("Masukkan pilihan anda:"))

                        if pilih_admin == 1:
                            os.system("cls")
                            print("+-----------------------------------------+")
                            print("|   SILAHKAN LOGIN ADMIN TERLEBIH DAHULU  |")
                            print("+-----------------------------------------+")

                            kesempatan = 3

                            while kesempatan > 0:
                                admin_username = input("Masukkan nama admin : ")
                                admin_password = pwinput.pwinput(prompt="Masukkan password admin : ")

                                with open("admin_data.json", "r") as admin_file:
                                    admin_data = json.load(admin_file)

                                    if admin_username in admin_data and admin_data[admin_username] == admin_password:
                                        os.system("cls")
                                        print("+---------------------------------------------------------+")
                                        print("|                 ANDA BERHASIL LOGIN                     |")
                                        print("+---------------------------------------------------------+")
                                        logged_in_as_admin = True
                                        break
                                    else:
                                        kesempatan -= 1
                                        if kesempatan > 0:
                                            print(f"Login gagal. Anda memiliki {kesempatan} kesempatan lagi.")
                                        else:
                                            print("Anda telah terkunci. Silakan coba lagi nanti.")
                                            break

                        if pilih_admin == 2:
                            os.system("cls")
                            print("+--------------------------------------+")
                            print("|   SILAHKAN MEMBUAT AKUN ADMIN BARU   |")
                            print("+--------------------------------------+")
                            admin_username = input("Masukkan nama admin baru: ")
                            admin_password = pwinput.pwinput(prompt="Masukkan password admin baru: ")

                            with open("admin_data.json", "r") as admin_file:
                                admin_data = json.load(admin_file)

                            if admin_username not in admin_data:
                                admin_data[admin_username] = admin_password
                                with open("admin_data.json", "w") as admin_file:
                                    json.dump(admin_data, admin_file)
                                print("Akun admin baru telah dibuat.")
                            else:
                                print("Akun admin sudah ada.")
                    # Tampilkan menu admin
                    if logged_in_as_admin:
                        try:
                            while True:
                                print("+---------------------------------------------------------+")
                                print("| [1] MENAMBAH DAFTAR KAMAR                               |")
                                print("| [2] MENAMPILKAN DAFTAR KAMAR                            |")
                                print("| [3] MENGUBAH DAFTAR KAMAR                               |")
                                print("| [4] MENGHAPUS DAFTAR KAMAR                              |")
                                print("| [5] KELUAR                                              |")
                                print("+---------------------------------------------------------+")
                                
                                pilih = int(input("Masukkan pilihan anda : "))
                                if pilih == 1:
                                    tambah_kamar()
                                elif pilih == 2:
                                    tampilkan_daftar_kamar()
                                elif pilih == 3:
                                    ubah_daftar_kamar()
                                elif pilih == 4:
                                    hapus_kamar()
                                elif pilih == 5:
                                    logged_in_as_admin = False
                                    break
                        except KeyboardInterrupt:
                                print(" anda tidak dapat menekan Ctrl+c ")
                                input("Tekan Enter untuk mencoba lagi: ")
                                continue
                        except Exception as e:
                            print(f"Terjadi kesalahan saat penginputan data {e}")
                            input("Tekan Enter untuk mencoba lagi: ")
                            break

            elif role == 2:
                while True:
                        os.system("cls")
                        print("+--------------------------------+")
                        print("|    SELAMAT DATANG CUSTOMER     |")
                        print("+--------------------------------+")
                        print("| [1] LOGIN CUSTOMER             |")
                        print("| [2] BUAT AKUN CUSTOMER BARU    |")
                        print("+--------------------------------+")

                        pilih_customer = int(input("Masukkan pilihan anda :"))

                        if pilih_customer == 1:
                            os.system("cls")
                            print("+------------------------------------------+")
                            print("|  SILAHKAN LOGIN CUSTOMER TERLEBIH DAHULU |")
                            print("+------------------------------------------+")

                            kesempatan = 3

                            while kesempatan > 0:
                                customer_username = input("Masukkan nama customer : ")
                                customer_password = pwinput.pwinput(prompt="Masukkan password : ")

                                with open("customer_data.json", "r") as customer_file:
                                    customer_data = json.load(customer_file)

                                if customer_username in customer_data and customer_data[customer_username]["password"] == customer_password:
                                    os.system("cls")
                                    print("+-----------------------------+")
                                    print("|     ANDA BERHASIL LOGIN     |")
                                    print("+-----------------------------+")
                                while True:
                                    try:
                                        print("+-----------------------------+")
                                        print("| [1] CHECK SALDO             |")
                                        print("| [2] TOP UP SALDO            |")
                                        print("| [3] CHECK IN                |")
                                        print("| [4] CHECK OUT               |")
                                        print("| [5] LOGOUT                  |")
                                        print("+-----------------------------+")

                                        customer_menu = int(input("Masukkan pilihan anda : "))

                                        if customer_menu == 1:
                                            os.system("cls")
                                            print("+-------| CHECK SALDO |-------+")
                                            print(f"Id  : {customer_data[customer_username]['id']}")
                                            print(f"Nama  : {customer_username}")
                                            print(f"Saldo Anda : {customer_data[customer_username]['saldo']}")
                                            print("+-----------------------------+")
                                            with open("customer_data.json", "r") as customer_file:
                                                customer_data = json.load(customer_file)
                                        elif customer_menu == 2:
                                            os.system("cls")
                                            tambah_saldo_customer()
                                        elif customer_menu == 3:
                                            os.system("cls")
                                            check_in(daftar_kamar, customer_data)
                                        elif customer_menu == 4:
                                            os.system("cls")
                                            check_out(daftar_kamar, customer_data)
                                        elif customer_menu == 5:
                                            break
                                    except Exception as e:
                                            print(f"Terjadi kesalahan saat penginputan data {e}")
                                            input("Tekan Enter untuk mencoba lagi: ")
                                            break
                            else:
                                kesempatan -= 1
                                if kesempatan > 0:
                                    print(f"Login gagal. Anda memiliki {kesempatan} kesempatan lagi.")
                                else:
                                    print("Anda telah terkunci. Silakan coba lagi nanti.")
                                    break
                                
                        elif pilih_customer == 2:
                            print("+-------------------------------------------+")
                            print("|    SILAHKAN MEMBUAT AKUN CUSTOMER BARU    |")
                            print("+-------------------------------------------+")
                            customer_username = input("Masukkan nama customer baru: ")
                            customer_password = pwinput.pwinput(prompt="Masukkan password customer baru: ")

                            with open("customer_data.json", "r") as customer_file:
                                customer_data = json.load(customer_file)

                            if customer_username not in customer_data:
                                customer_id = len(customer_data) + 1
                                customer_saldo = 0
                                customer_data[customer_username] = {"password": customer_password, "id": customer_id, "saldo": customer_saldo}
                                with open("customer_data.json", "w") as customer_file:
                                    json.dump(customer_data, customer_file)
                                print("Akun customer baru telah dibuat.")
                                
                            else:
                                print("Username sudah digunakan. Silakan pilih username lain.")

            elif role == 3:
                print("Terima kasih telah menggunakan layanan kami.")
                break
        except KeyboardInterrupt:
            print(" anda tidak dapat menekan Ctrl+c ")
            input("Tekan Enter untuk mencoba lagi: ")
            continue
        
        except Exception as e:
            print(f"Terjadi kesalahan saat penginputan data {e}")
            input("Tekan Enter untuk mencoba lagi: ")
            continue
        