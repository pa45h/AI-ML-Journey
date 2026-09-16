# ============================================================
# 1. STRINGS
# ============================================================

# A string is a sequence of characters enclosed in quotes.
str1 = "hello world"
str2 = "Prime"

print(str1)
print(str2)

# Single, double and triple quotes
single = 'Python'
double = "Python"
multi_line = """Python
for
AI/ML"""

print(single)
print(double)
print(multi_line)


# ============================================================
# 2. STRING IMMUTABILITY
# ============================================================

# Strings are immutable: their characters cannot be changed
# directly after the string has been created.

word = "Python"

# This would raise TypeError:
# word[0] = "J"

# Instead, create a new string:
word = "J" + word[1:]
print(word)


# ============================================================
# 3. len() — STRING LENGTH
# ============================================================

word = "Prime"

print(len(word))  # 5

# Spaces also count as characters.
text = "Hello World"
print(len(text))


# ============================================================
# 4. STRING CONCATENATION
# ============================================================

str1 = "Apna"
str2 = "College"

word = str1 + " " + str2
print(word)

# Strings can be repeated with *
print("AI " * 3)


# ============================================================
# 5. LOOPING OVER STRINGS
# ============================================================

s = "Python"

for ch in s:
    print(ch)


# ============================================================
# 6. STRING INDEXING
# ============================================================

# Python uses zero-based indexing.
s = "Python"

print(s[0])   # P
print(s[3])   # h
print(s[-1])  # n
print(s[-2])  # o

# Index positions:
#
#   P  y  t  h  o  n
#   0  1  2  3  4  5
#  -6 -5 -4 -3 -2 -1


# ============================================================
# 7. STRING SLICING
# ============================================================

# Syntax:
# sequence[start:stop:step]
#
# start -> inclusive
# stop  -> exclusive
# step  -> default 1

s = "Python"

print(s[0:2])    # Py
print(s[2:])     # thon
print(s[:3])     # Pyt
print(s[:])      # Python
print(s[::2])    # Pto
print(s[::-1])   # nohtyP

# Negative slicing
print(s[-5:-2])


# ============================================================
# 8. STRING MEMBERSHIP
# ============================================================

word = "Artificial Intelligence"

print("Intelligence" in word)
print("Java" in word)
print("Java" not in word)

if "AI" in word:
    print("Substring exists")


# ============================================================
# 9. IMPORTANT STRING METHODS
# ============================================================

text = "  Artificial Intelligence  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# replace() returns a new string because strings are immutable.
print(text.replace("Artificial", "Generative"))

# split() converts a string into a list.
sentence = "Python is useful for AI"
words = sentence.split()
print(words)

# join() combines strings.
joined = "-".join(["Python", "AI", "ML"])
print(joined)

# startswith / endswith
filename = "model.csv"
print(filename.startswith("model"))
print(filename.endswith(".csv"))

# find()
print(sentence.find("useful"))
print(sentence.find("Java"))  # -1 if not found

# count()
print(sentence.count("i"))


# ============================================================
# 10. STRING FORMATTING — format()
# ============================================================

name = "Rahul"
age = 25

text = "My name is {} and I am {} years old.".format(name, age)
print(text)

# Positional placeholders
print("Coordinates: ({1}, {0})".format("x", "y"))

# Named placeholders
print("Name: {n}, Age: {a}".format(n="Bob", a=30))


# ============================================================
# 11. STRING FORMATTING — f-STRINGS
# ============================================================

name = "Rahul"
age = 25

text = f"My name is {name} and I am {age} years old."
print(text)

a = 5
b = 10

print(f"Sum of {a} & {b} = {a + b}")
print(f"Average of {a} & {b} = {(a + b) / 2}")


# Formatting numbers
pi = 3.14159265
print(f"Pi = {pi:.2f}")

percentage = 0.8765
print(f"Percentage = {percentage:.2%}")


# ============================================================
# 12. LISTS
# ============================================================

# A list is an ordered, mutable collection.
# Lists can contain duplicate and heterogeneous values.

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

my_list2 = [10, "Hello", 3.14, True, 10]
print(my_list2)

# Nested list
nested = [[1, 2], [3, 4]]
print(nested)


# ============================================================
# 13. LIST CHARACTERISTICS
# ============================================================

"""
Lists are:

1. Ordered
2. Mutable
3. Able to contain duplicates
4. Able to contain different data types
5. Indexed
6. Sliceable
"""


