from prettytable import PrettyTable

dict_kamar = [
    {'Kode':'GAR001', 
     'Tipe Kamar':'Standart',       
     'Jenis Kasur':'Single Bed',         
     'Service': 'Tanpa Breakfast',    
     'Status Kamar': 'Kosong',    
     'Harga': 1250000},

    {'Kode':'GAR002', 
     'Tipe Kamar':'Standart',       
     'Jenis Kasur':'Twin Bed',           
     'Service': 'Tanpa Breakfast',    
     'Status Kamar': 'Tersedia',  
     'Harga': 1250000},

    {'Kode':'GAR003', 
     'Tipe Kamar':'Standart',       
     'Jenis Kasur':'Single Bed',         
     'Service': 'Tanpa Breakfast',    
     'Status Kamar': 'Tersedia',  
     'Harga': 1250000},

    {'Kode':'GAR004', 
     'Tipe Kamar':'Deluxe',         
     'Jenis Kasur':'Single Bed',         
     'Service': 'Termasuk Breakfast', 
     'Status Kamar': 'Kosong',    
     'Harga': 1750000},

    {'Kode':'GAR005', 
     'Tipe Kamar':'Suite',          
     'Jenis Kasur':'Queen Size Bed',     
     'Service': 'Termasuk Breakfast', 
     'Status Kamar': 'Tersedia',  
     'Harga': 2300000},

    {'Kode':'GAR006', 
     'Tipe Kamar':'Deluxe',         
     'Jenis Kasur':'Twin Bed',           
     'Service': 'Termasuk Breakfast', 
     'Status Kamar': 'Tersedia',  
     'Harga': 1800000},

    {'Kode':'GAR007', 
     'Tipe Kamar':'Suite',          
     'Jenis Kasur':'King Size Bed',      
     'Service': 'Termasuk Breakfast', 
     'Status Kamar': 'Kosong',    
     'Harga': 2500000},

    {'Kode':'GAR008', 
     'Tipe Kamar':'Standart',       
     'Jenis Kasur':'Single Bed',         
     'Service': 'Tanpa Breakfast',    
     'Status Kamar': 'Tersedia',  
     'Harga': 1250000},

    {'Kode':'GAR009', 
     'Tipe Kamar':'Standart',       
     'Jenis Kasur':'Twin Bed',           
     'Service': 'Tanpa Breakfast',    
     'Status Kamar': 'Kosong',    
     'Harga': 1250000},
     
    {'Kode':'GAR010', 
     'Tipe Kamar':'Deluxe',         
     'Jenis Kasur':'Twin Bed',           
     'Service': 'Termasuk Breakfast', 
     'Status Kamar': 'Kosong',    
     'Harga': 1800000}
]

def header(menu='mainmenu'):
    print(60*'\n')
    print(42*'==')
    if menu == 'create':
        print(f'ADD DATA GRIYA ALSIS RESIDENCE 🏡'.center(82))
    elif menu == 'read':
        print(f'READ DATA GRIYA ALSIS RESIDENCE 🏡'.center(82))
    elif menu == 'update':
        print(f'UPDATE DATA GRIYA ALSIS RESIDENCE 🏡'.center(82))
    elif menu == 'delete':
        print(f'DELETE DATA GRIYA ALSIS RESIDENCE 🏡'.center(82))
    elif menu == 'booking':
        print(f'BOOK ROOM GRIYA ALSIS RESIDENCE 🏡'.center(82))
    else:
        print(f'GRIYA ALSIS RESIDENCE ADMINISTRATION 🏡'.center(82))

    print(42*'==')

def datakamar():
    header()
    kolomtable = PrettyTable()
    kolomtable.field_names =dict_kamar[0].keys()
    for row in dict_kamar:
        kolomtable.add_row(row.values())

    print(kolomtable) 

