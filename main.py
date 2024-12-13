import random

VALID_COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]

class ColorGame:
    def __init__(self):
        self.games_won = 0
        self.games_lost = 0
        self.player_name = ""
    
    def start_game(self):
        self.player_name = input("Please enter your name for the scoreboard: ").strip()
        while True:
            print("\n1> Start Game")
            print("2> Exit")
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.play_game()
            elif choice == "2":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def play_game(self):
        print("\nStarting the game...")
        machine_color = random.choice(VALID_COLORS)
        attempts = 0
        max_attempts = 5
        
        while attempts < max_attempts:
            attempts += 1
            user_color = input("\nPlease enter a color: ").strip().lower()
            
            if user_color not in VALID_COLORS:
                print("Invalid color. Please enter a valid color.")
                attempts -= 1  # Invalid attempt does not count
                continue
            
            if user_color == machine_color:
                print(f"You won the game! 🎉\nNumber of attempts: {attempts}")
                self.games_won += 1
                break
            else:
                attempts_left = max_attempts - attempts
                if attempts_left > 0:
                    print(f"Your guess was wrong. Please try again. Attempts left: {attempts_left}")
                else:
                    print(f"Sorry, you've used all attempts. The correct color was '{machine_color}'.")
                    self.games_lost += 1
        
        self.post_game_menu()
    
    def post_game_menu(self):
        while True:
            print("\n1> See Scoreboard")
            print("2> Play Again")
            print("3> Exit")
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.display_scoreboard()
            elif choice == "2":
                self.play_game()
                break
            elif choice == "3":
                print("Exiting the game. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")
    
    def display_scoreboard(self):
        print("\n--- Scoreboard ---")
        print(f"Player Name: {self.player_name}")
        print(f"Number of games won: {self.games_won}")
        print(f"Number of games lost: {self.games_lost}")


# Main program
if __name__ == "__main__":
    print("Welcome to the Color Game!")
    game = ColorGame()
    game.start_game()