import random


def get_computer_choice():
    # The computer randomly chooses between 'rock', 'paper', and 'scissor'
    return random.choice(["rock", "paper", "scissor"])


def get_user_choice():
    # Ask the user to enter their choice
    choice = input("Enter your choice (rock, paper, scissor): ").lower()
    # Ensure the user's input is valid
    while choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please choose from 'rock', 'paper', or 'scissor'.")
        choice = input("Enter your choice (rock, paper, scissor): ").lower()
    return choice


def determine_winner(user_choice, computer_choice):
    # Determine who wins based on the rules
    if user_choice == computer_choice:
        return "It's a tie!"

    if (
        (user_choice == "rock" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "scissor")
        or (user_choice == "scissor" and computer_choice == "rock")
    ):
        return "Computer win!"

    return "You wins!"


def play_game():
    print("Welcome to the Rock, Paper, Scissor Game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer choose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


# Start the game
play_game()
