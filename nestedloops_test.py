# i=0
# while(i<10):
#     j=0
#     while(j<=5):
#         print(j)
#         j=j+1
#     i=i+1


# Output: [[11,19], [12,18],[13,17]]
list_1=[10,11,12,13,15,17,18,19]
num=30
i=0
list_2=[]
while(i<len(list_1)):
    j=i+1
    while(j<len(list_1)):
        if(list_1[i]+list_1[j]==num):
            a=[list_1[i],list_1[j]]
            list_2.append(a)
        j=j+1
    i=i+1
print(list_2)


