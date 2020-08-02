num=2
number=int (input("enter the number="))
while(number>num):
    if(number%num==0):
        print(number, "not prime number")
        break
    num=num+1
else:
    print(number,"this  is  prime number")
