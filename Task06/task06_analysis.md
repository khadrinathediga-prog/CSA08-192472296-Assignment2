
# Q6 – Recursion and Its Limits

## 1. Problem
The number of ways to climb n steps using either 1 or 2 steps
is calculated using recursion.

## 2. Base and Recursive Cases
Base case:
If n <= 1, return 1.

Recursive case:
ways(n) = ways(n-1) + ways(n-2)

## 3. Correctness Check

| Steps | Number of Ways |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 5 |
| 5 | 8 |
| 6 | 13 |

## 4. Function Call Comparison

| n | Naive Calls | Memoised Calls |
|---|---:|---:|
| 10 | 177 | 11 |
| 20 | 21891 | 21 |
| 25 | 242785 | 26 |
| 30 | 2692537 | 31 |

## 5. Observation
Naive recursion repeats the same calculations many times.
Memoisation stores previously calculated results and avoids
repeating those calculations.

## 6. Recursion Limit
The Python recursion limit was 1000.
The memoised recursive function raised RecursionError for
1000 steps because the recursive call depth exceeded the limit.

The iterative solution successfully calculated the result
for 1000 steps.

## 7. Alternative: Iteration
The iterative approach stores only the previous two values.
It avoids recursive function calls and cache storage.

## 8. Complexity Analysis
- Naive recursion: O(2^n) time, O(n) stack space.
- Memoisation: O(n) time, O(n) cache and stack space.
- Iteration: O(n) time, O(1) auxiliary space.

## 9. Conclusion
Memoisation greatly reduces repeated calculations.
Iteration is the preferred deployment solution for 1000 steps
because it avoids recursion depth limitations and uses
constant auxiliary space.
