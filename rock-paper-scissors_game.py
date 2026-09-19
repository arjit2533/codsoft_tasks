import random

def print_header():
    """Prints the styled ASCII header for the CLI UI."""
    print("=" * 50)
    print("    R O C K   P A P E R   S C I S S O R S    ")
    print("=" * 50)
    print(" Rules: [Rock] beats [Scissors]")
    print("        [Scissors] beats [Paper]")
    print("        [Paper] beats [Rock]")
    print("-" * 50)

def rock_paper_scissors_cli():
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    print_header()

    while True:
        # Prompting user input via Command Line
        print("\n>>> YOUR TURN")
        user_choice = input("Select [rock, paper, scissors] or 'q' to quit: ").strip().lower()

        # Handle Quit Command
        if user_choice in ['q', 'quit', 'exit']:
            print("\n" + "=" * 50)
            print("                FINAL SCORES                  ")
            print("=" * 50)
            print(f"  Player Score  : {user_score}")
            print(f"  Computer Score: {computer_score}")
            print("-" * 50)
            print("  Thanks for playing! Goodbye.")
            print("=" * 50)
            break

        # CLI Input Validation Feedback
        if user_choice not in choices:
            print("\n[!] ERROR: Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer selection
        computer_choice = random.choice(choices)

        # CLI Visual Output Display
        print("\n" + "-" * 20 + " ROUND RESULT " + "-" * 20)
        print(f"  You chose     : {user_choice.upper()}")
        print(f"  Computer chose: {computer_choice.upper()}")
        print("-" * 54)

        # Game Logic
        if user_choice == computer_choice:
            result_msg = "IT'S A TIE!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            result_msg = "YOU WIN THIS ROUND! 🎉"
            user_score += 1
        else:
            result_msg = "COMPUTER WINS THIS ROUND! 🤖"
            computer_score += 1

        # Display Result & Updated Scoreboard
        print(f"  Outcome       : {result_msg}")
        print(f"  Scoreboard    : YOU [{user_score}]  |  COMPUTER [{computer_score}]")
        print("=" * 54)

        # Play Again CLI Prompt
        play_again = input("\nPlay another round? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("\n" + "=" * 50)
            print("                FINAL SCORES                  ")
            print("=" * 50)
            print(f"  Player Score  : {user_score}")
            print(f"  Computer Score: {computer_score}")
            print("-" * 50)
            print("  Thanks for playing! Goodbye.")
            print("=" * 50)
            break

if __name__ == "__main__":
    rock_paper_scissors_cli()