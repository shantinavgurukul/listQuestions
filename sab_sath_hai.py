elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
count=0
count2=0
sum=0
sum2=0
a=0
a2=0
while(index<len(elements)):
    if(elements[index]%2==0):
        count=count+1
        sum=sum+elements[index]
        a=sum//count
    else:
        count2=count2+1
        sum2=sum2+elements[index]
        a2=sum2//count2
    index=index+1
print(count,"even")
print(count2,"odd")
print(count+count2,"total no. of evenodd")
print(sum,"sum of even")
print(sum2,"sum2 of odd ")
print(sum+sum2,"total sum of oddeven")
print(a,"total average of even no.")
print(a2,"total average of odd no.")
print(a+a2,"total average both")

