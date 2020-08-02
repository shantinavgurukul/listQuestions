held=int(input("enter the class held="))
attended=int(input("enter the class attended="))
parecentage=(attended/held)*100
if(parecentage>=75):
    print("you are allowed to sit in exam")
else:
    print("you are not allowed to sit in exam because your attendece is less")

