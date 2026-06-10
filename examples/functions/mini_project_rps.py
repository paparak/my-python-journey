import random

def get_guess():
    """Gets and validates user input."""
    while True:
        try:
            choice = int(input("Choose: 1. Rock, 2. Scissors, 3. Paper: "))
            if 1 <= choice <= 3:
                return choice
            print("Invalid input! Please enter a number between 1 and 3.")
        except ValueError:
            print("Oops! That's not a number. Please try again.")

def get_winner(comp_pick, user_guess):
    """Determines the game outcome."""
    if user_guess == comp_pick:
        return "It's a tie! Try again."
    
    # Logic for winning/losing
    if (user_guess == 1 and comp_pick == 2) or \
       (user_guess == 2 and comp_pick == 3) or \
       (user_guess == 3 and comp_pick == 1):
        return "You won! Nice move."
    
    return "You lost! Better luck next time."

def play_game():
    print("--- Welcome to Rock, Paper, Scissors ---")
    continue_playing = True

    while continue_playing:
        comp_pick = random.randint(1, 3)
        user_guess = get_guess()
        print(f"Result: {get_winner(comp_pick, user_guess)}")

        # Game loop logic
        play_again = input("Play again? (yes/no): ").lower()
        if play_again == 'yes':
            continue # Goes to the next round
        
        # 'Takhs' logic: Ask one more time to be persistent
        check_again = input("Are you sure? You're giving up already? (yes/no): ").lower()
        
        if check_again == 'no':
            # If they say 'no' (not giving up), keep playing
            print("Great! Let's play again.")
            continue_playing = True 
        else:
            # If they say 'yes' (sure about giving up), stop the game
            print("Game over. See you next time!")
            continue_playing = False

if __name__ == "__main__":
    play_game()
