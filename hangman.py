import random

HANGMAN = [
        "  _______",
        "  |     |",
        "  |     O",
        "  |    /|\\",
        "  |    / \\",
        "__|__"
]

WORDS = ["apple", "banana", "cherry", "durian", "raspberry", "fig", "grape"]

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_guesses = 6
        
        
    def display(self):
        # Display the current state of the game
        revealed_word = ""
        for letter in self.word:
            if letter in self.guesses:
                revealed_word += letter + " "
            else:
                revealed_word += "_"
        print("Word: " + revealed_word)
        # print("# of Guesses left: " + str(self.max_guesses))
                
        if self.max_guesses == 6:
            print("  _______")
            print("  |     |")
            print("  |     ")
            print("  |    ")
            print("  |    ")
            print("__|__")
        elif self.max_guesses == 5:
            print("  _______")
            print("  |     |")
            print("  |     O")
            print("  |    ")
            print("  |    ")
            print("__|__")
        elif self.max_guesses == 4:
            print("  _______")
            print("  |     |")
            print("  |     O")
            print("  |     |")
            print("  |    ")
            print("__|__")
        elif self.max_guesses == 3:
            print("  _______")
            print("  |     |")
            print("  |     O")
            print("  |    /|")
            print("  |    ")
            print("__|__")
        elif self.max_guesses == 2:
            print("  _______")
            print("  |     |")
            print("  |     O")
            print("  |    /|\\")
            print("  |    ")
            print("__|__")
        elif self.max_guesses == 1:
            print("  _______")
            print("  |     |")
            print("  |     O")
            print("  |    /|\\")
            print("  |    / ")
            print("__|__")
        else:
            print("  _______")
            print("  |     |")
            print("  |     O")
            print("  |    /|\\")
            print("  |    / \\")
            print("__|__")
                                  
    def update(self, letter):
        if letter in self.word:
            self.guesses.append(letter)
            print("Good guess! '"+ letter +"' is in the word.")
        else:
            self.max_guesses -= 1
            print("Bad guess...'" + letter +"' is not in the word.")
          
    def is_game_over(self):
        # Check if the game has ended
        if all(letter in self.guesses for letter in self.word):
            print(f"Congratulations! You correctly guessed the word {self.word}!")
            return True
        elif self.max_guesses == 0:
            print(f"Sorry, you ran out of guesses. The word was {self.word}.")
            return True
        else:
            return False
    
    def play(self):
        player = Player()
        print("Welcome to Lauron's Hangman!")
        # player.set_name()
        while not self.is_game_over():
            self.display()
            guess = player.guess()
            self.update(guess)
        print("Game over.")
        self.display()
    
        return all(letter in self.guesses for letter in self.word)
        
    def tryAgain(self):
        prompt = input('\nWould you like to play again? (Y/N) ')
        if (prompt == 'Y'):
            return True
        elif (prompt == 'N'):
            print("Thanks for playing!")
            return False
        else:
            exit
            
class Player:
    def __init__(self):
        # self.name = ""
        self.score = 0
        
    # def set_name(self):
        # self.name = input("Enter your name: ")
    
    def guess(self):
        user_input = input('\nPlease type a letter: ')
        return user_input
        

if __name__ == '__main__':
    while True:
        word = random.choice(WORDS)
        hangman = Hangman(word)
        won_game = hangman.play()
        if not hangman.tryAgain():
            break
    