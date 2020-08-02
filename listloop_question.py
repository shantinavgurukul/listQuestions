number=[50,40,23,70,56,12,5,10,7]
index=0
count=0
while(index<len(number)):
    if(number[index] >= 20 and number[index] < 40):
        count=count+1
    index=index+1
print(count)

