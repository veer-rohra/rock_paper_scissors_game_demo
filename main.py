import random #import an library to make the computer choose randomly
computer = random.choice([-1,0,1])
yourchoice = input("enter your choice:") #input our choice
yourchoices = {"scissors" : -1,"rock" : 0,"paper" : 1} #all available choices
reversedict = {-1:"scissors",0:"rock",1:"paper"}

you = yourchoices[yourchoice]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(computer == you):
    print("it's a draw") #adding all the possible outcomes
else:
    if(computer ==-1 and you ==0):
        print("you win")
    elif(computer ==-1 and you ==1):
        print("you lose")
    elif(computer ==0 and you ==-1):
        print("you lose")
    elif(computer ==0 and you ==1):
        print("you win")
    elif(computer ==1 and you ==-1):
        print("you win")
    elif(computer ==1 and you ==0):
        print("you lose")
    else:
        print("something went wrong")
