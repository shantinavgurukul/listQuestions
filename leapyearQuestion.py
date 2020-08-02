year=int (input("enter the year="))
if(year%4==0 and year%100!=0):
    print(year,"it's leap year.")
elif(year%400==0):
    print(year,"it's   leap year-")
else:
    print(year, "it's not leap year")