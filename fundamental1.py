# konstruksi dasar python
# sequential : eksekusi berurutan
print('hello world')
print('by teguh')
print('tanggal 23 februari 2021')
print('-' * 10)

# percabangan
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus')
else:
    print('jalan lain')

# Perulangan
jumlah_anak = 4
for index_anak in range(1, jumlah_anak + 1):
    print(f'hai {index_anak}')

#array / data list
anak = ['wildan','zidan']
print(anak)
print(f'hai {anak[1]}')

for a in anak:
    print(f'anak {a}')

for a in range(0,len(anak)):
    print(f'anak {anak[a]}')
