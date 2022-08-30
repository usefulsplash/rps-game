import random, sys

print("ROCK PAPER SCISSORS")
wins = 0
losses = 0
ties = 0

# Main game loop
while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    # Player input loop
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            print("Thanks for playing!")
            sys.exit()  # quits program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break  # break out of player input loop
        print(
            "Type either r, p, s, or q please."
        )  # error handling if user input is invalid
    # Display player choice
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

    # Computer choice display
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    # Final display and W/L/T recording
    if playerMove == computerMove:
        print("It is a tie!")
        ties += 1
    elif (
        (playerMove == "r" and computerMove == "s")
        or (playerMove == "p" and computerMove == "r")
        or (playerMove == "s" and computerMove == "p")
    ):
        print("You win!")
        wins += 1
    elif (
        (playerMove == "r" and computerMove == "p")
        or (playerMove == "p" and computerMove == "s")
        or (playerMove == "s" and computerMove == "r")
    ):
        print("You lose...")
        losses += 1
