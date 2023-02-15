import random
#player_dict={}
player_list=[]
players=int(input("WELCOME TO CHABLESZ BILLION DICE GAME;\nEnter the number of the available players:"))


while players>=1:
    name=input("Enter the name of the players:")
    player_list.append(name)


    players-=1
b=players
#print(player_list:)
for a in player_list:
    first=random.randint(1,7)
    second=random.randint(1,7)
    c=int(input("press 1 to roll dice:"))
    if c==1:
        print(player_list[b], ':', first, "computer",":",second)
        #if first> second:
        #   print("")
    b+=1    

