kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
index=0
crorepati=0
lakhapati=0
diwali=0
while(index<len(kitna_paisa_hai)):
    if(kitna_paisa_hai[index]>=10000000):
        crorepati=crorepati+1
        
    elif(kitna_paisa_hai[index]>=100000) :
        lakhapati=lakhapati+1
       
    else:
        diwali=diwali+1
        
        
    index=index+1
print("crorepati=",crorepati)
print("lakhapati=",lakhapati)
print("diwali=",diwali)
