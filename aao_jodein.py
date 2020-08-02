elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
esum1=0
osum2=0
index=0
while(index<len(elements)):
    if(elements[index]%2==0):
        esum1=esum1+elements[index]
    else:
        osum2=osum2+elements[index]
    index=index+1
print(esum1)
print(osum2)