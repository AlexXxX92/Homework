from datetime import date
from application import salary
from application.db import people
import requests


def get_date():
    today_ = date.today().strftime('%d.%m.%Y')
    print(f'Сегодня: {today_}')


if __name__ == '__main__':
    get_date()
    salary.calculate_salary()
    people.get_employees()