def menu_utama():
 while True:
    header('mainMenu')
    MenuInput=input('''               
        List Menu:
                    
            1. Menampilkan Data Kamar Griya Alsis Residence
            2. Menambah Data Kamar Griya Alsis Residence
            3. Mengedit Data Kamar Griya Alsis Residence  
            4. Menghapus Data Kamar Griya Alsis Residence                    
            5. Keluar Program
                            
            Masukkan angka Menu yang ingin dijalankan : ''')
    if MenuInput == '1':
        menampilkan_data_kamar()
    elif MenuInput == '2':
        menambah_data_kamar()
    elif MenuInput == '3':
        mengupdate_data_kamar()
    elif MenuInput == '4':
        menghapus_data_kamar()
    elif MenuInput == '5':
        keluar_program()    
    else:
        print('Pilihan menu tidak ada!')
        input('Tekan Enter..')

def menampilkan_data_kamar():
    while True:
        header('read')
        print('''
        List Menu:
              
            1. Lihat semua data kamar Griya Alsis Residence
            2. Lihat data kamar berdasarkan kode
            3. Keluar ''')
        
        opsimenampilkan =input('Masukkan menu yang ingin dijalankan: ')

        if opsimenampilkan=='1':
         while True:
            option=input('Tampilkan semua data? (Ya/Tidak): ').capitalize() 
            if option=='Ya':
                datakamar()
                input('Tekan Enter..')
                break
            elif option=='Tidak':
                 print('Data tidak ditampilkan!')
                 input('Tekan Enter..')
                 break
            else:
                print('Input tidak valid masukkan Ya/Tidak!')
            

        elif opsimenampilkan=='2':
             kode_kamar=input('Masukkan kode kamar harus diawali 3 huruf "GAR" dan 3 angka belakang! (contoh: GAR001) : ')
             if kode_kamar[:3] == 'GAR' and kode_kamar[3:].isdigit and len(kode_kamar) ==6:
                kode = False
                for data in dict_kamar:
                    if data['Kode'] == kode_kamar:
                       show = PrettyTable()
                       show.field_names = data.keys()
                       show.add_row(data.values())
                       kode = True
                       print('Berikut data kamar yang ada: ')
                       print(show)
                       input('Tekan Enter..')
                       break

                if not kode:
                 print('Kode kamar tidak ditemukan! ')
                 input('Tekan Enter..')                
             else:
              print('Format kode kamar tidak sesuai!, diawali 3 huruf "GAR" dan 3 angka belakang! (contoh: GAR001) ')
              input('Tekan Enter..')
                
        elif opsimenampilkan=='3':
            menu_utama()
        else:
         print('Pilihan menu tidak ada! ')
         input('Tekan Enter..')
          
def menambah_data_kamar():
    while True:
        header('create')
        print('''
              List Menu:
                  1. Buat data kamar baru
                  2. Keluar
        ''')
        opsimenambah=input('Masukkan angka yang ingin dijalankan: ')

        if opsimenambah=='1':
             
            kodekamar=input('Masukkan kode kamar, format kode "GAR" dan 3 angka belakang (contoh: GAR001): ')

            if not kodekamar[:3] == 'GAR' or not kodekamar[3:].isdigit or len(kodekamar) !=6:
                 print('Kode yang dimasukkan tidak sesuai, format kode diawali 3 huruf "GAR" dan 3 angka belakang (contoh: GAR001) ')
                 input('Tekan Enter..')
                 continue
            kode= False
            for data_table in dict_kamar:
                 if data_table['Kode'] == kodekamar:
                     kode = True
                     break
                 
            if kode:
                 print('Data dengan kode kamar tersebut sudah ada.')
                 input('Tekan Enter..')
                 continue
            
            while True:
                tipekamar=input("Masukkan tipe kamar yang baru 'Standart, Deluxe, Suite': ").title().strip()
                if tipekamar in['Standart','Deluxe','Suite']:
                    break
                print('Masukkan tipe kamar "Standart,Deluxe,Suite"' )
            while True:
                jeniskasur=input('''Masukkan jenis kasur pada kamar "Single Bed,Twin Bed, Queen Size Bed,King Size Bed": ''').title().strip()
                if jeniskasur in['Single Bed','Twin Bed','Queen Size Bed','King Size Bed']:
                    break
                print('''Masukkan jenis kasur "Single Bed, Twin Bed, Queen Size Bed, King Size Bed" ''')
            while True:
                service=input('Masukkan layanan kamar (Tanpa Breakfast/Termasuk Breakfast): ').title()
                if service in ['Tanpa Breakfast','Termasuk Breakfast']:
                    break
                print('Masukkan layanan dengan "Termasuk Breakfast / Tanpa Breakfast" ')  
            while True:
                statuskamar=input('Masukkan status kamar: ').capitalize()
                if statuskamar:
                    break
                print('Data harus diisi!' )
            while True:        
                hargakamar=input('Masukkan harga Kamar: ')
                if hargakamar.isdigit():
                    break
                print('Harga kamar harus berupa angka dan harus bilangan bulat!')
                    
            while True:
                save = input("Apakah ingin menyimpan data? (Ya / Tidak): ").capitalize()
                if save=='Ya':
                    dict_kamar.append({'Kode':kodekamar ,'Tipe Kamar' : tipekamar, 'Jenis Kasur': jeniskasur, 'Service': service, 'Status Kamar' : statuskamar, 'Harga Kamar' : hargakamar })
                    print('Data kamar tersimpan ✅ ')
                    input('Tekan Enter..')
                    break
                elif save=='Tidak':
                    print('Data tidak jadi ditambahkan ✅ ')
                    break
                else:
                    print('Data yang dimasukkan tidak valid!, silahkan masukkan "Ya / Tidak" ')
            
        elif opsimenambah=='2':
            menu_utama()
        else:
            print('Pilihan menu tidak ada!')
            input('Tekan Enter..')
                 
