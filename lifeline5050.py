questions_list=["how many counseling in NG?",
                "what is the capita of india?",
                "how many you have sister?",
                "aap luch me kya khana pasand kroge?"]

option_of_list=[["one","three","six","nine"],
                ["chandigarh","bhopal","chennai","delhi"],
                ["four","five","two","one"],
                ["paneer-roti","saahipaneer","mutton-rice","chiken&chicken karoma"]]
# 5050=[5050]
answer_list=[2,3,2,2]
sahigalt_list=[[3,2],[1,3],[2,0],[0,2]]
check_sahi_galat = [2,2,1,1]
i=0
while(i<len(questions_list)):
    print("apka question hai?")
    print("")
    print(questions_list[i])
    j=0
    print("apka option hai?")
    while (j<len(option_of_list[i])):
        print(j+1,option_of_list[i][j])
        j=j+1
    solution=input("Enter the answer/lifeline5050:-")
    if(solution=="lifeline5050"):
        l = sahigalt_list[i]
        print(option_of_list[i][l[0]])
        print(option_of_list[i][l[1]])  
        check=int(input("enter the answer:-"))
        if(check==check_sahi_galat[0]):
            print("answer sahi hai")
        
        else:
            print("answer glt hai")
            break
                    
     
    if((solution)==answer_list[i]):
        print("my answer is right")
    # else:
    #     print("oopps! sorry your answer is wrong")
    #     break
        
    i=i+1