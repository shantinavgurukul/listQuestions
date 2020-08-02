questions_list=["how many counseling in NG?",
                "what is the capital of india?",
                "how many you have sister?",
                "aap luch me kya khana pasand kroge?"]

option_of_list=[["one","three","six","nine"],
                ["chandigarh","bhopal","chennai","delhi"],
                ["four","five","two","one"],
                ["paneer-roti","saahipaneer","mutton-rice","chiken&chicken karoma"]]
answer_list=[2,3,2,2]
sahigalt_list=[[3,2],[1,3],[2,0],[0,2]]
# check_sahi_galat = [2,2,1,1]
check_sahi_galat = [1,1,0,0]
i=0
lifeline = 0
while(i<len(questions_list)):
    # print("apka question hai?")
    print()
    print("Q.",i+1,questions_list[i])
    j=0
    # print("apka option hai?")
    while (j<len(option_of_list[i])):
        print(j+1,option_of_list[i][j])
        j=j+1
    solution=(input("Enter the answer/lifeline5050:-"))
    if(solution=="lifeline5050"): 
        if (lifeline == 0):
            l = sahigalt_list[i]
            print(option_of_list[i][l[0]])
            print(option_of_list[i][l[1]])  
            check=int(input("enter the answer:-"))
            if(check==(check_sahi_galat[0]+1)):
                print("answer sahi hai")
                lifeline +=1
                
            else:
                print("answer glt hai")
                break
        else:
            print("You allready use your lifeline")
            user=int(input("enter your correct answer:- "))
            d=answer_list[i]
            if(user==(d+1)):
                print("my answer is right")
            else:
                print("oopps! sorry ")
                break
    
    # solution = int(solution)
    
    elif(int(solution)==(answer_list[i]+1)):
        print("my answer is right")
    else:
        print("oopps! sorry your answer is wrong")
        break
        
    i=i+1




# def my_kbc_game(num):
#     if num%2==0:
#         return "even number"
#     else:
#         return "odd number"
# print(my_kbc_game (12))
# print(my_kbc_game(9))
    


