def print_board(c):
    print("---------")
    print(f"| {c[0]} {c[1]} {c[2]} |")
    print(f"| {c[3]} {c[4]} {c[5]} |")
    print(f"| {c[6]} {c[7]} {c[8]} |")
    print("---------")


def check(cells):
    wins = [
        [cells[0], cells[1], cells[2]],
        [cells[3], cells[4], cells[5]],
        [cells[6], cells[7], cells[8]],
        [cells[0], cells[3], cells[6]],
        [cells[1], cells[4], cells[7]],
        [cells[2], cells[5], cells[8]],
        [cells[0], cells[4], cells[8]],
        [cells[2], cells[4], cells[6]],
    ]

    if ["X", "X", "X"] in wins:
        return "X wins"
    if ["O", "O", "O"] in wins:
        return "O wins"
    if "_" not in cells:
        return "Draw"
    return "Game not finished"


cells = ["_"] * 9
player = "X"

print_board(cells)

while True:
    coords = input("Enter the coordinates: ").split()

    if not (len(coords) == 2 and coords[0].isdigit() and coords[1].isdigit()):
        print("You should enter numbers!")
        continue

    x, y = map(int, coords)

    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    index = (x - 1) + (3 * (y - 1))

    if cells[index] != "_":
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = player
    print_board(cells)

    result = check(cells)
    if result != "Game not finished":
        print(result)
        break

    player = "O" if player == "X" else "X"