import random 
print("1.Rock\n2.Paper\n3.Scissor")

y = int(input("Enter option: "))
c = random.randint(4,6)
if y==1 :
    if c==5:
        print("You loose computer has chosen paper")
    elif c==6:
        print("You win computer has chosen scissor")
    else:
         print("Play again")
elif y==2 :
    if c==4:
        print("you win computer has chosen rock")
    elif c==6:
         print("you loose computer has chosen scissor")
    else:
        print("Play again")
elif y==3:
    if c==4:
        print("you loose computer has chosen rock")
    elif c==5:
        print("you win computer has chosen paper")
    else:
        print("Play again")
else :
    print("Choose correct option")