"""Collect student details and print a formatted college ID card."""


def main():
    college = input("College name: ").strip()
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()
    course = input("Course: ").strip()
    department = input("Department: ").strip()
    academic_year = input("Academic year: ").strip()
    date_of_birth = input("Date of birth: ").strip()
    blood_group = input("Blood group: ").strip()
    contact = input("Contact number: ").strip()

    details = [
        ("Name", name),
        ("Student ID", student_id),
        ("Course", course),
        ("Department", department),
        ("Academic year", academic_year),
        ("Date of birth", date_of_birth),
        ("Blood group", blood_group),
        ("Contact", contact),
    ]

    content = [college.upper(), "COLLEGE ID CARD", ""]
    content.extend(f"{label}: {value}" for label, value in details)
    width = max(len(line) for line in content)

    print()
    print("+" + "-" * (width + 4) + "+")
    for line in content:
        print("|  " + line.ljust(width) + "  |")
    print("+" + "-" * (width + 4) + "+")


if __name__ == "__main__":
    main()
