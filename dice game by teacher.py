import random

a=int(input("Enter the number of Players:"))
player=[]

y={}

z=0

while a !=0:
    b=input("Player Name:")
    player.append(b)
    a-=1



for x in player:
    c=int(input("\nPress 1 to roll dice:"))

    a=random.randint(1,6)
    b=random.randint(1,6)
    c=a+b
    
    y[player[z]]=c
    print(player[z],":",a,":",b)
    z+=1

print('\n',y)    
    