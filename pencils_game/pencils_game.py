import random

NAMES = ["John", "Jack"]  


def ask_pencils() -> int:
    while True:
        s = input("How many pencils would you like to use:\n")
        if not s.isdigit():
            print("The number of pencils should be numeric")
            continue

        n = int(s)
        if n == 0:
            print("The number of pencils should be positive")
            continue

        return n


def ask_first_player() -> str:
    while True:
        first = input(f"Who will be the first ({NAMES[0]}, {NAMES[1]}):\n")
        if first not in NAMES:
            print(f"Choose between '{NAMES[0]}' and '{NAMES[1]}'")
            continue
        return first


def bot_move(pencils: int) -> int:
    
    if pencils == 1:
        return 1

    if pencils % 4 == 0:
        return 3
    if pencils % 4 == 3:
        return 2
    if pencils % 4 == 2:
        return 1

    
    return random.randint(1, min(3, pencils))


def main():
    pencils = ask_pencils()
    current = ask_first_player()

    while pencils > 0:
        print("|" * pencils)

        if current == "John":
            print("John's turn!")
            move = input()

            if move not in ("1", "2", "3"):
                print("Possible values: '1', '2' or '3'")
                continue

            taken = int(move)

            if taken > pencils:
                print("Too many pencils were taken")
                continue
        else:
            
            print("Jack's turn:")
            taken = bot_move(pencils)
            print(taken)

        pencils -= taken

        if pencils == 0:
            
            winner = NAMES[0] if current == NAMES[1] else NAMES[1]
            print(f"{winner} won!")
            break

        
        current = NAMES[0] if current == NAMES[1] else NAMES[1]


if __name__ == "__main__":
    main()
