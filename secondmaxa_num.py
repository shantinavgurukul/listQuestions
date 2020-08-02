num=[50,40,23,70,56,12,5,10,7]
maxa=max(num[0],num[1])
seconmdmaxa=min(num[0],num[1])
i=0
while(i<len(num)):
    if(num[i]>maxa):
        seconmdmaxa=maxa
        maxa=num[i]
    else:
        if(num[i]>seconmdmaxa):
            seconmdmaxa=num[i]
    i=i+1
print("secondmaxa number is"+"= ",(seconmdmaxa))