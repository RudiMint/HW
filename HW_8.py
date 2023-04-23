from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint

def get_next_week_start(d: datetime.date):
    diff_days = 6 - d.weekday()
    return d + timedelta(days=diff_days)

def prepare_birthday(text: str):
    bd = datetime.strptime(text, "%d, %m, %Y")
    return bd.replace(year=datetime.now().year).date()

def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <= prepare_birthday(user["birthday"]) <= end_period]

    for user in happy_users:
        current_bd = prepare_birthday(user["birthday"])
        if current_bd.weekday() in (5, 6):
            birthdays["Monday"].append(user["name"])
        else:
            birthdays[current_bd.strftime("%A")].append(user["name"])

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Dasha", "birthday": "21, 4, 1967"},
        {"name": "Sasha", "birthday": "22, 4, 1985"},
        {"name": "Nastya", "birthday": "25, 4, 1999"},
        {"name": "Vlad", "birthday": "26, 4, 1997"}
    ]

    pprint(get_birthdays_per_week(users))

list = [1, 3, 5, 6, 7, 8]
new_list = list[2::]
print(new_list)
string = " ".join([str(i) for i in new_list])
print(string)