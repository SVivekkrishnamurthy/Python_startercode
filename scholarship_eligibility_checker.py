"""Check whether a student meets the scholarship eligibility requirements."""

import math


INCOME_LIMIT = 250000
MIN_ATTENDANCE = 75
CATEGORY_PERCENTAGE_REQUIREMENTS = {
    "general": 75,
    "reserved": 65,
}


def qualifies_for_scholarship(category, percentage, family_income, attendance):
    required_percentage = CATEGORY_PERCENTAGE_REQUIREMENTS[category]
    return (
        percentage >= required_percentage
        and family_income <= INCOME_LIMIT
        and attendance >= MIN_ATTENDANCE
    )


def get_percentage(prompt):
    while True:
        try:
            percentage = float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid percentage.")
            continue

        if not math.isfinite(percentage) or not 0 <= percentage <= 100:
            print("Percentage must be between 0 and 100.")
            continue
        return percentage


def get_family_income():
    while True:
        try:
            income = float(input("Family income (Rs.): ").strip())
        except ValueError:
            print("Please enter a valid income.")
            continue

        if not math.isfinite(income) or income < 0:
            print("Family income cannot be negative.")
            continue
        return income


def get_category():
    while True:
        category = input("Category (General/Reserved): ").strip().lower()
        if category in CATEGORY_PERCENTAGE_REQUIREMENTS:
            return category
        print("Please enter General or Reserved.")


def main():
    name = input("Student name: ").strip()
    category = get_category()
    percentage = get_percentage("Percentage scored: ")
    family_income = get_family_income()
    attendance = get_percentage("Attendance percentage: ")

    qualifies = qualifies_for_scholarship(
        category, percentage, family_income, attendance
    )

    print()
    if qualifies:
        print(f"{name or 'The student'} qualifies for the scholarship.")
    else:
        print(f"{name or 'The student'} does not qualify for the scholarship.")


if __name__ == "__main__":
    main()
