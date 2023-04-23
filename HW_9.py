contacts = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Print help"
    return inner

def hello(*args):
    return "How can I help you?"

@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_contact = list_of_param[1]

    if name in contacts:
        return "name already exists"

    if phone_contact.isdigit() == False:
        return "phone has to be digit"


    contacts[name] = phone_contact

    return f'{name}, phone {phone_contact} added'

@input_error
def change(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_contact = list_of_param[1]

    if not phone_contact:
        raise IndexError()

    if phone_contact.isdigit() == False:
        return "phone has to be digit"
    contacts[name] = phone_contact

    return f'{name}, phone {phone_contact} changed'

@input_error
def phone(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    return f"{name} - {contacts[name]}"

def show_all(*args):
    return [f"{k}, {contacts[k]}" for k in contacts]

def good_bye(*args):
    return "Good bye!"

def no_command(*args):
    return "Unknown command, try again."

COMMANDS ={
    hello: "hello",
    add: "add",
    change: "change",
    phone: "phone",
    show_all: "show all",
    good_bye: "exit"
}

def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, "").strip()
    return no_command, None

def main():
    print(hello())
    while True:
        user_input = input("...")
        command, data = command_handler(user_input)
        print(command(data))
        if command == good_bye:
            break

if __name__ == "__main__":
    main()