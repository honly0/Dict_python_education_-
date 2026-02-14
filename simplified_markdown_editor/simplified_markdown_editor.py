formatters = [
    "plain", "bold", "italic", "header",
    "link", "inline-code",
    "ordered-list", "unordered-list",
    "new-line"
]

special_commands = ["!help", "!done"]

markdown = ""


def print_help():
    print("Available formatters:", *formatters)
    print("Special commands:", *special_commands)


def add_plain():
    return input("Text: ")


def add_bold():
    return f"**{input('Text: ')}**"


def add_italic():
    return f"*{input('Text: ')}*"


def add_inline_code():
    return f"`{input('Text: ')}`"


def add_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def add_header():
    while True:
        level = input("Level: ")
        if not level.isdigit() or not (1 <= int(level) <= 6):
            print("The level should be within the range of 1 to 6.")
        else:
            break
    text = input("Text: ")
    return "#" * int(level) + " " + text + "\n"


def add_new_line():
    return "\n"


def add_list(ordered=True):
    while True:
        rows = input("Number of rows: ")
        if not rows.isdigit() or int(rows) <= 0:
            print("The number of rows should be greater than zero")
        else:
            rows = int(rows)
            break

    result = ""
    for i in range(1, rows + 1):
        text = input(f"Row #{i}: ")
        if ordered:
            result += f"{i}. {text}\n"
        else:
            result += f"* {text}\n"

    return result


while True:
    command = input("Choose a formatter: ") 

    if command == "!help":
        print_help()

    elif command == "!done":
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(markdown)
        break

    elif command not in formatters:
        print("Unknown formatting type or command")

    else:
        if command == "plain":
            markdown += add_plain()
        elif command == "bold":
            markdown += add_bold()
        elif command == "italic":
            markdown += add_italic()
        elif command == "inline-code":
            markdown += add_inline_code()
        elif command == "link":
            markdown += add_link()
        elif command == "header":
            markdown += add_header()
        elif command == "new-line":
            markdown += add_new_line()
        elif command == "ordered-list":
            markdown += add_list(True)
        elif command == "unordered-list":
            markdown += add_list(False)

        print(markdown)
