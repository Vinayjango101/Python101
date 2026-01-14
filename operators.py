# operators_demo.py
# This Python script demonstrates the usage of all types of operators in Python
# Each section is well-commented for educational purposes

# ---------------------------
# 1. Arithmetic Operators
# ---------------------------
a = 10
b = 3

print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division (float result)
print(f"a // b = {a // b}")  # Floor division (integer division)
print(f"a % b = {a % b}")  # Modulus (remainder)
print(f"a ** b = {a ** b}")  # Exponentiation

# ---------------------------
# 2. Assignment Operators
# ---------------------------
c = 5
print("\nAssignment Operators:")
c += 2  # Equivalent to c = c + 2
print(f"c += 2 -> {c}")
c -= 1  # Equivalent to c = c - 1
print(f"c -= 1 -> {c}")
c *= 3  # Equivalent to c = c * 3
print(f"c *= 3 -> {c}")
c /= 2  # Equivalent to c = c / 2
print(f"c /= 2 -> {c}")
c %= 4  # Equivalent to c = c % 4
print(f"c %= 4 -> {c}")
c **= 2  # Equivalent to c = c ** 2
print(f"c **= 2 -> {c}")
c //= 3  # Equivalent to c = c // 3
print(f"c //= 3 -> {c}")

# ---------------------------
# 3. Comparison Operators
# ---------------------------
x = 7
y = 10

print("\nComparison Operators:")
print(f"x == y -> {x == y}")  # Equal
print(f"x != y -> {x != y}")  # Not equal
print(f"x > y -> {x > y}")    # Greater than
print(f"x < y -> {x < y}")    # Less than
print(f"x >= y -> {x >= y}")  # Greater than or equal
print(f"x <= y -> {x <= y}")  # Less than or equal

# ---------------------------
# 4. Logical Operators
# ---------------------------
p = True
q = False

print("\nLogical Operators:")
print(f"p and q -> {p and q}")  # Logical AND
print(f"p or q -> {p or q}")    # Logical OR
print(f"not p -> {not p}")      # Logical NOT

# ---------------------------
# 5. Bitwise Operators
# ---------------------------
m = 5  # binary: 0101
n = 3  # binary: 0011

print("\nBitwise Operators:")
print(f"m & n -> {m & n}")  # AND
print(f"m | n -> {m | n}")  # OR
print(f"m ^ n -> {m ^ n}")  # XOR
print(f"~m -> {~m}")        # NOT
print(f"m << 1 -> {m << 1}")  # Left shift
print(f"m >> 1 -> {m >> 1}")  # Right shift

# ---------------------------
# 6. Membership Operators
# ---------------------------
my_list = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print(f"3 in my_list -> {3 in my_list}")     # True if 3 is in the list
print(f"6 not in my_list -> {6 not in my_list}") # True if 6 is NOT in the list

# ---------------------------
# 7. Identity Operators
# ---------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators:")
print(f"a is b -> {a is b}")   # True because b points to the same object as a
print(f"a is c -> {a is c}")   # False because c is a different object, even if contents are same
print(f"a is not c -> {a is not c}") # True

# ---------------------------
# End of Operators Demo
# ---------------------------
