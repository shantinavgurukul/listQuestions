number=[50,40,23,70,56,12,5,10,7]
index=0
maxa=number[0]
while(index < len(number)):
    if(number[index] > maxa):
        maxa=number[index]
    index=index+1
print("maximum number is"+"=",(maxa))