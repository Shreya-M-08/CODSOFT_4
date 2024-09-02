import random

choices = ("rock", "paper", "scissors")
play_again = True

u = 0
c = 0

while play_again:
    user = None
    play = None
    computer = random.choice(choices)

    while user not in choices:
        user = input("Choose rock, paper or scissors : ")

    print(f"User : {user}")
    print(f"Computer : {computer}")

    if user == computer:
        print("It's a tie!")
        print(f"User: {u} \nComputer: {c}\n")
    elif user == "scissors" and computer == "paper":
        print("You Win!\n")
        u += 1
        print(f"User: {u} \nComputer: {c}\n")
    elif user == "rock" and computer == "scissors":
        print("You Win!\n")
        u += 1
        print(f"User: {u} \nComputer: {c}\n")
    elif user == "paper" and computer == "rock":
        print("You Win!\n")
        u += 1
        print(f"User: {u} \nComputer: {c}\n")
    else:
        print("Computer Wins\n")
        c += 1
        print(f"User: {u} \nComputer: {c}\n")

    choices2 = ("y", "n")
    while play not in choices2:
        play = input("Play again?  (y/n) : ").lower()
        if play == "y":
            play_again = True
        if play == "n":
            play_again = False


print("Thanks for playing!  :)")
