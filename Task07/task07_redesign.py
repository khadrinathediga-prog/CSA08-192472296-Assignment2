
# Q7 - Diagnose, Redesign and Validate
# Original: Naive Recursion
# Redesigned: Memoisation

from functools import lru_cache
import time


# ORIGINAL SOLUTION
original_calls = 0

def ways_original(n):
    global original_calls
    original_calls += 1

    if n <= 1:
        return 1

    return ways_original(n - 1) + ways_original(n - 2)


# REDESIGNED SOLUTION
redesigned_calls = 0

@lru_cache(maxsize=None)
def ways_redesigned(n):
    global redesigned_calls
    redesigned_calls += 1

    if n <= 1:
        return 1

    return ways_redesigned(n - 1) + ways_redesigned(n - 2)


# BENCHMARK
print("Q7: DIAGNOSE, REDESIGN AND VALIDATE")
print("=" * 65)

print("\n1. Original vs Redesigned Performance")

for n in [10, 20, 25, 30]:

    # Original version
    original_calls = 0

    start = time.perf_counter()
    original_result = ways_original(n)
    original_time = time.perf_counter() - start

    original_count = original_calls

    # Redesigned version
    ways_redesigned.cache_clear()
    redesigned_calls = 0

    start = time.perf_counter()
    redesigned_result = ways_redesigned(n)
    redesigned_time = time.perf_counter() - start

    redesigned_count = redesigned_calls

    print(f"\nInput n = {n}")
    print("Original result:", original_result)
    print("Redesigned result:", redesigned_result)
    print("Results match:", original_result == redesigned_result)

    print("Original calls:", original_count)
    print("Redesigned calls:", redesigned_count)

    print(f"Original time: {original_time:.6f} seconds")
    print(f"Redesigned time: {redesigned_time:.6f} seconds")


# DESIGN OBJECTIVE
print("\n2. DESIGN OBJECTIVE")
print("Reduce repeated function calls while maintaining")
print("the same output for every input.")


# FINAL VALIDATION
print("\n3. FINAL VALIDATION")

for n in [10, 20, 25, 30]:
    ways_redesigned.cache_clear()
    print(f"n={n}: {ways_redesigned(n)}")


# COMPLEXITY COMPARISON
print("\n4. COMPLEXITY ANALYSIS")
print("Original: O(2^n) time, O(n) stack space")
print("Redesigned: O(n) time, O(n) cache and stack space")

print("\nConclusion:")
print("Memoisation avoids repeated calculations and")
print("significantly reduces the number of function calls.")
