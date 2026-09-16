# ============================================================
# 1. OUTPUT — print()
# ============================================================

# Basic output
print("Hello, World!")
print(3.14)
print(2 + 3)

# Multiple values in one print statement
print("Hello", "from AI/ML Journey")

# print() with sep
print("2026", "09", "16", sep="-")

# print() with end
print("Hello", end=" ")
print("Python")

# Escape sequences
print("Line 1\nLine 2")
print("Name:\tParth")
print("He said, \"Python is easy to start.\"")
print("C:\\Users\\Parth\\AI-ML")

# Useful related concept: f-strings
name = "Parth"
age = 21
print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 2. PYTHON CHARACTER SET
# ============================================================

# Python source code can contain:
# - Letters: a-z, A-Z
# - Digits: 0-9
# - Special symbols
# - Whitespace
# - Escape characters
# - Unicode characters

print("Python 3")
print("AI/ML 🤖")
print("₹1000")


# ============================================================
# 3. COMMENTS
# ============================================================

# Single-line comment

"""
This is a multi-line string.
It is often used like a multi-line comment,
although technically it is a string literal.
"""


# ============================================================
# 4. VARIABLES
# ============================================================

# A variable is a name referring to a value/object.
name = "Parth"
age = 21
cgpa = 8.63
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)

# Python is dynamically typed:
# We do not explicitly declare the type of a variable.
value = 100
print(type(value))

value = "one hundred"
print(type(value))

# Python is case-sensitive
age = 21
Age = 25
print(age)
print(Age)

# Variables can be reassigned
score = 50
score = 75
print(score)


# ============================================================
# 5. IDENTIFIER / VARIABLE NAMING RULES
# ============================================================

# Valid:
student_name = "Parth"
_marks = 90
marks2 = 95
student2_name = "Alex"

# Invalid examples — uncomment one at a time to see SyntaxError:
# 2name = "Bob"       # Cannot start with a digit
# student-name = ""  # '-' is treated as subtraction
# class = 10         # 'class' is a Python keyword

# Good naming practice: use descriptive snake_case names.
total_marks = 450
average_marks = total_marks / 5


# ============================================================
# 6. PYTHON KEYWORDS
# ============================================================

# Keywords are reserved words with predefined meaning.
# Examples:
# if, else, elif, for, while, class, def, return,
# in, is, True, False, None, and, or, not

# You can inspect the current Python version's keywords:
import keyword

print(keyword.kwlist)
print(keyword.iskeyword("class"))   # True
print(keyword.iskeyword("student")) # False


# ============================================================
# 7. INDENTATION
# ============================================================

# Indentation defines code blocks in Python.
# The common style is 4 spaces per indentation level.

temperature = 30

if temperature > 25:
    print("It is warm.")
    print("Stay hydrated.")

# Incorrect indentation would raise IndentationError.


# ============================================================
# 8. BUILT-IN DATA TYPES
# ============================================================

integer_value = 10
float_value = 3.14
string_value = "Artificial Intelligence"
boolean_value = True
none_value = None

print(type(integer_value))  # int
print(type(float_value))    # float
print(type(string_value))   # str
print(type(boolean_value))  # bool
print(type(none_value))     # NoneType

# Related types that will appear later in the journey:
complex_value = 2 + 3j
list_value = [10, 20, 30]
tuple_value = (10, 20, 30)
set_value = {10, 20, 30}
dict_value = {"name": "Parth", "age": 21}

print(type(complex_value))
print(type(list_value))
print(type(tuple_value))
print(type(set_value))
print(type(dict_value))


# ============================================================
# 9. TYPE CHECKING — type() vs isinstance()
# ============================================================

x = 100

print(type(x))
print(isinstance(x, int))
print(isinstance(x, (int, float)))

# isinstance() is generally more useful when checking
# whether a value belongs to a type hierarchy.


# ============================================================
# 10. TYPE CONVERSION / IMPLICIT CONVERSION
# ============================================================

# Python can automatically convert a value in some expressions.
a = 5          # int
b = 3.0        # float

result = a + b
print(result)
print(type(result))  # float

# int + float -> float


# ============================================================
# 11. EXPLICIT TYPE CASTING
# ============================================================

x = 10

y = float(x)
z = str(x)
w = bool(x)

print(y, type(y))
print(z, type(z))
print(w, type(w))

# Common conversion functions:
# int(), float(), str(), bool(), list(), tuple(), set()


# ============================================================
# 12. TYPE CASTING — IMPORTANT BEHAVIOR
# ============================================================

print(int(3.99))       # 3 — decimal part is discarded
print(float(10))       # 10.0
print(str(123))        # "123"

# String -> number
number = int("25")
decimal = float("3.14")
print(number, decimal)

# Be careful:
# int("3.14") would raise ValueError.
# Use int(float("3.14")) if that behavior is actually desired.

# bool() follows truthiness rules:
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False
print(bool("Python"))  # True


# ============================================================
# 13. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # True division
print(a % b)   # Modulus / remainder
print(a ** b)  # Exponentiation