def mengupdate_data_kamar():
    while True:
        header('update')
        print('''
              List Menu:
                  1. Edit data kamar Griya Alsis Residence
                  2. Keluar
        ''')
        opsimengupdate=input('Masukkan angka yang ingin dijalankan: ')

        if opsimengupdate=='1':
            primerkey = input('Masukkan kode kamar yang ingin diperbarui,format "GAR" dan tiga angka dibelakang (contoh: GAR001):')
            if not primerkey[:3] == 'GAR' and not primerkey[3:].isdigit() or len(primerkey) != 6:
                print('Kode yang dimasukkan tidak sesuai, format kode "GAR" dan tiga angka dibelakang (contoh: GAR001)')
                input('Tekan Enter..')
                continue    
            kode = False
            for data_tabel in range(len(dict_kamar)):
                if primerkey in dict_kamar[data_tabel].values():  
                    kode = True
                    print('Data kamar yang akan diubah: ')
                    update_table = PrettyTable()
                    update_table.field_names = dict_kamar[data_tabel].keys()  
                    update_table.add_row(dict_kamar[data_tabel].values())  
                    print(update_table)
                    break
            if not kode:
             print('Data dengan kode kamar tersebut tidak ditemukan! ')
             input('Tekan Enter..')
             continue
                  
            update = input('Apakah data ingin diperbarui (Ya/Tidak)? ').strip().capitalize()
            if update == 'Ya':
                kolom=input('Masukkan nama kolom yang ingin diedit: ').title()
                if kolom=='Tipe Kamar':
                 while True:
                    ValueEdit=input(f'Masukkan {kolom} yang baru "Standart, Deluxe, Suite": ').title().strip()
                    if ValueEdit in ['Standart','Deluxe','Suite']:
                        break
                    print('Masukkan tipe kamar "Standart, Deluxe, Suite"!')
                 while True:
                    confirmation=input(f'Ganti {kolom} menjadi "{ValueEdit}" (Ya/Tidak)?: ').capitalize()
                    if confirmation=='Ya':
                        dict_kamar[data_tabel][kolom]=ValueEdit
                        confirmation == ValueEdit
                        print(f'Data {kolom} berhasil di edit ✅')
                        input('Tekan Enter..')
                        mengupdate_data_kamar()
                    elif confirmation=='Tidak':
                        print('Data tidak jadi disimpan!')
                        input('Tekan Enter..')
                        mengupdate_data_kamar()
                    else:
                        print('Input tidak valid masukkan "Ya / Tidak" ')
                                    
                elif kolom=='Jenis Kasur':
                 while True:
                    ValueEdit=input(f'Masukkan {kolom} yang baru "Single Bed, Twin Bed, Queen Size Bed, King Size Bed": ').title().strip()
                    if ValueEdit in ['Single Bed','Twin Bed','Queen Size Bed','King Size  Bed']:
                        break
                    print(f'Masukkan jenis kasur yang ada "Single Bed, Twin Bed, Queen Size Bed, King Size Bed"! ') 
                 while True:       
                    confirmation=input(f'Ganti {kolom} menjadi "{ValueEdit}" (Ya/Tidak)?: ').capitalize()
                    if confirmation=='Ya':
                        dict_kamar[data_tabel][kolom]=ValueEdit
                        confirmation == ValueEdit
                        print(f'Data {kolom} berhasil di edit ✅')
                        input('Tekan Enter..')
                        mengupdate_data_kamar()
                    elif confirmation=='Tidak':
                        print('Data tidak jadi disimpan!')
                        input('Tekan Enter..')
                        mengupdate_data_kamar()
                    else:
                        print('Input tidak valid masukkan "Ya / Tidak" ')
                        input('Tekan Enter..')
                        
                elif kolom=='Service':
                 while True:
                    ValueEdit=input(f'Masukkan {kolom} yang baru termasuk breakfast / tanpa breakfast: ').title()
                    if ValueEdit in ['Termasuk Breakfast', 'Tanpa Breakfast']:
                        break  # Keluar dari loop jika input benar
                    print('Input tidak valid! Masukkan "Termasuk Breakfast" atau "Tanpa Breakfast".')
                 while True:
                    confirmation=input(f'Ganti {kolom} menjadi "{ValueEdit}" (ya/tidak)?: ').lower()
                    if confirmation=='ya':
                        dict_kamar[data_tabel][kolom]=ValueEdit
                        confirmation == ValueEdit
                        print(f'Data {kolom} berhasil di edit ✅')
                        input('Tekan Enter..')
                        mengupdate_data_kamar()
                    elif confirmation=='tidak':
                        print('Data tidak jadi disimpan!')
                        input('Tekan Enter..')
                        mengupdate_data_kamar()
                    else:
                        print('Input tidak valid masukkan "ya / tidak" ')
                        input('Tekan Enter..') 

                elif kolom=='Status Kamar':
                    while True:
                        ValueEdit=input(f'Masukkan {kolom} yang baru: ').capitalize().strip()
                        if ValueEdit:
                            break
                        print('Data harus diisi!')
                    while True:
                        confirmation=input(f'Ganti {kolom} menjadi "{ValueEdit}" (ya/tidak)?: ').lower()
                        if confirmation=='ya':
                            dict_kamar[data_tabel][kolom]=ValueEdit
                            confirmation == ValueEdit
                            print(f'Data {kolom} berhasil di edit ✅')
                            input('Tekan Enter..')
                            mengupdate_data_kamar()
                        elif confirmation=='tidak':
                            print('Data tidak jadi disimpan!') 
                            input('Tekan Enter..')
                            mengupdate_data_kamar()
                        else:
                            print('Input tidak valid masukkan "ya / tidak" ')
                            input('Tekan Enter..')

                elif kolom=='Harga':
                    while True:
                        ValueEdit=input(f'Masukkan {kolom} kamar yang baru: ')
                        if ValueEdit.isdigit():
                            break
                        print('Harga harus angka dan bilangan bulat! ')
                    while True:        
                        confirmation=input(f'Ganti {kolom} menjadi "{ValueEdit}" (ya/tidak)?: ').lower()
                        if confirmation=='ya':
                            dict_kamar[data_tabel][kolom]=ValueEdit
                            confirmation == ValueEdit
                            print(f'Data {kolom} berhasil di edit ✅')
                            input('Tekan Enter..')
                            mengupdate_data_kamar()
                        elif confirmation=='tidak':
                            print('Data tidak jadi disimpan!')
                            input('Tekan Enter..')
                            mengupdate_data_kamar()
                        else:
                            print('Input tidak valid masukkan "ya / tidak" ')
                            input('Tekan Enter..')

                elif kolom=='Kode':
                    print(f'Kolom {kolom} tidak dapat diubah! ') # kolom kode merupakan Identifier dari setiap values dan tidak bisa diubah
                    input('Tekan Enter..') 
                else:
                 print('Masukkan nama kolom yang benar! ')
                 input('Tekan Enter..')

            elif update == 'tidak':
                print('Edit data dibatalkan!')
                input('Tekan Enter..')
            else:
                print('Input tidak valid masukkan "ya / tidak", silahkan coba lagi.. ')
                input('Tekan Enter..')  

        elif opsimengupdate=='2':
         menu_utama()
        else:
         print('Pilihan menu tidak ada!')
         input('Tekan Enter..')
    
