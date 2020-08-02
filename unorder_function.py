unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]

empty_list=[]
index=0
while(index<len(unorder_list)):
    j=index
    while(j<len(unorder_list)):
        if(unorder_list[index]>unorder_list[j]):
            unorder_list[index],unorder_list[j]=unorder_list[j],unorder_list[index]
        j=j+1
    empty_list.append(unorder_list[index])
    index=index+1
print(empty_list)














