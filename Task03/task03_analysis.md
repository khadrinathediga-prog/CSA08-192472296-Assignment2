# Q3 – Vehicle Registration Number Validator

## 1. Normalisation
Spaces and hyphens are removed using replace().
The registration number is converted to uppercase using upper().

## 2. Validation
The program checks:
- State code: 2 letters
- District code: 2 digits
- Series: 1 or 2 letters
- Registration number: 4 digits

Only valid registration numbers are accepted.

## 3. String Slicing
- reg[-4:] returns the last four characters.
- reg[4:-4] returns the middle series characters.
- Slicing works for both 9-character and 10-character numbers.

## 4. String Immutability
Strings cannot be modified after creation.
upper() returns a new uppercase string without changing the original.

## 5. Alternative: Regular Expressions
The validation can also use re.fullmatch().

Example:
re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg)

## 6. Complexity Analysis
Let L be the registration number length.

- Time complexity: O(L)
- Space complexity: O(L) for the normalized string.
- Regular expressions also take O(L) time for this fixed pattern.

## 7. Conclusion
String methods and slicing provide a clear way to normalize,
validate and format vehicle registration numbers without regex.