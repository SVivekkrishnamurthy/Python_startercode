"""Check whether a student meets the college admission requirements."""

import math


CATEGORY_PERCENTAGE_REQUIREMENTS = {
    "general": 75,
    "reserved": 60,
}
MIN_ENTRANCE_SCORE = 50
MIN_AGE = 17
MAX_AGE = 25


def qualifies_for_admission(category, percentage, entrance_score, age):
    normalized_category = category.strip().lower()
    if normalized_category not in CATEGORY_PERCENTAGE_REQUIREMENTS:
        raise ValueError("Category must be General or Reserved.")

    if not math.isfinite(percentage) or not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    if not isinstance(age, int) or not MIN_AGE <= age <= MAX_AGE:
        raise ValueError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")

    if not math.isfinite(entrance_score):
        raise ValueError("Entrance score must be a valid number.")

    return (
        percentage >= CATEGORY_PERCENTAGE_REQUIREMENTS[normalized_category]
        and entrance_score >= MIN_ENTRANCE_SCORE
    )


def get_category():
    while True:
        category = input("Category (General/Reserved): ").strip().lower()
        if category in CATEGORY_PERCENTAGE_REQUIREMENTS:
            return category
        print("Please enter General or Reserved.")


def get_percentage():
    while True:
        try:
            percentage = float(input("Class 12 percentage: ").strip())
        except ValueError:
            print("Please enter a valid percentage.")
            continue

        if not math.isfinite(percentage) or not 0 <= percentage <= 100:
            print("Percentage must be between 0 and 100.")
            continue
        return percentage


def get_entrance_score():
    while True:
        try:
            score = float(input("Entrance score: ").strip())
        except ValueError:
            print("Please enter a valid entrance score.")
            continue

        if not math.isfinite(score):
            print("Please enter a valid entrance score.")
            continue
        return score


def get_age():
    while True:
        try:
            age = int(input("Age: ").strip())
        except ValueError:
            print("Please enter a valid age in years.")
            continue

        if not MIN_AGE <= age <= MAX_AGE:
            print(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
            continue
        return age


def main():
    name = input("Student name: ").strip()
    category = get_category()
    percentage = get_percentage()
    entrance_score = get_entrance_score()
    age = get_age()

    qualifies = qualifies_for_admission(
        category, percentage, entrance_score, age
    )

    print()
    if qualifies:
        print(f"{name or 'The student'} is eligible for admission.")
    else:
        print(f"{name or 'The student'} is not eligible for admission.")


if __name__ == "__main__":
    main()
