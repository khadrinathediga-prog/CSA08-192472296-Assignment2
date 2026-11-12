
# Q6 - Recursion and Its Limits
from functools import lru_cache
import sys
import time


# Count calls for naive recursion
naive_calls = 0

def ways_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Count calls for memoised recursion
memo_calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Iterative solution
def ways_iterative(n):
    if n <= 1:
        return 1

    previous, current = 1, 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


# 1. Correctness check
print("Q6: TEMPLE STAIRS")
print("=" * 60)

print("\n1. Correctness Check")

for n in range(1, 7):
    print(f"Steps: {n}, Ways: {ways_iterative(n)}")


# 2. Naive and memoised call counts
print("\n2. Function Call Comparison")

for n in [10, 20, 25, 30]:
    naive_calls = 0
    result_naive = ways_naive(n)
    naive_count = naive_calls

    ways_memo.cache_clear()
    memo_calls = 0
    result_memo = ways_memo(n)
    memo_count = memo_calls

    print(f"\nn = {n}")
    print("Naive result:", result_naive)
    print("Naive calls:", naive_count)
    print("Memo result:", result_memo)
    print("Memo calls:", memo_count)


# 3. Call tree for n = 5
print("\n3. Call Tree for n = 5")
print("""
ways(5)
├── ways(4)
│   ├── ways(3)
│   │   ├── ways(2)
│   │   └── ways(1)
│   └── ways(2)
└── ways(3)
    ├── ways(2)
    └── ways(1)
""")


# 4. Recursion limit investigation
print("4. Recursion Limit")
print("Current recursion limit:", sys.getrecursionlimit())

ways_memo.cache_clear()

try:
    print("Memoised ways(1000):", ways_memo(1000))
except RecursionError:
    print("RecursionError occurred at 1000 steps.")


# 5. Iterative solution for 1000 steps
print("\n5. Iterative Solution for 1000 Steps")

start = time.perf_counter()
result = ways_iterative(1000)
elapsed = time.perf_counter() - start

print("Ways for 1000 steps:", result)
print(f"Iterative time: {elapsed:.6f} seconds")


# 6. Complexity comparison
print("\n6. Complexity Analysis")
print("Naive recursion: O(2^n) time, O(n) stack space")
print("Memoisation: O(n) time, O(n) cache and stack space")
print("Iteration: O(n) time, O(1) auxiliary space")
