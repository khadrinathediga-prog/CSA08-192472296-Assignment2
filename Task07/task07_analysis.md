
# Q7 – Diagnose, Redesign and Validate

## A. Diagnose the Bottleneck

The Q6 naive recursive program repeatedly calculates
the same subproblems.

At n = 30, it makes 2,692,537 function calls.
This repeated work increases execution time significantly.

## B. Design Objective

Reduce the number of function calls and execution time
while producing exactly the same result.

## C. Revised Solution

Memoisation using functools.lru_cache was implemented.

Previously calculated results are stored in a cache.
When the same input occurs again, the stored result is reused.

Extra memory is required for the cache.

## D. Prediction

Memoisation is expected to reduce repeated function calls,
execution time and unnecessary calculations.

## E. Experimental Results

| n | Original Calls | Redesigned Calls | Original Time (s) | Redesigned Time (s) |
|---|---:|---:|---:|---:|
| 10 | 177 | 11 | 0.000018 | 0.000005 |
| 20 | 21891 | 21 | 0.002025 | 0.000006 |
| 25 | 242785 | 26 | 0.022832 | 0.000012 |
| 30 | 2692537 | 31 | 0.254516 | 0.000020 |

All original and redesigned results matched.

## F. Evaluation

At n = 30, function calls decreased from 2,692,537
to only 31.

Execution time decreased from 0.254516 seconds
to 0.000020 seconds in this experiment.

The redesign achieved the objective.

## G. Complexity Analysis

Original:
- Time: O(2^n)
- Space: O(n) recursion stack

Redesigned:
- Time: O(n)
- Space: O(n) cache and recursion stack

The redesigned method uses additional memory for caching,
but avoids repeated calculations.

## H. Final Conclusion

Memoisation significantly improves the recursive solution.
It is especially useful when the same subproblems occur repeatedly.
For very large inputs, an iterative solution may still be preferable
because it avoids recursion depth limitations.
