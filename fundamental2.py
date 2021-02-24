import requests

kamus = {}
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['ayah'] = 'father'

print(kamus)
print(kamus['istri'])

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(hitung_luas_segitiga(13,2))
print(hitung_luas_segitiga(73,4))

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200 :
        print('sukses')
        print(response.text)
    else:
        print(f'ada kesalahan {response.status_code}')
except Exception as e:
    print('gagal')