def menghapus_data_kamar():
    header('delete')
    while True:
        header('delete')   
        print('''
              List Menu:
                  1. Hapus data kamar Griya Alsis Residence
                  2. Restore data yang di hapus
                  3. Keluar
        ''')
        opsihapus = input('Masukkan angka menu yang ingin dijalankan: ')

        if opsihapus=='1':

            primerkey = input('Masukkan kode kamar yang ingin dihapus, format kode "GAR" dan tiga angka dibelakang (contoh: GAR001): ')
            if not primerkey[:3] == 'GAR' or not primerkey[3:].isdigit() or len(primerkey) != 6:
                print('Kode yang dimasukkan tidak sesuai, format kode "GAR" dan tiga angka dibelakang (contoh: GAR001)')
                input('Tekan Enter..')
                continue
                
            kode = False
            for i in range(len(dict_kamar)):
                if primerkey in dict_kamar[i].values():  
                    kode = True
                    print('Data kamar yang akan dihapus: ')
                    hapus_table = PrettyTable()
                    hapus_table.field_names = dict_kamar[i].keys()  
                    hapus_table.add_row(dict_kamar[i].values())  
                    print(hapus_table)
                    break
            if not kode:
                print('Kode kamar tidak ditemukan!')
                input('Tekan Enter..')
                menghapus_data_kamar()

            while True:
                delete = input('Apakah data kamar ini ingin dihapus (Ya/Tidak)? ').capitalize()
                
                if delete =='Ya':
                    data_terhapus.append(dict_kamar[i])
                    del dict_kamar[i]
                    print('Data kamar berhasil dihapus! ')
                    input('Tekan Enter..')
                    menghapus_data_kamar()
                elif delete == 'Tidak':
                    print('Data kamar batal dihapus! ')
                    input('Tekan Enter..')
                    menghapus_data_kamar()
                    break
                else:
                 print('Input tidak valid, masukkan "Ya" / "Tidak" ')
        
        elif opsihapus=='2':
            restore_data()
            
        elif opsihapus =='3':
             menu_utama()
        else:
         print('Pilihan menu tidak ada!')
         input('Tekan Enter..')

