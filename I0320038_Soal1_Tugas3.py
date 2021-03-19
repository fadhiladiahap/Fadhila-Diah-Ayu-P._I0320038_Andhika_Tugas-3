#List 10 teman
nama_teman = ['Memed', 'Attar', 'Bagus', 'Erysa', 'Efa', 'Alip', 'Dhea', 'Gea', 'Rio', 'Alvin']

#Menampilkan list indeks pada nomor 4,6,dan 7
print("Nama teman pada list indeks nomor 4,6, dan 7 yaitu", nama_teman[4], ",", nama_teman[6], ", dan", nama_teman[7])

#Mengganti nama teman di list 3,5, dan 9
nama_teman[3] = ('Neta')
nama_teman[5] = ('Febe')
nama_teman[9] = ('David')

#Menambahkan 2 nama teman
nama_teman.append('Mahes')
nama_teman.append('Indra')

#Menampilkan nama teman dengan pengulangan
for pengulangan in nama_teman :
    print(pengulangan)

# Menampilkan panjang list
print(len(nama_teman))