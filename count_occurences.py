# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# a=0
# n=0
# t=0
# x=0
# u=0
# g=0
# i=0
# while(i<len(char_list)):
#     if(char_list[i]=="a"):
#         a=a+1
#     elif(char_list[i]=="n"):
#         n=n+1
#     elif(char_list[i]=="t"):
#         t=t+1
#     elif(char_list[i]=="x"):
#         x=x+1
#     elif(char_list[i]=="u"):
#         u=u+1
#     else:
#         g=g+1
#     i=i+1
# print("a is=",a,"n is=",n,"t is=",t,"x is=",x,"u is=",u,"g is=",g)


char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# emptyList=[ ]
# while(i<len(char_list)):
#     j=0
#     c=0
#     while(j<len(char_list)):
#         if(char_list[i]==char_list[j]):
#             c=c+1
#             # print(char_list[i],c)
#             # emptyList.append(char_list[i],c)
            
#         j=j+1
#     print(char_list[i],c)
#     i=i+1



# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i = 0
# a = [ ]
# b = [[] ]
# while i<len(char_list):
#     j = 0
#     count = 0
#     while j<len(char_list):
#         if char_list[i] == char_list[j]:
#             count = count + 1
#             b = char_list[i],count
#             a.append(b)
#         j = j + 1
#     print(b,"times",end="")
#     i = i + 1


# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i = 0
# a = [ ]
# b = [ ]
# while i<len(char_list):
#     j = 0
#     count = 0
#     while j<len(char_list):
#         if char_list[i] == char_list[j]:
#             count = count + 1
#             b = char_list[i],count
#             a.append(b)
#         j = j + 1
#     print()
#     print(b,"times")
#     i = i + 1

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i = 0
a = [ ]
while(i<len(char_list)):
    if char_list[i] not in a:
        a.append(char_list[i])
    i=i+1
print(a)

j=0
p=[ ]
while(j<len(a)):
    k=0
    count=0
    d=[ ]
    while(k<len(char_list)):
        if(a[j]==char_list[k]):
            count=count+1
        k=k+1
    d.append(a[j])
    d.append(count)
    p.append(d)
    print(a[j],"=",count,"times")
    j=j+1
print(p)

            
            
            
































