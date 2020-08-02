# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index=0
# # average=0
# list1=[]
# list2=[]
# while(index<len(elements)):
#     if(elements[index]%2!=0):
#         list1.append(elements[index])
#         # list1=list1+1
#         average=elements[index]//7
#     else:
#         list2.append(elements[index])
#         # list2=list2+1
#         average=elements[index]//4
        
#     index=index+1
# print("even number is:",list1)
# print(average)
# print("odd number is:",list2)
# print(average)



elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even=0
# odd=0
# esum1=0
# osum2=0
# index=0
# while index<len(elements):
#     if elements[index]%2==0:
#         even=even+1
        
#         esum1=esum1+elements[index]
    
#     else:
#         odd=odd+1
        
#         osum2=osum2+elements[index]
    
#     index=index+1
# avarge1=esum1/even
# avarge2=osum2/odd
# print(esum1)
# print(osum2)
# print(even) 
# print(odd) 
# print(avarge1) 
# print(avarge2)         

index=0
evensum=0
oddsum=0
evencount=0
oddcount=0
while(index<len(elements)):
    if(elements[index]%2==0):
        evensum=evensum+elements[index]
        evencount=evencount+1
    else:
        oddsum=oddsum+elements[index]
        oddcount=oddcount+1
    index=index+1
evenAverage=evensum//evencount
oddAverage=oddsum//oddcount
print(evensum)
print(oddsum)
print(evenAverage)
print(oddAverage)



















