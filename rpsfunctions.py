import random
from enum import IntEnum

wins = 0
losses = 0
ties = 0


class Choice(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_player_choice():
    choices = [f"{choice.name}({choice.value})" for choice in Choice]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter your move - {choices_str}: "))
    choice = Choice(selection)
    if choice == 0:
        print("ROCK versus...")
    elif choice == 1:
        print("PAPER versus...")
    elif choice == 2:
        print("SCISSORS versus...")
    return choice


def get_computer_choice():
    selection = random.randint(0, len(Choice) - 1)
    choice = Choice(selection)
    if choice == 0:
        print("ROCK")
    elif choice == 1:
        print("PAPER")
    elif choice == 2:
        print("SCISSORS")
    return choice


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a tie!")
        result = "tie"
    elif player_choice == Choice.Rock:
        if computer_choice == Choice.Scissors:
            print("ROCK smashes SCISSORS! You win!")
            result = "win"
        else:
            print("PAPER covers ROCK! You lose...")
            result = "loss"
    elif player_choice == Choice.Paper:
        if computer_choice == Choice.Rock:
            print("PAPER covers ROCK! You win!")
            result = "win"
        else:
            print("SCISSORS cuts PAPER! You lose...")
            result = "loss"
    elif player_choice == Choice.Scissors:
        if computer_choice == Choice.Paper:
            print("SCISSORS cuts PAPER! You win!")
            result = "win"
        else:
            print("ROCK smashes SCISSORS! You lose...")
            result = "loss"
    return result


# Main Game Loop Driver
while True:
    # Gets player choice (with exception handling for user error)
    try:
        player_choice = get_player_choice()
    except ValueError as e:
        range_str = f"[0, {len(Choice) -1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    # Tracks and displays W/L/T
    if result == "win":
        wins += 1
    elif result == "loss":
        losses += 1
    elif result == "tie":
        ties += 1
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
