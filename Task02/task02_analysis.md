# Q2 – Loops that Count Attempts

## 1. While Loop
The while loop continues until three valid OTP attempts
are completed. Blank entries are skipped and do not count.

## 2. For Loop
The for loop uses range(3) to allow three valid attempts.
The inner while loop skips blank entries.

## 3. Control Statements
- break: Stops the loop when the OTP is correct.
- continue: Skips blank input.
- pass: Acts as a placeholder without performing an operation.
- else: Locks the account when the loop finishes without break.

## 4. Changed Condition
If the security answer is correct, the customer receives
five OTP attempts instead of three.

## 5. Alternative: Recursion
A recursive function can call itself for each valid attempt.
It stops when the OTP is correct or the attempt limit is reached.

## 6. Complexity Analysis
For a attempts:
- Time complexity: O(a)
- Loop auxiliary space: O(1)
- Recursive stack space: O(a)

## 7. Conclusion
Loops are preferable for OTP verification because they use
constant auxiliary space and avoid recursion depth limitations.
