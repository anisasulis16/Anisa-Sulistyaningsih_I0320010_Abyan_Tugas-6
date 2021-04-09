#Program Menghitung nilai rata-rata dgn perintah for atau while
#menginputkan variabel
n = float(input('banyaknya data= '))
jum = 0
i = 1

while i<=n:
    x = float(input('nilai= '))
    print('Data ke-', i, '=', x)
    i += 1
    jum += x
#memproses
rata = jum/n
#menampilkan
print('rata-rata= ', rata)
print('jumlah = ', jum)








