# ============================================================
# 1. CONDITIONAL STATEMENTS
# ============================================================

# if: executes a block when the condition is True.
age = 20

if age >= 18:
    print("You can vote.")


# if / else
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")


# if / elif / else
color = "yellow"

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Unknown color")


# Multiple independent if statements
temperature = 30

if temperature > 20:
    print("Above 20")

if temperature > 25:
    print("Above 25")

if temperature > 35:
    print("Above 35")


# ============================================================
# 2. LOGICAL OPERATORS IN CONDITIONS
# ============================================================

age = 20

if age >= 18 and age <= 60:
    print("Age is in the working-age range.")

if age < 18 or age > 60:
    print("Outside the range.")

if not age < 18:
    print("Age is not below 18.")


# Related concept: chained comparison
if 18 <= age <= 60:
    print("Age is between 18 and 60.")


# ============================================================
# 3. NESTED CONDITIONALS
# ============================================================

username = "admin"
password = "pass"

if username == "admin":
    if password == "pass":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User does not exist")


# A flatter version can sometimes be clearer:
if username == "admin" and password == "pass":
    print("Login successful")


# ============================================================
# 4. TERNARY EXPRESSION
# ============================================================

# Syntax:
# value_if_true if condition else value_if_false

age = 18
status = "Adult" if age >= 18 else "Not Adult"
print(status)

# Ternary expressions are best for simple decisions.
# Complex logic is usually clearer with normal if/else.


# ============================================================
# 5. MATCH / CASE
# ============================================================

# match/case is useful when comparing one value against
# multiple patterns.

color = "green"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Wrong color")


# The _ pattern acts as a catch-all/default case.


# ============================================================
# 6. WHILE LOOP
# ============================================================

# A while loop repeats while its condition remains True.

i = 1

while i <= 5:
    print(i)
    i += 1


# Countdown
i = 5

while i >= 1:
    print(i)
    i -= 1


# Important:
# A loop variable/state must eventually change if the condition
# depends on it, otherwise the loop can become infinite.


# ============================================================
# 7. INFINITE LOOP — EXAMPLE ONLY
# ============================================================

# DO NOT RUN this unless you intentionally want an infinite loop.
#
# while True:
#     print("Prime")


# while True is commonly used when the loop should continue
# until a break condition occurs.


# ============================================================
# 8. BREAK
# ============================================================

# break immediately terminates the nearest enclosing loop.

i = 1

while i <= 10:
    if i % 6 == 0:
        break
    print(i)
    i += 1


# ============================================================
# 9. CONTINUE
# ============================================================

# continue skips the remaining body of the current iteration
# and moves to the next iteration.

i = 0

while i < 10:
    i += 1

    if i % 3 == 0:
        continue

    print(i)


# ============================================================
# 10. FOR LOOP
# ============================================================

# A for loop iterates over items of an iterable.

for number in [10, 20, 30]:
    print(number)


# String iteration
word = "Prime"

for character in word:
    print(character)


# Tuple iteration
numbers = (1, 2, 3)

for number in numbers:
    print(number)


# ============================================================
# 11. MEMBERSHIP OPERATOR: in
# ============================================================

# 'in' checks whether an item exists in an iterable.

word = "Prime"

print("P" in word)       # True
print("z" in word)       # False

if "i" in word:
    print("Letter exists")


# 'not in'
if "x" not in word:
    print("Letter does not exist")


# ============================================================
# 12. COUNTING SOMETHING WITH A FOR LOOP
# ============================================================

word = "artificial intelligence"
vowel_count = 0

for character in word:
    if character in "aeiou":
        vowel_count += 1

print("Vowel count:", vowel_count)


# ============================================================
# 13. NESTED LOOPS
# ============================================================

# A loop inside another loop is a nested loop.

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)


# Example: multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")


# ============================================================
# 14. range()
# ============================================================

# range(stop)
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4


