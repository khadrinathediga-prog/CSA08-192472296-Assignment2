
# Q1 - Decisions with Many Boundaries
# State Electricity Subsidy Eligibility

households = [
    ("H1", 100, True, 30),
    ("H2", 101, True, 25),
    ("H3", 101, False, 40),
    ("H4", 200, True, 50),
    ("H5", 200, False, 35),
    ("H6", 201, False, 85),
    ("H7", 201, True, 45),
    ("H8", 80, False, 82)
]


# Method 1: Separate if statements
def separate_if(units, ration_card, age):
    results = []

    if units <= 100:
        results.append("Full subsidy")

    # Intentional overlapping condition to demonstrate the bug
    if units <= 200 and ration_card:
        results.append("Partial subsidy")

    if units > 200 and age > 80:
        results.append("Special subsidy")

    if not results:
        results.append("No subsidy")

    return results


# Method 2: if-elif-else
def elif_decision(units, ration_card, age):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200 and ration_card:
        return "Partial subsidy"
    elif units > 200 and age > 80:
        return "Special subsidy"
    else:
        return "No subsidy"


# Method 3: match-case
def match_decision(units, ration_card, age):
    match units:
        case u if u <= 100:
            return "Full subsidy"
        case u if 101 <= u <= 200 and ration_card:
            return "Partial subsidy"
        case u if u > 200 and age > 80:
            return "Special subsidy"
        case _:
            return "No subsidy"


# Display results
print("Q1: ELECTRICITY SUBSIDY ELIGIBILITY")
print("-" * 65)

for name, units, ration, age in households:
    print(f"{name}: Units={units}, Ration={ration}, Age={age}")
    print("Separate if:", separate_if(units, ration, age))
    print("If-elif-else:", elif_decision(units, ration, age))
    print("Match-case:", match_decision(units, ration, age))
    print()
