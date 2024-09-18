import random
choice=["rock","paper","scissor"]
a=1
while(a==1):
  print(choice)
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
    b=1
    while(b==1):
       play=input("play again ?...type yes or no : ")
       if(play=="No" or play=="no"):
            a=0
            b=0
       elif(play=="Yes" or play=="yes"):
            a=1
            b=0
       else:
           print("please enter yes or no : ")
  else:
    print("Please enter Right choice.... ")