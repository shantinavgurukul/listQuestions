my_guess=5
number=10
num=1
while(num<=number):
    user=int(input("enter the number="))
    if(my_guess==user):
        print("sahi guess hai")
        break
    else:
        print("galt guess hai")
    num=num+1