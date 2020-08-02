n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
while(count <= n):
  print(sum)
  count=count+1
  a = b
  b = sum
  sum = a + b