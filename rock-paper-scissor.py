import random
choice=["rock","paper","scissor"]
print(choice)
a=1
while(a==1):
  user=input("Please choose any one of them:  ")
  if(user== choice[0] or user== choice[1] or user== choice[2]):
    computer=random.choice(choice)
    print("computer: ",computer)
    if(user== computer):
        print("Draw")
    elif((user=="rock" and computer=="paper") or (user=="paper" and computer=="rock")):
        if(user=="paper"):
            print("user win ")
        else:
            print("computer win")
    elif((user=="rock" and computer=="scissor") or (user=="scissor" and computer=="rock")):
        if(user=="rock"):
            print("user win ")
        else:
            print("computer win")
    elif((user=="scissor" and computer=="paper") or (user=="paper" and computer=="scissor")):
        if(user=="scissor"):
            print("user win ")
        else:
            print("computer win")
    a=0
  else:
    print("Please enter Right choice.... ")