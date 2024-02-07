import random
import pygame

class NumberGuessingGame:
    def __init__(self):
        self.total_rounds = 0
        self.total_wins = 0
        pygame.mixer.init()
        self.start_sound = pygame.mixer.Sound(r"C:\Users\intel\Downloads\start_sound.mp3")
        self.wrong_guess_sound = pygame.mixer.Sound(r"C:\Users\intel\Downloads\wrong_choice.mp3")
        self.correct_guess_sound = pygame.mixer.Sound(r"C:\Users\intel\Downloads\correct_choice.mp3")
        self.end_game_sound = pygame.mixer.Sound(r"C:\Users\intel\Downloads\warning-sound-6686.mp3")
        self.new_round_sound = pygame.mixer.Sound(r"C:\Users\intel\Downloads\new_round.mp3")
        self.low_attempts_warning_sound = pygame.mixer.Sound(r"C:\Users\intel\Downloads\warning-sound-6686.mp3")

    def play_round(self, difficulty_level):
        self.new_round_sound.play()
        if difficulty_level == 'easy':
            number_to_guess = random.randint(1, 50)
            max_attempts = 5
        else:  # hard levelh
            number_to_guess = random.randint(1, 1000)
            max_attempts = 10

        attempts = 0

        while attempts < max_attempts:
            guess = int(input(f"Guess a number between 1 and {number_to_guess} (Attempt {attempts+1}/{max_attempts}): "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
                self.wrong_guess_sound.play()
            elif guess > number_to_guess:
                print("Too high!")
                self.wrong_guess_sound.play()
            else:
                print(f"Congratulations! You found the number in {attempts} attempts.")
                self.correct_guess_sound.play()
                return True

            if max_attempts - attempts == 2:
                self.low_attempts_warning_sound.play()

        print(f"Sorry, you didn't guess the number. It was {number_to_guess}.")
        return False

    def play_game(self):
        self.start_sound.play()
        print("Welcome to the Number Guessing Game!")
        while True:
            difficulty_level = input("Choose difficulty level (easy/hard): ")
            self.total_rounds += 1
            if self.play_round(difficulty_level):
                self.total_wins += 1
            print(f"Your stats: {self.total_wins} wins in {self.total_rounds} rounds ({self.total_wins/self.total_rounds*100:.2f}% win rate)")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                self.end_game_sound.play()
                break

# Start the game
game = NumberGuessingGame()
game.play_game()
