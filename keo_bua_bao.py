import random

player = input(("Input Rock Paper Scrissor:"))
computer = random.randint(0,2)

if computer == 0:
    computer = "Rock"
if computer == 1:
    computer = "Paper"
if computer == 2:
    computer = "Srissor"

print(computer)

if player == computer:
    print("Draw")

else:
    if player == "Rock":
        if computer == "Paper":
            print("win")
        else:
            print("lose")
        
    if player == "Paper":
        if computer == "Rock":
            print("win")
        else:
            print("lose")

    if player == "Srissor":
        if computer == "Paper":
            print("win")
        else:
            print("lose")