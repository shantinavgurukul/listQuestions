a=[-2,0,-9,11,45]
b=[]
i=0
while i<len(a):
    j=i
    while j<len(a):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    b.append(a[i])
    i+=1
print(b)