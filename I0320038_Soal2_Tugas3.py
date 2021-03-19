# Membuat dictionary
dict = {'Nama': 'Fadhila Diah', 'Hobi' : ['Membaca novel', 'memasak', 'memancing'], 'Sosial Media' : ['Instagram: fdhladiahapr','Twitter: fdhladiahapr', 'Line: fdhladiahapr'], 'Makanan favorit':['Indomie rebus', 'Indome goreng', 'Popmie']}

# Mengubah hobi
dict['Hobi'][0] = 'Mengaji'

# Mengubah sosial media
dict['Sosial Media'][1] = 'Tiktok: fdhladiahapr'

# Menghapus 2 makanan favorit
del dict ['Makanan favorit'][0:2]

# Menambahkan 1 hobi
dict['Hobi'].append('Bobo')

