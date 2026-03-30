import random

def load_rating(name):
    rating = 0
    try:
        with open("rating.txt", "r") as f:
            for line in f:
                user, score = line.split()
                if user == name:
                    rating = int(score)
    except:
        pass
    return rating


name = input("Enter your name: ")
print(f"Hello, {name}")

options = input()
if options == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options.split(",")

print("Okay, let's start")

rating = load_rating(name)

while True:
    user = input()

    if user == "!exit":
        print("Bye!")
        break

    elif user == "!rating":
        print(f"Your rating: {rating}")

    elif user not in options:
        print("Invalid input")

    else:
        comp = random.choice(options)

        if user == comp:
            print(f"There is a draw ({comp})")
            rating += 50
        else:
            index = options.index(user)
            losing = options[index+1:] + options[:index]
            half = len(losing) // 2

            if comp in losing[:half]:
                print(f"Sorry, but the computer chose {comp}")
            else:
                print(f"Well done. The computer chose {comp} and failed") 
                rating += 100