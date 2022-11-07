levels = ["1", "2", "3", "4", "5", "6"]
text = ""
help_msg = "Available formatters: plain bold italic header link inline-code new-line unordered-list ordered-list\n" \
           "Special commands: !help !done"


def header():
    while True:
        level = input("Level:")
        if level in levels:
            level = int(level) * "#"
            text_input = input("Text:")
            return f"{level} {text_input}\n"
        else:
            print("The level should be within the range of 1 to 6")


def plain():
    text_input = input("Text:")
    return text_input


def bold():
    text_input = input("Text:")
    return f"**{text_input}**"


def italic():
    text_input = input("Text:")
    return f"*{text_input}*"


def inline_code():
    text_input = input("Text:")
    return f"`{text_input}`"


def new_line():
    return "\n"


def link():
    label_input = input("Label:")
    url_input = input("URL:")
    return f"[{label_input}]({url_input})"


def ordered_list():
    while True:
        rows_num = int(input("Number of rows:"))
        if rows_num > 0:
            ordered_text_list = [str(i) + ". " + input(f"Row #{i}: ") for i in range(1, rows_num + 1)]
            ordered_text = "\n".join(ordered_text_list) + "\n"
            return ordered_text
        else:
            print("The number of rows should be greater than zero")


def unordered_list():
    while True:
        rows_num = int(input("Number of rows:"))
        if rows_num > 0:
            unordered_text_list = ["* " + input(f"Row #{i}: ") for i in range(1, rows_num + 1)]
            unordered_text = "\n".join(unordered_text_list) + "\n"
            return unordered_text
        else:
            print("The number of rows should be greater than zero")


def done():
    markdown_file = open("output.md", "w")
    markdown_file.write(text)
    markdown_file.close()


formatters = {"plain": plain, "bold": bold, "italic": italic, "header": header, "link": link,
              "inline-code": inline_code, "new-line": new_line, "ordered-list": ordered_list,
              "unordered-list": unordered_list}


def formatter_choice():
    global text
    while True:
        user_input = input("Choose a formatter:")
        if user_input in formatters:
            text += formatters[user_input]()
            print(text)
        elif user_input == "!help":
            print(help_msg)
        elif user_input == "!done":
            done()
            break
        else:
            print("Unknown formatting type or command")


formatter_choice()
