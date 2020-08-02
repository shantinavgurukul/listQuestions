n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
def duplicate_naam(n):
    # n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
    i=0
    empltyList=[]
    while(i<len(n)):
        if(n[i]not in empltyList):
            empltyList.append(n[i])
        i=i+1
    print(empltyList)
list2=n
duplicate_naam([19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11])
duplicate_naam(list2)