# range(start, stop)
for i in range(1, 6):
    print(i)
# 1, 2, 3, 4, 5


# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
# 1, 3, 5, 7, 9


# Negative step
for i in range(5, 0, -1):
    print(i)
# 5, 4, 3, 2, 1


# range() excludes stop.
print(list(range(1, 6)))


# Related concept:
# range() is a range object, not a list.
r = range(5)
print(type(r))
print(3 in r)


# ============================================================
# 15. PRACTICE — MULTIPLE OF 5
# ============================================================

number = 25

if number % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


# ============================================================
# 16. PRACTICE — ODD OR EVEN
# ============================================================

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 17. PRACTICE — MULTIPLICATION TABLE
# ============================================================

n = 7

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ============================================================
# 18. PRACTICE — ODD NUMBERS USING continue
# ============================================================

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# ============================================================
# 19. FUNCTIONS
# ============================================================

# A function is a reusable block of code that performs a task.

def hello():
    print("Hello from Python!")


# Function call
hello()
hello()


# ============================================================
# 20. FUNCTIONS WITH PARAMETERS
# ============================================================

def add(a, b):
    print(a + b)


# 5 and 10 are arguments.
add(5, 10)


# Parameter vs argument:
# a, b -> parameters
# 5, 10 -> arguments


# ============================================================
# 21. RETURN
# ============================================================

def average(a, b, c):
    return (a + b + c) / 3


result = average(10, 20, 30)
print("Average:", result)


# return sends a value back to the caller.
# It also immediately exits the function.

def check_number(n):
    if n > 0:
        return "Positive"

    return "Zero or Negative"


print(check_number(10))


# ============================================================
# 22. print() VS return
# ============================================================

def add_and_print(a, b):
    print(a + b)


def add_and_return(a, b):
    return a + b


# print() displays a result.
# return makes the result available to the caller.

x = add_and_return(10, 20)
print(x * 2)


# ============================================================
# 23. DEFAULT PARAMETERS
# ============================================================

def greet(name="Guest"):
    print(f"Hello, {name}!")


greet("Parth")
greet()


# Default parameters are used when the caller does not provide
# that argument.


# ============================================================
# 24. MULTIPLE DEFAULT PARAMETERS
# ============================================================

def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(5, 3))


# Rule:
# Parameters with defaults should come after required parameters.
#
# Correct:
# def example(a, b=10):
#     ...
#
# Incorrect:
# def example(a=10, b):
#     ...


# ============================================================
# 25. KEYWORD ARGUMENTS — RELATED CONCEPT
# ============================================================

def student_info(name, age, course):
    print(name, age, course)


# Positional arguments
student_info("Parth", 21, "AI/ML")

# Keyword arguments
student_info(name="Parth", age=21, course="AI/ML")

# Keyword arguments make calls more explicit.


# ============================================================
# 26. BUILT-IN FUNCTIONS
# ============================================================

# Built-in functions are already provided by Python.

print("Hello")
name = "Parth"

# input() is also built-in, but it is kept commented
# so this revision file does not pause for user input.
#
# name = input("Enter name: ")

print(type(name))
print(len(name))
print(range(5))

# Other useful built-ins:
print(abs(-10))
print(max(10, 20, 5))
print(min(10, 20, 5))
print(sum([1, 2, 3, 4, 5]))
print(sorted([5, 2, 8, 1]))


# ============================================================
# 27. LAMBDA FUNCTIONS
# ============================================================

# Syntax:
# lambda parameters: expression

square = lambda x: x ** 2

print(square(5))


# Multiple parameters
add = lambda a, b: a + b
print(add(10, 20))


# Lambda expressions implicitly return the expression's result.
# They are generally useful for short operations.


# ============================================================
# 28. LAMBDA WITH sorted()
# ============================================================

students = [
    ("Parth", 88),
    ("Alex", 95),
    ("John", 76)
]