# ============================================================
# 14. LIST INDEXING
# ============================================================

my_list = ["apple", "banana", "cherry"]

print(my_list[0])
print(my_list[1])
print(my_list[-1])


# ============================================================
# 15. MODIFYING LIST ELEMENTS
# ============================================================

my_list = [1, 2, 3, 4]

my_list[0] = 10

print(my_list)


# ============================================================
# 16. LIST SLICING
# ============================================================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4]
print(numbers[:4])     # [0, 1, 2, 3]
print(numbers[5:])     # [5, 6, 7, 8, 9]
print(numbers[:])      # whole list
print(numbers[::2])    # every second element
print(numbers[1::3])   # 1, 4, 7
print(numbers[::-1])   # reversed list

# Negative slicing
print(numbers[-5:-2])


# ============================================================
# 17. LIST METHODS
# ============================================================

nums = [5, 2, 9]

print(len(nums))

# append() adds one element at the end.
nums.append(7)
print(nums)

# insert(index, value)
nums.insert(1, 4)
print(nums)

# sort() modifies the list in-place.
nums.sort()
print(nums)

# reverse() reverses the list in-place.
nums.reverse()
print(nums)


# ============================================================
# 18. MORE USEFUL LIST METHODS
# ============================================================

numbers = [10, 20, 30, 20, 40]

print(numbers.count(20))
print(numbers.index(30))

# remove() removes the first matching value.
numbers.remove(20)
print(numbers)

# pop() removes and returns an element.
removed = numbers.pop()
print("Removed:", removed)
print(numbers)

# pop(index)
numbers.pop(0)
print(numbers)

# clear()
numbers.clear()
print(numbers)


# ============================================================
# 19. LIST OPERATORS
# ============================================================

a = [1, 2, 3]
b = [4, 5]

print(a + b)       # concatenation
print(a * 2)       # repetition
print(2 in a)      # membership
print(10 not in a)


# ============================================================
# 20. COPYING LISTS — IMPORTANT RELATED CONCEPT
# ============================================================

original = [1, 2, 3]

# This does NOT create an independent list.
alias = original

alias.append(4)

print(original)  # original also changed
print(alias)


# Proper shallow copy
original = [1, 2, 3]

copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1.append(4)

print("Original:", original)
print("Copy:", copy1)


# ============================================================
# 21. LOOPING OVER LISTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# ============================================================
# 22. LIST WITH enumerate()
# ============================================================

numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)


# ============================================================
# 23. LINEAR SEARCH
# ============================================================

numbers = [5, 12, 7, 3, 18, 9]
target = 18

found_index = -1

for index, num in enumerate(numbers):
    if num == target:
        found_index = index
        break

print("Found at index:", found_index)


# Using the built-in index() method:
if target in numbers:
    print("Index:", numbers.index(target))


# ============================================================
# 24. LINEAR SEARCH AS A FUNCTION
# ============================================================

def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


print(linear_search([5, 12, 7, 3, 18, 9], 18))
print(linear_search([5, 12, 7, 3, 18, 9], 100))


# ============================================================
# 25. LIST COMPREHENSIONS — RELATED CONCEPT
# ============================================================

# General syntax:
# [expression for item in iterable]

squares = [x ** 2 for x in range(1, 6)]
print(squares)


# With a condition:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)


# Transforming strings:
words = ["python", "machine", "learning"]
upper_words = [word.upper() for word in words]
print(upper_words)


# ============================================================
# 26. NESTED LISTS
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])

for row in matrix:
    for value in row:
        print(value)


# ============================================================
# 27. TUPLES
# ============================================================

# A tuple is an ordered, immutable collection.

tup = (10, 20, 30)

print(tup)
print(type(tup))

empty_tuple = ()
single_element_tuple = (42,)

print(empty_tuple)
print(single_element_tuple)


# IMPORTANT:
# (42) is just an integer.
# (42,) is a tuple.

print(type((42)))
print(type((42,)))


# ============================================================
# 28. TUPLE CHARACTERISTICS
# ============================================================

"""
Tuples are:

1. Ordered
2. Immutable
3. Allow duplicates
4. Can contain different data types
5. Indexed
6. Sliceable
"""


# ============================================================
# 29. TUPLE INDEXING AND SLICING
# ============================================================

t = (10, 20, 30, 40)

print(t[0])
print(t[-1])
print(t[1:3])
print(t[::-1])


# This would raise TypeError:
# t[0] = 100


# ============================================================
# 30. LOOPING OVER TUPLES
# ============================================================

