from collections import UserDict
from datetime import datetime, timedelta, date
import pickle
from copy import copy


class Field:

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, value, phone=None):
        self.phone = phone
        if not phone.isdigit():
            raise ValueError('Must be a digit')
        self.value = value


class Birthday(Field):
    def __init__(self, date_of_birth=None):
        self.date_of_birth = date_of_birth
        try:
            datetime.strptime(date_of_birth, "%d.%m.%Y")
        except:
            ValueError("date must be in format dd.mm.yy")


class Record(Name, Phone, Birthday):

    def __init__(self, name: Name, phone: Phone, birthday: Birthday):
        self.name = name
        self.birthday = birthday
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_number(self, phone: Phone):
        self.phones.append(phone)

    def change_number(self, phone: Phone, new_phone: Phone):
        if phone in self.phones:
            for item in self.phones:
                if item == phone:
                    self.phones.remove(phone)
                    self.phones.append(new_phone)
        else:
            return f"{phone} not found"

    def delete(self, phone: Phone):
        if phone in self.phones:
            for item in self.phones:
                if item == phone:
                    self.phones.remove(phone)

    def days_to_birthday(self, name: Name):
        today = datetime.now().date()
        bd = datetime.strptime(self.birthday, "%d.%m.%Y").date()
        bd.replace(year=datetime.now().year)
        return f"{-(bd - today)} before birthday"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.current_value = 0

    def add_field(self, field: Record):
        self.data[field.name] = field

    def search_by_name(self, name: Name):
        if name in self.data:
            print(self.data[name].name)
            print(self.data[name].phones)
            print(self.data[name].birthday)
        else:
            print(f"Contact {name} not found")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.data.__len__():
            self.current_value += 1
            return self.data[self.current_value - 1]
        raise StopIteration


def hello(*args):
    return "How can I help you?"


def good_bye(*args):
    return "Good bye!"


def no_command(*args):
    return "Unknown command, try again."


def create_contact(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = None
    birthday = None
    match len(list_of_param):
        case 2:
            if list_of_param[1].isdigit():
                phone_number = list_of_param[1]
            else:
                birthday = list_of_param[1]
        case 3:
            phone_number = list_of_param[1]
            birthday = list_of_param[2]

    contact = Record(name, phone_number, birthday)
    addressbook.add_field(contact)


def add_number(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = list_of_param[1]
    addressbook.data[name].add_number(phone_number)


def change_number(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    old_phone_number = list_of_param[1]
    new_phone_number = list_of_param[2]
    print(addressbook.data[name].change_number(old_phone_number, new_phone_number))


def days_to_birthday(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    print(addressbook.data[name].days_to_birthday(name))


def search_by_name(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    print(addressbook.search_by_name(name))


def store_addressbook(*args):
    with open("test.pickle", "wb") as outfile:
        pickle.dump(addressbook.data, outfile)


def load_addressbook(*args):
    with open("test.pickle", "rb") as infile:
        addressbook.data = pickle.load(infile)


COMMANDS = {
    hello: "hello",
    add_number: "add",
    change_number: "change",
    Phone: "phone",
    search_by_name: "search",
    good_bye: "exit",
    create_contact: "new contact",
    days_to_birthday: "days to birthday",
    store_addressbook: "store",
    load_addressbook: "load"
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
    addressbook = AddressBook()
    main()
