# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# i=0
# value=0
# while(i<len(binary_number)):
#     digit=binary_number.pop()
#     if digit=='1':
#         value=value+pow(2,i)
#         i=i+1
# print("the decimal value of the number=",value)

# b_num = list(input("Input a binary number: "))
# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# value = 0

# for i in range(len(binary_number)):
# 	digit = binary_number.pop()
# 	if digit == '1':
# 		value = value + pow(2, i)
# print("The decimal value of the number is", value)

# binary_number = [1,1,1,0,1,0]
# length = len(binary_number)
# a = 1
# sum=0
# i=0
# while(i<=length):
#     sum= sum+2**i*(binary_number[length-a])
#     i=i+1
#     a = a+1
# print(sum)




binary_number = [1,1,0,1,0]
length = len(binary_number)
a = 1
sum=0
i=0
while(i<=length):
    sum= sum+2**i*(binary_number[length-a])
    i=i+1
    a = a+1
print(sum)










