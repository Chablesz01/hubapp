from tkinter import*
import random

root=Tk()
root.title("Guessing Game")
root.geometry("600x400")

e=random.randint(1,31)

def exi():
    root.destroy()
def submit():

    
    f= 1
    z=int(c.get())
    print(e)

    
    while f<=5:

        if z==e: 
            g=Label(root,text="welldone. you guessed right",bg="black",fg="white",font=("Cambria Bold",12)).grid(row=4,column=1)
            
            h=Button(root,text="exit",command=exi,bg="red",fg="white",font=("Arial Bold",10)).grid(row=5, column=1)
            
            break
        
        elif z>30:
             g=Label(root,text="Guess between 1 and 30",bg="black", fg="white",font=("Arial",8)).grid(row=4, column=1)
            
        elif z<e:
             g=Label(root,text="Your guess is Lower X, guess higher").grid(row=4, column=1)
            
        elif z>e:
             g=Label(root,text="Your guess is higher X, guess lower").grid(row=4,column=1)
            
        else:
             g=Label(root,text="Guess between 1 and 30......",bg='black',fg='white').grid(row=5, column=1)
             f+=1



a=Label(root,text="CHABLESZ GUESSING GAME",font=("Cambria Bold",20), bg="black",fg="white").grid(row=0,column=1)
b=Label(root,text="Guess a number:",font=("Cambria",16), bg="black",fg="white").grid(row=1, column=0) 
c=Entry(root,width=30)
c.grid(row=1,column=1)
d=Button(root,text="Submit",font=("Cambria",14),bg="dark green",fg="white" ,command=submit).grid(row=2,column=1)


root.mainloop()
                     