t = (10, 20, 30, 40)

for value in t:
    print(value)


# Sum using a loop
t = (5, 15, 25)

total = 0

for value in t:
    total += value

print("Sum:", total)


# ============================================================
# 31. TUPLE METHODS
# ============================================================

t = (1, 2, 2, 3, 5)

print(t.index(2))  # first occurrence
print(t.count(2))  # total occurrences


# ============================================================
# 32. TUPLE UNPACKING — RELATED CONCEPT
# ============================================================

person = ("Parth", 21, "AI/ML")

name, age, field = person

print(name)
print(age)
print(field)


# Extended unpacking
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# Swapping values using tuple unpacking
a = 10
b = 20

a, b = b, a

print(a, b)


# ============================================================
# 33. DICTIONARIES
# ============================================================

# A dictionary stores key-value pairs.

my_dict = {
    "name": "Shradha",
    "age": 30,
    "city": "Delhi"
}

print(my_dict)
print(type(my_dict))


# ============================================================
# 34. DICTIONARY CHARACTERISTICS
# ============================================================

"""
Dictionaries are:

1. Mutable
2. Key-value based
3. Keys must be unique
4. Keys must be hashable
5. Values can be of any normal Python type
6. Modern Python preserves insertion order
"""


# ============================================================
# 35. ACCESSING DICTIONARY VALUES
# ============================================================

student = {
    "name": "Bob",
    "age": 20
}

print(student["name"])
print(student["age"])


# Missing key with [] raises KeyError.
# print(student["city"])


# ============================================================
# 36. get() — SAFE DICTIONARY ACCESS
# ============================================================

student = {
    "name": "Bob",
    "age": 20
}

print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not Found"))


# ============================================================
# 37. ADDING AND MODIFYING DICTIONARY ITEMS
# ============================================================

student = {
    "name": "Bob",
    "age": 20
}

student["city"] = "Vadodara"
student["age"] = 21

print(student)


# ============================================================
# 38. DICTIONARY METHODS
# ============================================================

d = {
    "name": "Shradha",
    "subjects": ["math", "science", "physics"],
    "cgpa": 9.5
}

print(d.keys())
print(d.values())
print(d.items())

# update() adds or modifies entries.
d.update({"city": "Delhi"})
print(d)

# pop() removes a key and returns its value.
removed = d.pop("city")
print("Removed:", removed)
print(d)


# ============================================================
# 39. LOOPING THROUGH DICTIONARIES
# ============================================================

d = {
    "name": "Shradha",
    "subjects": ["math", "science", "physics"],
    "cgpa": 9.5
}

# Keys
for key in d:
    print(key)

# Values
for value in d.values():
    print(value)

# Key-value pairs
for key, value in d.items():
    print(key, value)


# ============================================================
# 40. DICTIONARY MEMBERSHIP
# ============================================================

student = {
    "name": "Parth",
    "age": 21
}

# 'in' checks keys by default.
print("name" in student)
print("Parth" in student)  # False

print("city" not in student)


# ============================================================
# 41. DICTIONARY WITH NESTED DATA
# ============================================================

student = {
    "name": "Parth",
    "marks": {
        "Python": 90,
        "ML": 85,
        "SQL": 88
    },
    "skills": ["Java", "Python", "Spring Boot"]
}

print(student["marks"]["ML"])
print(student["skills"][0])


# Nested structures are extremely common in real-world data.


# ============================================================
# 42. DICTIONARY COMPREHENSION — RELATED CONCEPT
# ============================================================

squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)


# ============================================================
# 43. SETS
# ============================================================

# A set is a mutable collection of unique elements.

my_set = {1, 2, 2, 2, 3}

print(my_set)
print(type(my_set))
print(len(my_set))


# Empty set:
empty_set = set()

# IMPORTANT:
# {} creates an empty dictionary, not an empty set.

empty_dict = {}

print(type(empty_set))
print(type(empty_dict))


# ============================================================
# 44. SET CHARACTERISTICS
# ============================================================

"""
Sets are:

1. Unique — duplicates are removed
2. Unordered — no index-based access
3. Mutable
4. Elements must be hashable
5. Useful for uniqueness and set operations
"""


# ============================================================
# 45. SET METHODS
# ============================================================

s = {10, 20, 30}

s.add(40)
print(s)

s.remove(10)
print(s)

# remove() raises KeyError if the element is absent.
# s.remove(100)

