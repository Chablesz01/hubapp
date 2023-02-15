import random
min=1
max=6
num1=random.randint(1,6)
name=[]
players=int(input('''
welcome to five billions dice Game!!!
Enter the number of availables players:
'''))
while players>=1:
    a=input("Enter your name:")
    name.append(a)
    players-=1

    c=int(input("Press 1 tp roll dice:"))

    print(name[0], ":",random.randint(1,6), ": ", random.randint(1,6))

    c=int(input("press 1 to roll dice:"))

    print(name[1], ": ",random.randint(1,6), ":", random.randint(1,6))



    