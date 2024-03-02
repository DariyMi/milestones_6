import csv
import random
from faker import Faker

fake = Faker()

departments = ['HR', 'Finance', 'Engineering', 'R&D', 'Legal']


def generate_employee():
    name = fake.name()
    hiring_date = fake.date_between(start_date='-5y', end_date='today')
    birthday = fake.date_of_birth(minimum_age=20, maximum_age=60)
    department = random.choice(departments)
    return [name, hiring_date, birthday, department]


def generate_data(database: csv, num: int):
    with open(database, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Hiring date', 'Birthday', 'Department'])
        for _ in range(num):
            empl = generate_employee()
            writer.writerow([empl[0], empl[1], empl[2], empl[3]])


generate_data('database.csv', 15)
