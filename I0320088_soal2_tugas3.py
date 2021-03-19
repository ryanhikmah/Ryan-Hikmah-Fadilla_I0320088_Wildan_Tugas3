dict1 = {'Nama': 'Ryan Hikmah Fadilla',
         'Hobi': ['Membaca', 'Bersepeda', 'Sepak Bola'],
         'Sosial Media': {'Instagram' : 'ryanhikmah', 'Facebook' : 'ryanhf', 'ID line' : 'ryanhf123'},
         'Lagu Kesukaan': ['Here With Me','Happier','Without Me'],
         'Makanan Favorit': ['Nasi Goreng','Mie Goreng','Rendang']}

#Mengubah 1 hobi dan 1 sosial media
dict1['Hobi'][0] = 'Main Game'
dict1['Sosial Media']['Facebook'] = 'ryanfadell'

#Menghapus 2 makanan favorit
del dict1['Makanan Favorit'][0]
del dict1['Makanan Favorit'][1]

#Menambah 1 Hobi
dict1['Hobi'].append('Mendengarkan Lagu')
print(dict1)


