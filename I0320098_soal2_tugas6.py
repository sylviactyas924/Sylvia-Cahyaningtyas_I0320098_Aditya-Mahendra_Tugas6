# menghitung rata-rata nilai
banyakNilai = int(input("Banyaknya nilai yang akan diinput : "))
data = []
n = 1

for n in range(banyakNilai):
    nilai = float(input("nilai ke-{} :".format(n + 1)))
    data.append(float(nilai))
    i = 1 + n
rata = sum(data)/banyakNilai
print("Nilai rata-rata = ", rata)
