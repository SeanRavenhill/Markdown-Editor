def main():

    formatters = {"plain": plain,
                  "bold": bold,
                  "italic": italic,
                  "header": header,
                  "link": link,
                  "inline-code": inline_code,
                  "ordered-list": ordered_list,
                  "unordered-list": unordered_list,
                  "new-line": new_line}

    stored_string = ""

    while True:
        user_input = input("- Choose a formatter: ").lower()

        if user_input == "!help":
            print("Available formatters: plain bold italic header link "
                  "inline-code ordered-list unordered-list new-line")
            print("Special commands: !help !done")

        elif user_input in formatters.keys():
            stored_string += formatters[user_input]()
            print(stored_string)

        elif user_input == "!done":
            break

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


def ordered_list():
    pass


def unordered_list():
    pass


def new_line():
    return "\n"


if __name__ == '__main__':
    main()
