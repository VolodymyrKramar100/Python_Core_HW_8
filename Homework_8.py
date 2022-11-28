from datetime import date, timedelta

users = [{'name': 'Vova', 'birthday': date(year=1990, month=6, day=27)},
         {'name': 'Pavel', 'birthday': date(year=1989, month=5, day=15)},
         {'name': 'Sonic', 'birthday': date(year=1990, month=4, day=10)},
         {'name': 'Olena', 'birthday': date(year=1994, month=12, day=4)},
         {'name': 'Oksana', 'birthday': date(year=1992, month=10, day=13)}]


def get_birthdays_per_week(users: list) -> None:
    result = {}
    count = start_index()
    for _ in range(7):
        interval = timedelta(days=count)
        week_day = date.today() + interval
        day = week_day.strftime('%A')
        for user in users:
            name = user['name']
            birthday = user['birthday'].replace(year=date.today().year)
            if birthday == week_day:
                if day not in ('Saturday', 'Sunday'):
                    result.setdefault(day, [])
                    result[day].append(name)
                else:
                    result.setdefault('Monday', [])
                    result['Monday'].append(name)
        count += 1

    print_birthday(result)


def start_index() -> int:
    week_day = date.today()
    day = week_day.strftime('%A')
    if day == 'Sunday':
        count = -1
    elif day == 'Monday':
        count = -2
    else:
        count = 0
    return count


def print_birthday(birth_dict: dict) -> None:
    for day_of_week in birth_dict.keys():
        print_result = f'{day_of_week}: '
        for name in birth_dict[day_of_week]:
            print_result += f'{name}, '
        print(f'{print_result}\b\b')


get_birthdays_per_week(users)

