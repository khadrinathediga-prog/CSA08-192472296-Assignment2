# Q1 – Decisions with Many Boundaries

## 1. Prediction
Eight households were selected before execution.
The boundary values 100, 101, 200 and 201 were included.

## 2. Observation
Separate if statements can execute multiple conditions.
For H1 (100 units), both Full subsidy and Partial subsidy
were returned.

The if-elif-else structure executes only one matching branch,
so it returns exactly one decision.

## 3. Design Decision
Combined Boolean conditions with if-elif-else were selected.
This makes the eligibility rules clear and avoids overlapping
subsidy decisions.

## 4. Alternative: match-case
A match-case implementation can use guards to check the
consumption units, ration card and age.

## 5. Complexity Analysis
For k eligibility conditions:
- Time complexity: O(k) in the worst case.
- Space complexity: O(1), excluding the output.

Both if-elif-else and match-case use constant auxiliary space.

## 6. Conclusion
The if-elif-else approach is more suitable because it ensures
exactly one subsidy decision for each household.