def restore_data():
    # print(data_terhapus)
    if not data_terhapus:
        print("\nTidak ada data yang dapat direstore.\n")
        input('Tekan Enter..')
        return

    print("\n=== Data yang dapat direstore ===")
    table = PrettyTable()
    table.field_names = data_terhapus[0].keys()  
    for data in data_terhapus:
        table.add_row(data.values())  
    print(table)

    kode_kamar = input('Masukkan kode kamar yang ingin direstore: ').strip().lower()

    data_lama = None
    for item in data_terhapus:
        if item['Kode'].lower() == kode_kamar: 
            data_lama = item
            break

    if data_lama:
        dict_kamar.append(data_lama)
        data_terhapus.remove(data_lama)
        print(f"\nData kamar dengan kode '{kode_kamar.upper()}' berhasil direstore.\n")
        input('Tekan Enter..')
    else:
        print("Slahkan isi kode kamar dengan benar!")
        input('Tekan Entar..')
    
def keluar_program():
     exit_confirmation=input('Masukkan "ya" untuk keluar dari program ini:  ').lower().strip()
     if exit_confirmation=='ya':
        print(60*'\n')
        print(40*'==')
        print(f"{'Terima kasih salam hangat kami':^72}")
        print(f"{'GRIYA ALSIS RESIDENCE 🏡':^72}")
        print(40*'==')
        exit()
     else:
         print('''Masukkan "ya", jika ingin keluar dari program. ''')
         input('Tekan Enter..')

data_terhapus=[]          
menu_utama() # Panggil Menu Utama