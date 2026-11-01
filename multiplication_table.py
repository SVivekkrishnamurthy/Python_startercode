"""Print the multiplication table for a number from 1 to 10."""


def main():
    number = int(input("Enter a number: "))

    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


if __name__ == "__main__":
    main()
