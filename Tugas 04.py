# -*- coding: utf-8 -*-
"""
Created on Mon Jan 03 18:06:07 2022

@author: Quina
"""

print("\nNama : Quina Majdina Syach")
print("NIM : 064002100033")
print("Program Studi : Teknik Informatika")

import sys 

file_name = str(input("Masukkan nama file: "))

try:
    file = open(f"{file_name}.txt","r")
    print(f"File dengan nama {file_name}.txt ditemukan")
    noun = file.readlines()
    file.close() 
except:
    print(f"File dengan nama {file_name}.txt tidak ditemukan")
    file_name = str(input("Masukkan nama file: "))
    try:
        file = open(f"{file_name}.txt",'r')
        print(f"File dengan nama {file_name}.txt ditemukan")
        noun = file.readlines()
        file.close() 
    except: 
        print(f"File dengan nama {file_name}.txt tidak ditemukan")
        sys.exit()
        noun = file.readlines()
        file.close()   

else:
    name = ['none'] # Name Data
    score = ['none'] # Score Data
    no = 0 # Nomor buat di cetak
    file = open(f"{file_name}.txt","r")
    for i in file:
        cache = str(i)
        cache = cache.split(' ')
        cache = list(cache) # Line Cache in loops
        namec = cache[0] # Name Cache in loops
        scorec = [] # Score Cache in loops
        scorec.append(int(cache[1]))
        scorec.append(int(cache[2]))
        scorec.append(int(cache[3]))
        no += 1 # Nomor yang tadi
        name.append(namec)
        score.append(scorec)  
    file.close()

update =  []

def lihat_semua():
    print("""\n [4. LIHAT SELURUH DATA]\n
    NAMA  |  PRAK 1  |  PRAK 2  |  PRAK3 | RATA-RATA
    -------------------------------------------------""")
    for i in noun:
        noun_list = i.strip().split(' ')
        value1, value2, value3 = noun_list[-3], noun_list[-2], noun_list[-1]
        name = ' '.join(noun_list[0:noun_list.index(value1)])
        average = (int(value1) + int(value2) + int(value3)) / 3
        print(f"\n\t{name} | {value1} | {value2} | {value3} | {average}")
    
def lihat_nilai():
    print("\n\t[1. LIHAT NILAI MAHASISWA]")
    found = str(input("\tMasukkan nama: "))
    no = 0
    for i in name:
        no += 1
        if i == found:
            found = True
            print(f"\tDitemukan! {found} ada di absen ke-{no-1}")
            rata2 = sum(score[no-1])/len(score[no-1])
            print(f"\tNilai: {score[no-1]}\n\tRata rata: {rata2}")
            break
    else:
        no += 1
        if i != found:
            print(f"\tMahasiswa dengan nama {found} tidak ditemukan")
    
def update_nilai():
    print("\n\t[2. UPDATE NILAI MAHASISWA]")
    name = str(input("\tMasukkan nama mahasiswa: "))
    for i in noun:
        noun_list = i.strip().split(' ')
        value1, value2, value3 = noun_list[-3], noun_list[-2], noun_list[-1]
        title = ' '.join(noun_list[0:noun_list.index(value1)])
        if name == title:
            value_to = int(input("\tIngin update nilai praktikum ke-: "))
            new_value = int(input("\tNilai baru: "))
            noun_tempt = [title, int(value1), int(value2), int(value3)]
            old_value = noun_tempt[value_to]
            noun_tempt[value_to] = new_value
            noun[noun.index(i)] = f"{title} {noun_tempt[1]} {noun_tempt[2]} {noun_tempt[3]}"
            print(f"\n\tData berhasil di update dari nilai {old_value} menjadi nilai {new_value}")
            update.append(f"\n\tUpdate nilai praktikum {value_to} {title}, dari nilai {old_value} menjadi {new_value}")
            break
    else:
        noun_list = i.strip().split(' ')
        value1, value2, value3 = noun_list[-3], noun_list[-2], noun_list[-1]
        title = ' '.join(noun_list[0:noun_list.index(value1)])
        if name != title:
            print(f"\tNama mahasiswa {name} tidak ditemukan")
            
def hapus_data():
    print ("\n\t[3. Hapus Data]")
    name = input("\tMasukkan nama mahasiswa yang datanya ingin dihapus: ")
    for i in noun:
        noun_list = i.strip().split(' ')
        title = ' '.join(noun_list[0:noun_list.index(noun_list[-3])])
        if name == title:
            noun.pop(noun.index(i))
            print(f"\n\tData dengan nama {name} telah dihapus")
            update.append(f"\n\tData milik {name} dihapus")
            break
    else:
        noun_list = i.strip().split(' ')
        title = ' '.join(noun_list[0:noun_list.index(noun_list[-3])])
        if name != title:
            print(f"\n\tTidak ada nama mahasiswa {name} di file") 
            
def simpan_ke_file():
    print("\n\t[5. SIMPAN UPDATE NILAI]")
    file = open(f'{file_name}.txt','w')
    file.write(''.join(noun))
    file.close()
    for x in update:
        print(x)
    print(f'\n\tFILE {file_name}.txt BERHASIL DISIMPAN')
update = []
        
while True:
    print(f"""

--------------[Menu]-------------
| 1. Lihat Nilai
| 2. Update Nilai
| 3. Hapus Data
| 4. Lihat Semua
| 5. Simpan ke file
| 6. Keluar
________________________________ """)

    pilih = str(input('Pilih: '))
    
    if pilih == '1':
        lihat_nilai()
    elif pilih == '2':
        update_nilai()
    elif pilih == '3':
        hapus_data()
    elif pilih == '4':
        lihat_semua()
    elif pilih == '5':
        simpan_ke_file()
    elif pilih == '6':
        print("\n\t[6. KELUAR] ")
        print("\n\tTERIMAKASIH TELAH BERKUNJUNG")
        sys.exit()
    else:
        print("\n\t[INVALID INPUT]")
        print("\n\tSILAHKAN MASUKKAN MENU 1-6")