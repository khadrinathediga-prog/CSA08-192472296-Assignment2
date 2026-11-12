
# Q5 - Functions, Parameters and Scope

# 1. Mutable Default Argument Bug
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# 2. Correct Function Using None
def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


# 3. Positional, Keyword and Default Parameters
def customer_order(customer, item, quantity=1):
    return f"{customer} ordered {quantity} {item}(s)"


# 4. Returning Multiple Values
def calculate_bill(amount):
    gst = amount * 0.18
    total = amount + gst
    return total, gst


# 5. Local and Global Scope
college = "SIMATS"


def show_scope():
    local_name = "Khadrinath"
    print("Local variable:", local_name)
    print("Global variable:", college)


# 6. Global Keyword Demonstration
counter = 0


def increase_global():
    global counter
    counter += 1


# 7. Nonlocal Scope Demonstration
def outer_function():
    message = "Original message"

    def inner_function():
        nonlocal message
        message = "Updated using nonlocal"

    inner_function()
    return message


# 8. Closure Alternative
def create_order():
    order = []

    def add(item):
        order.append(item)
        return order.copy()

    return add


# Main Program
print("Q5: FUNCTIONS, PARAMETERS AND SCOPE")
print("=" * 55)

print("\n1. Mutable Default Argument Bug")
print("First call:", add_item_buggy("Tea"))
print("Second call:", add_item_buggy("Vada"))
print("Defaults:", add_item_buggy.__defaults__)

print("\n2. Correct Function")
print("Customer 1:", add_item("Tea"))
print("Customer 2:", add_item("Vada"))
print("Customer 3:", add_item("Coffee"))

print("\n3. Parameters")
print(customer_order("Kushi", "Tea"))
print(customer_order(customer="Rahul", item="Coffee", quantity=2))
print(customer_order("Priya", "Vada", quantity=3))

print("\n4. Multiple Return Values")
total, gst = calculate_bill(1000)
print("GST:", gst)
print("Total:", total)

print("\n5. Local and Global Scope")
show_scope()

print("\n6. Global Keyword")
increase_global()
print("Global counter:", counter)

print("\n7. Nonlocal Scope")
print(outer_function())

print("\n8. Closure Alternative")
customer1 = create_order()
customer2 = create_order()

print("Customer 1:", customer1("Tea"))
print("Customer 1:", customer1("Vada"))
print("Customer 2:", customer2("Coffee"))
