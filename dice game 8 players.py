import random

min=1
max=4
name=[]
print("WELCOME TO CHABLESZ FIVE BILLIONS GANGS DICE GAME\n")
player=int(input("Enter the numbers of available players:"))

while player>=1:
    a=input("Please Enter the  first player name:")
    name.append(a)
    b=input("Enter the second player name:")
    name.append(b)
    c=input("Enter the third player name:")
    name.append(c)
    d=input("Enter the fourth player name:")
    name.append(d)
    player-=2


    b=player 

    for c in name:
        d=input("Press 1 to roll dice:")
        print(name[b], random.randint(1,4), ':', random.randint(1,4))
        b+=1
