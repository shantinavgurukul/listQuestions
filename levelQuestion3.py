quantity=int(input("enter the quantity="))
if(quantity*100>1000):
    print("total cost is=",(quantity*100)-(0.1*quantity*100))
else:
    print("cost is=",quantity*100)