# Sort by marks
students_sorted = sorted(students, key=lambda student: student[1])

print(students_sorted)


# ============================================================
# 29. enumerate() — RELATED CONCEPT
# ============================================================

# enumerate() gives both index and value.

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)


# Start indexing from another number:
for index, language in enumerate(languages, start=1):
    print(index, language)


# ============================================================
# 30. zip() — RELATED CONCEPT
# ============================================================

names = ["Parth", "Alex", "John"]
marks = [90, 85, 78]

for name, mark in zip(names, marks):
    print(name, mark)


# zip() pairs corresponding elements.


# ============================================================
# 31. pass — RELATED CONTROL STATEMENT
# ============================================================

# pass does nothing. It is useful as a placeholder.

number = 10

if number > 0:
    pass
else:
    print("Negative or zero")


# Unlike continue, pass does NOT skip an iteration.
# It simply performs no operation.


# ============================================================
# 32. FUNCTION DOCSTRINGS — RELATED CONCEPT
# ============================================================

def calculate_square(n):
    """Return the square of n."""
    return n ** 2


print(calculate_square(6))
print(calculate_square.__doc__)


# ============================================================
# 33. FUNCTION SCOPE — RELATED CONCEPT
# ============================================================

global_value = 100

def scope_demo():
    local_value = 50
    print("Inside:", global_value)
    print("Inside:", local_value)


scope_demo()

# local_value exists only inside scope_demo().
# print(local_value) outside the function would raise NameError.


# ============================================================
# 34. *args — RELATED CONCEPT
# ============================================================

# *args collects extra positional arguments into a tuple.

def add_many(*numbers):
    return sum(numbers)


print(add_many(1, 2, 3))
print(add_many(10, 20, 30, 40))


# ============================================================
# 35. **kwargs — RELATED CONCEPT
# ============================================================

# **kwargs collects extra keyword arguments into a dictionary.

def show_details(**details):
    print(details)


show_details(name="Parth", age=21, field="AI/ML")


# ============================================================
# 36. RECURSION — PREVIEW
# ============================================================

# A recursive function calls itself.
# This is a preview because recursion can be studied separately.

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(3)


# ============================================================
# 37. PRACTICE — SUM OF FIRST N NATURAL NUMBERS
# ============================================================

n = 5
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# ============================================================
# 38. PRACTICE — FACTORIAL
# ============================================================

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial:", factorial)


# ============================================================
# 39. PRACTICE — FACTORIAL USING A FUNCTION
# ============================================================

def factorial_of(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial_of(5))


# ============================================================
# 40. PRACTICE — LARGEST OF THREE NUMBERS
# ============================================================

def get_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(get_largest(10, 5, 8))


# A simpler built-in solution:
print(max(10, 5, 8))


# ============================================================
# 41. PRACTICE — COUNT VOWELS
# ============================================================

def count_vowels(word):
    count = 0

    for character in word.lower():
        if character in "aeiou":
            count += 1

    return count


print(count_vowels("Artificial Intelligence"))


# ============================================================
# 42. PRACTICE — PRIME CHECK
# ============================================================

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


print(is_prime(17))
print(is_prime(18))


# ============================================================
# 43. COMMON LOOP PATTERNS
# ============================================================

numbers = [4, 7, 2, 9, 1]

# Sum
total = 0
for number in numbers:
    total += number
print("Sum:", total)

# Count
count = 0
for number in numbers:
    if number > 5:
        count += 1
print("Numbers > 5:", count)

# Search
target = 9
found = False

for number in numbers:
    if number == target:
        found = True
        break

print("Found:", found)


# ============================================================
# 44. LOOP ELSE — RELATED CONCEPT
# ============================================================

# The else block of a loop executes if the loop finishes
# normally (i.e., without break).

for number in [1, 3, 5, 7]:
    if number % 2 == 0:
        print("Even found")
        break
else:
    print("No even number found")
