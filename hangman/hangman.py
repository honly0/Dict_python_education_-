import random

WORDS = ["python", "java", "javascript", "php"]


def play_one_game():
    secret = random.choice(WORDS)
    attempts = 8
    guessed_letters = set()
    current = ["-"] * len(secret)

    while attempts > 0:
        print()
        print("".join(current))
        letter = input("Input a letter: ")

        
        if len(letter) != 1:
            print("You should input a single letter")
            continue

        
        if not ("a" <= letter <= "z"):
            print("Please enter a lowercase English letter")
            continue

        
        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(letter)

        if letter in secret:
            
            for i, ch in enumerate(secret):
                if ch == letter and current[i] == "-":
                    current[i] = letter

            
            if "-" not in current:
                print()
                print("".join(current))
                print(f"You guessed the word {secret}!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    
    print("You lost!")


def main():
    print("HANGMAN")
    while True:
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == "play":
            play_one_game()
        elif command == "exit":
            break
        else:
            continue



