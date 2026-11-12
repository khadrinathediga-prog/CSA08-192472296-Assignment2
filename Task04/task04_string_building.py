
# Q4 - Building Long Text: + vs join()
import time


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return ";".join(parts) + ";"


def build_fstring(parts):
    lines = [f"{p};" for p in parts]
    return "".join(lines)


def measure(function, items):
    times = []

    for _ in range(3):
        start = time.perf_counter()
        result = function(items)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    return sum(times) / len(times), result


print("Q4: STRING BUILDING PERFORMANCE")
print("=" * 65)

for size in [1000, 10000, 200000]:
    items = [f"Item{i}:Rs{i % 50}" for i in range(size)]

    plus_time, a = measure(build_plus, items)
    join_time, b = measure(build_join, items)
    fstring_time, c = measure(build_fstring, items)

    print(f"\nNumber of lines: {size}")
    print("All outputs same:", a == b == c)
    print(f"+= average:       {plus_time:.6f} seconds")
    print(f"join average:     {join_time:.6f} seconds")
    print(f"f-string average: {fstring_time:.6f} seconds")
    print("Output length:", len(b))


# Complete the assignment's 200,000-item example
items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

start = time.perf_counter()
a = build_plus(items)
t_plus = time.perf_counter() - start

start = time.perf_counter()
b = build_join(items)
t_join = time.perf_counter() - start

print("\nASSIGNMENT COMPLETE-CODE TEST")
print("Same text:", a == b, "| length:", len(b))
print(f"+= time: {t_plus:.4f} s")
print(f"join time: {t_join:.4f} s")
