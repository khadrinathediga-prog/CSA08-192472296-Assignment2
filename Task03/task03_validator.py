
# Q3 - Vehicle Registration Number Validator

def normalise(text):
    """Remove spaces and hyphens and convert to uppercase."""
    return text.replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    """Validate Indian vehicle registration format."""

    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (
        len(state) == 2 and state.isalpha()
        and len(district) == 2 and district.isdigit()
        and len(series) in (1, 2) and series.isalpha()
        and len(number) == 4 and number.isdigit()
    )


def format_receipt(reg):
    """Format a valid registration number for receipt printing."""
    if not is_valid(reg):
        return "INVALID"

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return f"{state} {district} {series} {number}"


# Test inputs
vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "MH 12 CD 5678",
    "AP-39-EF-9876"
]

print("VEHICLE REGISTRATION VALIDATOR")
print("-" * 60)

for raw in vehicles:
    reg = normalise(raw)

    if is_valid(reg):
        print(f"{raw:18} -> {reg:11} VALID")
        print("Receipt:", format_receipt(reg))
    else:
        print(f"{raw:18} -> {reg:11} INVALID")


# String slicing demonstration
print("\nSTRING SLICING DEMONSTRATION")

for value in ["TN09AB1234", "TN09M1234"]:
    print("\nRegistration:", value)
    print("Last four characters:", value[-4:])
    print("Middle characters:", value[4:-4])


# String immutability demonstration
print("\nSTRING IMMUTABILITY")

text = "tn09ab1234"
upper_text = text.upper()

print("Original:", text)
print("Uppercase:", upper_text)
print("Original remains unchanged:", text)
