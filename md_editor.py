def main():

    formatters = {"plain": plain,
                  "bold": bold,
                  "italic": italic,
                  "header": header,
                  "link": link,
                  "inline-code": inline_code,
                  "ordered-list": make_list,
                  "unordered-list": make_list,
                  "new-line": new_line}

    stored_string = ""

    while True:
        user_input = input("- Choose a formatter: ").lower()

        if user_input == "!help":
            print("Available formatters: plain bold italic header link "
                  "inline-code ordered-list unordered-list new-line")
            print("Special commands: !help !done")

        elif user_input in formatters.keys():
            if user_input in ["ordered-list", "unordered-list"]:
                stored_string += formatters[user_input](user_input)
                print(stored_string)
            else:
                stored_string += formatters[user_input]()
                print(stored_string)

        elif user_input == "!done":
            conv_string_file(stored_string)
            exit()

        else:
            print("Unknown formatting type or command. Please try again.")


def plain():
    text_input = input("- Text: ")
    return text_input


def bold():
    text_input = input("- Text: ")
    return "**" + text_input + "**"


def italic():
    text_input = input("- Text: ")
    return "*" + text_input + "*"


def header():
    while True:
        try:
            title_level = int(input('Level: '))
            if title_level in range(1, 7):
                break
            print('The level should be within the range of 1 to 6')
        except ValueError:
            print(ValueError)
            pass

    title_input = input("- Text: ")
    return "#" * title_level + " " + title_input + "\n"


def link():
    input_label = input("- Label: ")
    input_url = input("- URL: ")
    return "[" + input_label + "]" + "(" + input_url + ")"


def inline_code():
    text_input = input("- Text: ")
    return "`" + text_input + "`"


# function for ordered-list & unordered-list formatters
def make_list(user_input):

    list_string = ""

    while True:
        try:
            rows = int(input("- Number of rows: "))
            if rows >= 1:
                break
            print("The number of rows should be greater than zero")
        except ValueError:
            print("Please enter a valid number of rows")
            pass

    for r in range(1, rows + 1):
        if user_input == "ordered-list":
            list_string += f"{r}. " + input(f"- Row #{r}: ") + "\n"
        else:
            list_string += "* " + input(f"- Row #{r}: ") + "\n"

    return list_string


def new_line():
    return "\n"


def conv_string_file(text):
    f = open('output.md', 'w+')
    f.write(text)
    f.close()


if __name__ == '__main__':
    main()
