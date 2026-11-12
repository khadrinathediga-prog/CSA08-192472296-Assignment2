
# Q2 - Loops that Count Attempts
# OTP Verification at a Bank Kiosk

CORRECT_OTP = "1234"
CORRECT_SECURITY_ANSWER = "blue"


# Method 1: while loop
def verify_while():
    attempts = 0

    print("\n--- WHILE LOOP ---")

    while attempts < 3:
        otp = input("Enter OTP (blank to skip): ").strip()

        if otp == "":
            print("Blank entry does not count.")
            continue

        attempts += 1

        if otp == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Incorrect OTP.")

    else:
        print("Account locked for 30 minutes.")


# Method 2: for loop
def verify_for():
    print("\n--- FOR LOOP ---")

    for attempt in range(3):
        while True:
            otp = input("Enter OTP (blank to skip): ").strip()

            if otp == "":
                print("Blank entry does not count.")
                continue

            break

        if otp == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Incorrect OTP.")

    else:
        print("Account locked for 30 minutes.")


# Method 3: Two extra attempts after security answer
def verify_with_security():
    print("\n--- SECURITY QUESTION ---")

    answer = input("Favourite colour: ").strip().lower()

    max_attempts = 5 if answer == CORRECT_SECURITY_ANSWER else 3

    print("You have", max_attempts, "OTP attempts.")

    for attempt in range(max_attempts):
        while True:
            otp = input("Enter OTP (blank to skip): ").strip()

            if otp == "":
                print("Blank entry does not count.")
                continue

            break

        if otp == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Incorrect OTP.")

    else:
        print("Account locked for 30 minutes.")


# Demonstration of pass
def demonstrate_pass():
    print("\n--- PASS DEMONSTRATION ---")

    for number in range(3):
        if number == 1:
            pass
        print("Number:", number)


print("BANK KIOSK OTP SYSTEM")
print("Demo OTP: 1234")

verify_while()
verify_for()
verify_with_security()
demonstrate_pass()
