n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
# j=0
emptyList=[]
while(i<len(n)):
    # if(n[i]==n[j]and 
    if (n[i]not in emptyList):
    # j=i+1
    # while(j<len(n[i])):Count Occurences
        # if(n[i]==n[j]and n[i]not in emptyList):
        emptyList.append(n[i])
        # j=j+1
    # j=j+1
    i=i+1
print(emptyList)



# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# # j=0
# emptyList=[]
# while(i<len(n)):
    
#     j=0
#     while(j<len(n[i])-1):
#         if( n[i]not in emptyList):
#             emptyList.append(n[i])
#         j=j+1
    
#     i=i+1
# print(emptyList)












