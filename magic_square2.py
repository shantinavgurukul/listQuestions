magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sum=0
while(i<len(magic_square)):
    j=0
    while(j<len(magic_square[i])):
        if(i==j):
            sum=sum+magic_square[i][j]
            if(i+j==len(magic_square)):
                sum=sum+magic_square[i][j]
        j=j+1
    i=i+1
print(sum)












# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# i=0
# sum=0
# while(i<len(magic_square)):
#     j=0
#     while(j<len(magic_square[i])):
#         if(i==j):
#             sum=sum+magic_square[j][i]
#             print(magic_square[j][i],"shanti")
            
#             if(i+j==len(magic_square)):
#                 sum=sum+magic_square[j][i]
                
#         j=j+1
#     i=i+1
# print(sum)
    

magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while(i<len(magic_square)):
    j=0
    sum=0
    while(j<len(magic_square[i])):
        sum=sum+magic_square[i][j]+len(magic_square)
        print(magic_square[i][j],"shanti")
        j=j+1
    if(sum==sum):
        print("its magic")
    else:
        print("its not magic")
    i=i+1
print(sum)

        