# discard() safely removes an element if it exists.
s.discard(100)
print(s)

# pop() removes and returns an arbitrary element.
removed = s.pop()
print("Removed:", removed)
print(s)

# clear()
s.clear()
print(s)


# ============================================================
# 46. SET UNION
# ============================================================

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A | B)


# ============================================================
# 47. SET INTERSECTION
# ============================================================

print(A.intersection(B))
print(A & B)


# ============================================================
# 48. SET DIFFERENCE — RELATED CONCEPT
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5}

print(A.difference(B))
print(A - B)

print(B.difference(A))
print(B - A)


# ============================================================
# 49. SYMMETRIC DIFFERENCE — RELATED CONCEPT
# ============================================================

# Elements present in either set, but not in both.

print(A.symmetric_difference(B))
print(A ^ B)


# ============================================================
# 50. SET SUBSET / SUPERSET
# ============================================================

A = {1, 2, 3, 4}
B = {1, 2}

print(B.issubset(A))
print(A.issuperset(B))


# ============================================================
# 51. FROZENSET — RELATED CONCEPT
# ============================================================

# frozenset is an immutable set.

fs = frozenset([1, 2, 3, 3])

print(fs)
print(type(fs))

# This would raise AttributeError:
# fs.add(4)


# ============================================================
# 52. MUTABILITY VS IMMUTABILITY
# ============================================================

"""
Mutable:
    list
    dict
    set

Immutable:
    int
    float
    bool
    str
    tuple
    frozenset

Mutable objects can generally be changed in-place.
Immutable objects require creating a new object for a changed value.
"""


# ============================================================
# 53. HASHABILITY — IMPORTANT RELATED CONCEPT
# ============================================================

"""
Dictionary keys and set elements must be hashable.

Common hashable examples:
    int
    float
    str
    tuple (when its contents are hashable)
    frozenset

Common unhashable examples:
    list
    dict
    set

Examples:
"""

valid_dict = {
    "name": "Parth",
    101: "Student",
    (1, 2): "Tuple key"
}

print(valid_dict)

# Invalid:
# invalid_dict = {[1, 2]: "list key"}  # TypeError


# ============================================================
# 54. COLLECTION COMPARISON
# ============================================================

"""
Collection    Ordered    Mutable    Duplicates    Access

list          Yes        Yes        Yes           index
tuple         Yes        No         Yes           index
dict          Yes*       Yes        keys unique   key
set           No         Yes        No             no index

* Modern Python dictionaries preserve insertion order.
"""


# ============================================================
# 55. PRACTICAL EXAMPLE — REMOVE DUPLICATES
# ============================================================

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(unique_numbers)

# Note:
# Converting through set does not guarantee the original ordering.
# If order must be preserved, use another approach.


# ============================================================
# 56. PRACTICAL EXAMPLE — FREQUENCY COUNT
# ============================================================

numbers = [1, 2, 2, 3, 1, 2, 4, 3]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)


# ============================================================
# 57. PRACTICAL EXAMPLE — WORD FREQUENCY
# ============================================================

sentence = "python is easy and python is powerful"

word_frequency = {}

for word in sentence.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency)


# ============================================================
# 58. PRACTICAL EXAMPLE — COMMON ELEMENTS
# ============================================================

skills_a = {"Python", "Java", "SQL", "Git"}
skills_b = {"Python", "SQL", "Docker", "AWS"}

common_skills = skills_a & skills_b

print("Common skills:", common_skills)


# ============================================================
# 59. PRACTICAL EXAMPLE — LIST OF DICTIONARIES
# ============================================================

students = [
    {"name": "Parth", "marks": 90},
    {"name": "Alex", "marks": 85},
    {"name": "John", "marks": 78}
]

for student in students:
    print(student["name"], student["marks"])


# This structure is very common when working with JSON/API data.


# ============================================================
# 60. PRACTICAL EXAMPLE — FILTER A LIST
# ============================================================

numbers = [10, 25, 30, 7, 42, 18]

greater_than_20 = [number for number in numbers if number > 20]

print(greater_than_20)


# ============================================================
# 61. PRACTICAL EXAMPLE — SIMPLE DATASET RECORD
# ============================================================

record = {
    "id": 101,
    "name": "Parth",
    "features": [8.63, 350, 21],
    "skills": {"Python", "Java", "SQL"}
}

print(record["name"])
print(record["features"][0])
print(record["skills"])


# This kind of nested structure will be useful when working
# with data, JSON, APIs and ML datasets.
