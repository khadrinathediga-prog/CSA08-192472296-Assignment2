
# Q5 – Functions, Parameters and Scope

## 1. Mutable Default Argument Bug
A default list is created only once when the function is defined.
Therefore, items from previous calls remain in the same list.

## 2. Corrected Function
Using order=None creates a new empty list for every customer
when no order is supplied.

## 3. Parameter Types
- Positional: Values passed in parameter order.
- Keyword: Values passed using parameter names.
- Default: A predefined value used when an argument is omitted.

## 4. Multiple Return Values
The calculate_bill() function returns both GST and total.
Python allows multiple values to be returned as a tuple.

## 5. Variable Scope
- Local: Defined inside a function.
- Global: Defined outside a function.
- Nonlocal: Refers to a variable in an enclosing function.

The global keyword allows modification of a global variable.
The nonlocal keyword allows modification of an enclosing variable.

## 6. Independent Customer Orders
Three customers were tested.
Each customer received a separate order list.

## 7. Alternative: Closure
A closure stores the order list inside an enclosing function.
Each call to create_order() creates an independent order.

## 8. Complexity Analysis
For adding one item:
- Time complexity: O(1) amortized.
- Space complexity: O(n) for an order containing n items.

Both None-default and closure approaches use O(n) storage
for each customer's order.

## 9. Conclusion
Using None as a default argument prevents shared mutable state.
Closures are another way to maintain independent customer orders.
