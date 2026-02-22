import random


def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")

        level = input()

        if level in ("1", "2"):
            return int(level)
        else:
            print("Incorrect format.")


def generate_question(level):
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operator = random.choice(["+", "-", "*"])
        print(f"{a} {operator} {b}")
        return eval(f"{a}{operator}{b}")
    else:
        a = random.randint(11, 29)
        print(a)
        return a ** 2


def get_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")


def save_result(name, score, level):
    descriptions = {
        1: "simple operations with numbers 2-9",
        2: "integral squares of 11-29"
    }

    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {score}/5 in level {level} ({descriptions[level]}).\n")


def main():
    level = get_level()
    score = 0

    for _ in range(5):
        correct_answer = generate_question(level) 
        user_answer = get_answer()

        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your mark is {score}/5.")

    print("Would you like to save your result to the file? Enter yes or no.")
    choice = input().lower()

    if choice in ("yes", "y"):
        print("What is your name?")
        name = input()
        save_result(name, score, level)
        print('The results are saved in "results.txt".')


if __name__ == "__main__":
    main()
