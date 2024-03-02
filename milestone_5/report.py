import csv
import sys
from collections import defaultdict

months = {
    'january': '01',
    'february': '02',
    'march': '03',
    'april': '04',
    'may': '05',
    'june': '06',
    'july': '07',
    'august': '08',
    'september': '09',
    'october': '10',
    'november': '11',
    'december': '12'
}


def read_database(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def count_events(data, month):
    birthdays = defaultdict(int)
    anniversaries = defaultdict(int)

    for employee in data:
        hiring_month = employee['Hiring date'].split('-')[1]
        birthday_month = employee['Birthday'].split('-')[1]

        if hiring_month == months[month.lower()]:
            anniversaries[employee['Department']] += 1

        if birthday_month == months[month.lower()]:
            birthdays[employee['Department']] += 1

    return birthdays, anniversaries


def report(birthdays, anniversaries, verbose=False):
    print(f"Report for {month.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {sum(birthdays.values())}")
    for department, count in birthdays.items():
        print(f"- {department}: {count}")
    print("--- Anniversaries ---")
    print(f"Total: {sum(anniversaries.values())}")
    for department, count in anniversaries.items():
        print(f"- {department}: {count}")


if len(sys.argv) < 3:
    print("Usage: python report.py <database_file> <month>")
    sys.exit(1)

database_file = sys.argv[1]
month = sys.argv[2]


data = read_database(database_file)
birthdays, anniversaries = count_events(data, month)
report(birthdays, anniversaries)
