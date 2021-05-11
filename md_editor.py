
COMMANDS = ["plain",
            "bold",
            "italic",
            "header",
            "link",
            "inline-code",
            "ordered-list",
            "unordered-list",
            "new-line"]

stored_string = []


def command():
    user_input = input("- Choose a formatter: ")
    if user_input == "!help":
        print("Available formatters: plain bold italic header link inline-code"
              " ordered-list unordered-list new-line")
        print("Special commands: !help !done")
        command()
    elif user_input in COMMANDS:
        formatter(user_input)
    elif user_input == "!done":
        exit()
    else:
        print("Unknown formatting type or command. Please try again.")
        command()


def plain():
    text_input = input("- Text: ")
    stored_string.append(text_input)
    print_string()
    command()


def bold():
    text_input = input("- Text: ")
    stored_string.append("**" + text_input + "**")
    print_string()
    command()


def italic():
    text_input = input("- Text: ")
    stored_string.append("*" + text_input + "*")
    print_string()
    command()


def header():
    title_level = int(input("- Level: "))
    if title_level not in range(1, 7):
        print("The level should be within the range of 1 to 6")
        header()
    else:
        title_input = input("- Text: ")
        stored_string.append("#" * title_level + " " + title_input + "\n")
        print_string()
        command()


def link():
    input_label = input("- Label: ")
    input_url = input("- URL: ")
    stored_string.append("[" + input_label + "]" + "(" + input_url + ")")
    print_string()
    command()


def inline_code():
    text_input = input("- Text: ")
    stored_string.append("`" + text_input + "`")
    print_string()
    command()


def ordered_list():
    pass


def unordered_list():
    pass


def new_line():
    stored_string.append("\n")
    print_string()
    command()


def formatter(user_input):
    if user_input == "plain":
        plain()
    elif user_input == "bold":
        bold()
    elif user_input == "italic":
        italic()
    elif user_input == "header":
        header()
    elif user_input == "link":
        link()
    elif user_input == "inline-code":
        inline_code()
    elif user_input == "ordered-list":
        ordered_list()
    elif user_input == "unordered-list":
        unordered_list()
    elif user_input == "new-line":
        new_line()
    else:
        print("Formatter type not recognised. Please try again.")
        command()


def print_string():
    print("".join(stored_string))


command()
