number=int(input("enter the number="))
if(number==8):
    print("ok")
elif(number<8):
    
    num=int(input((("please give me again input",8-number))))
    print("good")
elif(number>8):
    print("please shift" , number-8 , "to other room")