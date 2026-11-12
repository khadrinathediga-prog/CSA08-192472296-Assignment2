
# Q4 – Building Long Text: + vs join()

## 1. Prediction
The join() method is expected to be faster because it combines
all strings in one operation instead of repeatedly creating
new strings.

## 2. Implementations
Three methods were tested:
- Repeated += inside a loop.
- List of strings followed by join().
- f-string for each line followed by join().

## 3. Benchmark Results

| Lines | += Average (s) | join Average (s) | f-string Average (s) |
|---|---:|---:|---:|
| 1,000 | 0.000090 | 0.000016 | 0.000065 |
| 10,000 | 0.000855 | 0.000150 | 0.000641 |
| 200,000 | 0.023174 | 0.003213 | 0.013532 |

Each method was executed three times and the average was calculated.

## 4. Observation
All three methods generated identical output.
join() was the fastest method in all three experiments.

At 200,000 lines, join() took 0.003213 seconds,
while repeated += took 0.023174 seconds.

## 5. String Immutability
Python strings are immutable. Repeated concatenation may create
new string objects and copy existing characters.
join() combines the strings efficiently in one operation.

## 6. Alternative Concepts
- File writing: Writes each line directly to a file.
- io.StringIO: Builds text using an in-memory file-like buffer.

These approaches can reduce the need to retain a separate
list of all strings.

## 7. Complexity Analysis
Let n be the number of lines and L be the total output length.

- join(): O(L) time and O(L) output space.
- Repeated +=: Can require O(nL) character copying in the
  worst case, depending on implementation.
- File writing: O(L) total time, with low memory usage.
- StringIO: O(L) time and O(L) memory.

## 8. Conclusion
join() is the recommended method for building large strings
because it was consistently faster in the experiments.
