"""Count student attendance and calculate the attendance percentage."""


def get_student_count():
    while True:
        try:
            student_count = int(input("Number of students: ").strip())
        except ValueError:
            print("Please enter a whole number greater than zero.")
            continue

        if student_count <= 0:
            print("The number of students must be greater than zero.")
            continue
        return student_count


def get_attendance_status(student_number):
    while True:
        status = input(
            f"Student {student_number} status (Present/Absent): "
        ).strip().lower()
        if status in ("present", "p"):
            return "present"
        if status in ("absent", "a"):
            return "absent"
        print("Please enter Present or Absent.")


def main():
    student_count = get_student_count()
    present_count = 0
    absent_count = 0

    for student_number in range(1, student_count + 1):
        status = get_attendance_status(student_number)
        if status == "present":
            present_count += 1
        else:
            absent_count += 1

    attendance_percentage = present_count / student_count * 100

    print("\nAttendance Summary")
    print(f"Present: {present_count}")
    print(f"Absent: {absent_count}")
    print(f"Attendance percentage: {attendance_percentage:.2f}%")


if __name__ == "__main__":
    main()
