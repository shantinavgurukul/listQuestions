# kitne odd numbers hai aur kitne
# even numbers hai.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
counteven=0
countodd=0
while(index<len(elements)):
    if(elements[index]%2==0):
        counteven=counteven+1
        
    else:
        countodd=countodd+1
        
    index=index+1
print(counteven)
print(countodd)
