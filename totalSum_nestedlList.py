# Output: [[11,19], [12,18],[13,17]]
n = [10, 11, 12, 13, 14, 17, 18, 19]
number = 30
index=0
new_list=[]
while(index<len(n)):
    j=index+1
    while(j<len(n)):
        if(n[index]+n[j]==number):
            a=[n[index],n[j]]
            new_list.append(a)
        j=j+1
    index=index+1
print(new_list)


