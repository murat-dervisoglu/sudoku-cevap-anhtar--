n= int(input("karenin boyutunu seçin: "))

m=[]
for i in range(0,n):
    m.append([])
    for j in range(0,n):
        m[i].append(0)
i=0    # m = dizi, i = satır numarası, j = sütun numarası, k = kutularda yazan sayı
j=n//2
k=0
while k<n**2:
    k+=1
    m[i][j]=k
    if k%n==0:
        i=i+1
    else:
        i=i-1
        j=j+1
        if i<0:
            i=n-1
        if j==n:
            j=0
for i in m:
    print(i)