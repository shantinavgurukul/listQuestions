guess_num=5
num=1
while(num<=10):
    user=int(input("enter the number="))
    if(guess_num==user):
        print("barbara hai")
        break
    elif(guess_num<=user):
        print("bada hai ")
    else:
        print("chhota hai")
    num=num+1