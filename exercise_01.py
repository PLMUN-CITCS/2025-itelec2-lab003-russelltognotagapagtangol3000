# Russell Togno
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

# Declaring variables with numeric literals
count = 10                   # 'count' is assigned 10 (integer literal)
Count = 15                   # 'Count' (different from 'count') is assigned 15
total_count = 20             # Another integer literal assignment
decimal_value = 3.14         # 'decimal_value' is assigned 3.14 (float literal)

# Declaring a variable with a string literal
message = "Hello, Python!"   # String literal

# Declaring a variable with a boolean literal
is_active = True             # Boolean literal

# Declaring a variable with the None literal
result = None                # None literal represents the absence of a value

# Displaying the variable values
print("Integer (count):", count)
print("Integer (Count):", Count)  # Demonstrates case sensitivity
print("Integer (total_count):", total_count)
print("Decimal:", decimal_value)
print("Text:", message)
print("Boolean:", is_active)
print("None Value:", result)

# Inline arithmetic with f-strings
num1 = 5
num2 = 3
print(f"Sum: {num1 + num2:.2f}")  # The result (8.00) is formatted to 2 decimal places