# Related arithmetic operator explicitly appearing in
# Python's precedence rules:
print(a // b)  # Floor division

# / always returns a float in normal Python 3 arithmetic.
print(10 / 2)   # 5.0
print(10 // 2)  # 5


# ============================================================
# 14. RELATIONAL / COMPARISON OPERATORS
# ============================================================

a = 10
b = 20

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Comparisons produce boolean values.
comparison_result = a < b
print(comparison_result, type(comparison_result))


# ============================================================
# 15. CHAINED COMPARISONS — RELATED CONCEPT
# ============================================================

marks = 85

# Instead of:
print(marks >= 0 and marks <= 100)

# Python also allows:
print(0 <= marks <= 100)


# ============================================================
# 16. ASSIGNMENT OPERATORS
# ============================================================

x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0

x %= 4
print(x)  # 2.0

x **= 3
print(x)  # 8.0

# Related operator:
x //= 3
print(x)


# ============================================================
# 17. LOGICAL OPERATORS
# ============================================================

x = 10
y = 20
z = 5

# AND: True only when both conditions are true
print(x < y and z < x)

# OR: True when at least one condition is true
print(x > y or z < y)

# NOT: reverses truth value
print(not (x > y))

# Truth tables:
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(False or False)   # False
print(not True)         # False


# ============================================================
# 18. SHORT-CIRCUIT EVALUATION — RELATED CONCEPT
# ============================================================

# 'and' and 'or' can stop evaluating once the result is known.

# False and ... never needs to evaluate the right side.
result = False and (10 / 0)
print(result)

# True or ... never needs to evaluate the right side.
result = True or (10 / 0)
print(result)

# This is useful for safe conditional expressions.


# ============================================================
# 19. UNARY OPERATORS
# ============================================================

x = 5

print(+x)  # Unary plus
print(-x)  # Unary minus
print(not (x > 0))

# Unary operators operate on one operand.


# ============================================================
# 20. BITWISE OPERATORS — RELATED TO THE PRECEDENCE LIST
# ============================================================

# These operate on the binary representation of integers.

a = 5   # 0101
b = 3   # 0011

print(a & b)   # Bitwise AND -> 0001 -> 1
print(a | b)   # Bitwise OR  -> 0111 -> 7
print(a ^ b)   # Bitwise XOR -> 0110 -> 6
print(~a)      # Bitwise NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift

# Bitwise operators are different from logical operators:
# &  -> bitwise AND
# and -> logical AND


# ============================================================
# 21. OPERATOR PRECEDENCE
# ============================================================

# A simplified order relevant to this lecture:
#
# 1. Parentheses                 ()
# 2. Exponentiation              **
# 3. Unary +, -, ~
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. Comparisons                < <= > >= == !=
# 11. not
# 12. and
# 13. or
# 14. Assignment                 =, +=, -=, ...

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
result3 = 2 ** 3 * 2
result4 = 10 + 20 / 5

print(result1)  # 14
print(result2)  # 20
print(result3)  # 16
print(result4)  # 14.0

# Best practice:
# Use parentheses when they make your intended logic clearer.


# ============================================================
# 22. STRINGS — RELATED TO OUTPUT AND INPUT
# ============================================================

single_quoted = 'Python'
double_quoted = "Python"
triple_quoted = """Python
for
AI/ML"""

print(single_quoted)
print(double_quoted)
print(triple_quoted)

# Basic string operations
first_name = "Parth"
last_name = "Katariya"

full_name = first_name + " " + last_name
print(full_name)

print("AI" * 3)

# String indexing and slicing (important later)
word = "Python"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[:3])
print(word[3:])
print(word[::-1])


# ============================================================
# 23. INPUT — input()
# ============================================================

# input() always returns a string.

# Uncomment to interactively test:
# name = input("Enter your name: ")
# print(name)
# print(type(name))

# Numeric input requires explicit conversion:
# age = int(input("Enter your age: "))
# print(age + 1)


# ============================================================
# 24. INPUT + TYPE CONVERSION
# ============================================================

# Example:
#
# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# print(first_number + second_number)

# Decimal input:
#
# price = float(input("Enter price: "))
# print(price)


# ============================================================
# 25. SAFE NUMERIC INPUT — RELATED CONCEPT
# ============================================================

# int(input(...)) raises ValueError if the user enters
# something that cannot be interpreted as an integer.
#
# A later lesson will cover exception handling in detail.
# For now, this is the basic idea:
#
# try:
#     age = int(input("Enter age: "))
#     print(age)
# except ValueError:
#     print("Please enter a valid integer.")


# ============================================================
# 26. PRACTICE: AVERAGE OF TWO NUMBERS
# ============================================================

a = 5
b = 10

average = (a + b) / 2
print("Average:", average)


# ============================================================
# 27. MINI PRACTICE: STUDENT SCORE SUMMARY
# ============================================================

student_name = "Parth"
maths = 85
python = 92
ml = 88

total = maths + python + ml
average = total / 3

print("\n--- Student Score Summary ---")
print("Name:", student_name)
print("Total:", total)
print("Average:", average)
print(f"Average formatted: {average:.2f}")


# ============================================================
# 28. MINI PRACTICE: BASIC CALCULATOR
# ============================================================

num1 = 20
num2 = 6

print("\n--- Calculator ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Power:", num1 ** 2)
