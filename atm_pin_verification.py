"""Verify an ATM PIN and block the card after three incorrect attempts."""


DEMO_PIN = "1234"
MAX_PIN_ATTEMPTS = 3


def main():
    attempts = 0

    while attempts < MAX_PIN_ATTEMPTS:
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == DEMO_PIN:
            print("PIN verified. Your card is ready to use.")
            return

        attempts += 1
        remaining_attempts = MAX_PIN_ATTEMPTS - attempts
        if remaining_attempts:
            print(f"Incorrect PIN. You have {remaining_attempts} attempt(s) left.")

    print("Three incorrect attempts. Your card is blocked.")


if __name__ == "__main__":
    main()
