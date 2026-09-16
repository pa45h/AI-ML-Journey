# ============================================================
# 1. FILE I/O — INTRODUCTION
# ============================================================

"""
File I/O means reading data from files and writing data to files.

Typical workflow:

    open file
        ↓
    read / write
        ↓
    close file

The recommended Python approach is:

    with open(...) as file:
        ...

because the context manager automatically closes the file.
"""


# ============================================================
# 2. FILE MODES
# ============================================================

"""
Common modes:

r   Read
    Opens an existing file for reading.
    Raises FileNotFoundError if the file does not exist.

w   Write
    Creates a new file or overwrites an existing file.

a   Append
    Creates the file if needed and writes at the end.

r+  Read + Write
    File must already exist.

w+  Write + Read
    Creates/overwrites the file.

a+  Append + Read
    Reading + writing, with writes at the end.

b   Binary mode
    Used with modes such as rb / wb for binary data.
"""


# ============================================================
# 3. CREATING A SAFE TEMPORARY FILE FOR DEMOS
# ============================================================

from pathlib import Path
import tempfile

demo_dir = Path(tempfile.mkdtemp(prefix="python_fileio_"))
demo_file = demo_dir / "data.txt"

print("Demo directory:", demo_dir)
print("Demo file:", demo_file)


# ============================================================
# 4. OPENING AND WRITING A FILE
# ============================================================

# "w" creates or overwrites a file.

with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Hello students!\n")
    f.write("Python is useful for AI/ML.\n")

print("File created and written.")


# ============================================================
# 5. READING THE ENTIRE FILE — read()
# ============================================================

with open(demo_file, "r", encoding="utf-8") as f:
    content = f.read()

print(content)


# ============================================================
# 6. READING A FIXED NUMBER OF CHARACTERS
# ============================================================

with open(demo_file, "r", encoding="utf-8") as f:
    first_10_characters = f.read(10)

print(first_10_characters)


# ============================================================
# 7. readline()
# ============================================================

with open(demo_file, "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()

print("Line 1:", line1, end="")
print("Line 2:", line2, end="")


# ============================================================
# 8. readlines()
# ============================================================

with open(demo_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("\nLines:", lines)
print("Type:", type(lines))


# ============================================================
# 9. ITERATING DIRECTLY OVER A FILE
# ============================================================

with open(demo_file, "r", encoding="utf-8") as f:
    for line in f:
        print("READ:", line.strip())


# Iterating over a file is memory-efficient compared with loading
# a very large file completely into memory.


# ============================================================
# 10. WRITING MULTIPLE LINES — writelines()
# ============================================================

lines_to_write = [
    "Python\n",
    "Machine Learning\n",
    "Deep Learning\n",
]

with open(demo_file, "w", encoding="utf-8") as f:
    f.writelines(lines_to_write)

with open(demo_file, "r", encoding="utf-8") as f:
    print(f.read())


# IMPORTANT:
# writelines() does NOT automatically add newline characters.
# You need to include "\n" yourself when required.


# ============================================================
# 11. APPENDING TO A FILE
# ============================================================

with open(demo_file, "a", encoding="utf-8") as f:
    f.write("Generative AI\n")
    f.write("RAG\n")

with open(demo_file, "r", encoding="utf-8") as f:
    print(f.read())


# "a" preserves existing content and writes at the end.


# ============================================================
# 12. WRITE MODE VS APPEND MODE
# ============================================================

"""
w:
    Existing content is discarded when the file is opened.

a:
    Existing content is preserved.
    New content is added at the end.

Use "w" carefully because it can overwrite data.
"""


# ============================================================
# 13. CONTEXT MANAGER — with open()
# ============================================================

with open(demo_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# File is automatically closed after leaving the with block.


# ============================================================
# 14. CHECKING WHETHER A FILE IS CLOSED
# ============================================================

f = open(demo_file, "r", encoding="utf-8")

print("Before close:", f.closed)

f.close()

print("After close:", f.closed)


# Explicit close() is valid, but "with open()" is preferred.


# ============================================================
# 15. pathlib.Path — RELATED MODERN APPROACH
# ============================================================

file_path = demo_dir / "example.txt"

file_path.write_text(
    "Python\nAI\nML\n",
    encoding="utf-8"
)

content = file_path.read_text(encoding="utf-8")

print(content)

# pathlib provides a clean object-oriented interface for paths
# and many common file operations.


# ============================================================
# 16. FILE CURSOR — tell() AND seek()
# ============================================================

cursor_file = demo_dir / "cursor.txt"

cursor_file.write_text(
    "ABCDEFGHIJ",
    encoding="utf-8"
)

with open(cursor_file, "r", encoding="utf-8") as f:
    print("Initial position:", f.tell())

    print(f.read(3))
    print("After reading 3:", f.tell())

    f.seek(0)
    print("After seek(0):", f.tell())

    print(f.read(2))


# tell() -> current file position
# seek() -> moves the file position


# ============================================================
# 17. BINARY MODE — RELATED CONCEPT
# ============================================================

binary_file = demo_dir / "binary.bin"

with open(binary_file, "wb") as f:
    f.write(b"Hello")

with open(binary_file, "rb") as f:
    data = f.read()

print(data)
print(type(data))


# Binary mode returns bytes rather than normal strings.
# Useful for images, PDFs, audio, videos, etc.


# ============================================================
# 18. ENCODING — RELATED CONCEPT
# ============================================================

unicode_file = demo_dir / "unicode.txt"

with open(unicode_file, "w", encoding="utf-8") as f:
    f.write("Python 🤖\n")
    f.write("ગુજરાતી\n")
    f.write("₹1000\n")

with open(unicode_file, "r", encoding="utf-8") as f:
    print(f.read())


# UTF-8 is a common choice for text files containing Unicode.


# ============================================================
# 19. DELETING A FILE
# ============================================================

import os

delete_me = demo_dir / "delete_me.txt"

delete_me.write_text("Temporary file", encoding="utf-8")

if delete_me.exists():
    os.remove(delete_me)

print("File exists after deletion:", delete_me.exists())


# IMPORTANT:
# os.remove() permanently deletes the file.
# Always verify the path before deleting real files.


# ============================================================
# 20. DELETING WITH pathlib — RELATED CONCEPT
# ============================================================

another_file = demo_dir / "another.txt"
another_file.write_text("Temporary", encoding="utf-8")

if another_file.exists():
    another_file.unlink()

print("File exists:", another_file.exists())


# Path.unlink() is pathlib's file-deletion method.


# ============================================================
# 21. EXCEPTION HANDLING
# ============================================================

"""
An exception is an error/event that occurs during program
execution.

If an exception is not handled, program execution can terminate.

Exception handling lets us respond to errors gracefully.
"""


# ============================================================
# 22. COMMON EXCEPTIONS
# ============================================================

"""
ZeroDivisionError
    Dividing by zero.

NameError
    Using a name that has not been defined.

FileNotFoundError
    Attempting to open a missing file.

TypeError
    Operation performed on an inappropriate type.

ValueError
    Correct type, but invalid value.

IndexError
    Sequence index does not exist.

KeyError
    Dictionary key does not exist.

AttributeError
    Object does not have the requested attribute.
"""


# ============================================================
# 23. BASIC try / except
# ============================================================

try:
    result = 10 / 0
except:
    print("An error occurred.")


# Bare except works, but specific exceptions are generally
# preferable because they make the error handling precise.


# ============================================================
# 24. SPECIFIC EXCEPTION
# ============================================================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")


# ============================================================
# 25. MULTIPLE EXCEPT BLOCKS
# ============================================================

def demonstrate_exceptions(value):
    try:
        number = int(value)
        result = 100 / number
        print("Result:", result)

    except ValueError:
        print("Input must be a valid integer.")

    except ZeroDivisionError:
        print("Number cannot be zero.")


demonstrate_exceptions("10")
demonstrate_exceptions("abc")
demonstrate_exceptions("0")


# ============================================================
# 26. EXCEPTION OBJECT — as e
# ============================================================

try:
    int("hello")
except ValueError as e:
    print("Exception:", e)
    print("Exception type:", type(e))


# "as e" gives access to the exception object.


# ============================================================
# 27. else BLOCK
# ============================================================

try:
    number = int("25")
except ValueError:
    print("Invalid input.")
else:
    print("Conversion successful:", number)


# else executes only when the try block completes
# without an exception.


# ============================================================
# 28. finally BLOCK
# ============================================================

try:
    number = 10 / 2
    print(number)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This always executes.")


# finally is commonly used for cleanup.


# ============================================================
# 29. try / except / else / finally TOGETHER
# ============================================================

try:
    number = int("50")
    result = 100 / number

except ValueError:
    print("Invalid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Success:", result)

finally:
    print("Operation completed.")


# ============================================================
# 30. FILE I/O + EXCEPTION HANDLING
# ============================================================

missing_file = demo_dir / "missing.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as f:
        print(f.read())

except FileNotFoundError:
    print("File was not found.")


# ============================================================
# 31. HANDLING USER INPUT SAFELY
# ============================================================

# Input is intentionally hard-coded here so this file can run
# without waiting for interactive input.

user_input = "42"

try:
    number = int(user_input)
except ValueError:
    print("Invalid number.")
else:
    print("Valid number:", number)


# ============================================================
# 32. raise — RELATED CONCEPT
# ============================================================

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


print(set_age(21))

# set_age(-1)  # ValueError


# raise allows us to explicitly trigger an exception when
# a program detects invalid state/input.


# ============================================================
# 33. CUSTOM EXCEPTION — RELATED CONCEPT
# ============================================================

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    return balance - amount


try:
    balance = withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print(e)


# Custom exceptions make application-specific errors clearer.


# ============================================================
# 34. EXCEPTION HIERARCHY — RELATED CONCEPT
# ============================================================

"""
Most normal application exceptions inherit from Exception.

A simplified hierarchy:

BaseException
    ├── Exception
    │      ├── ValueError
    │      ├── TypeError
    │      ├── OSError
    │      │     └── FileNotFoundError
    │      └── ...
    └── system-level exceptions

Usually catch Exception subclasses rather than BaseException.
"""

# ============================================================
# 35. JSON — INTRODUCTION
# ============================================================

"""
JSON = JavaScript Object Notation

It is a lightweight data-interchange format commonly used by:

    - APIs
    - Web applications
    - Configuration files
    - Data storage
    - Backend/frontend communication

JSON is structurally similar to Python dictionaries/lists.
"""


# ============================================================
# 36. IMPORTING JSON
# ============================================================

import json


# ============================================================
# 37. PYTHON OBJECT -> JSON STRING — dumps()
# ============================================================

data = {
    "name": "John",
    "age": 25,
    "marks": [85, 90, 92]
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))


# dumps() returns a JSON-formatted string.


# ============================================================
# 38. JSON STRING -> PYTHON OBJECT — loads()
# ============================================================

json_data = '{"name": "John", "age": 25}'

python_obj = json.loads(json_data)

print(python_obj)
print(type(python_obj))
print(python_obj["name"])


# loads() converts JSON text into Python objects.


# ============================================================
# 39. PRETTY JSON — indent
# ============================================================

data = {
    "name": "Aisha",
    "city": "Delhi",
    "skills": ["Python", "ML", "SQL"]
}

pretty_json = json.dumps(data, indent=4)

print(pretty_json)


# indent makes JSON easier for humans to read.


# ============================================================
# 40. JSON FILE — dump()
# ============================================================

json_file = demo_dir / "data.json"

data = {
    "name": "Aisha",
    "city": "Delhi",
    "marks": [85, 90, 92]
}

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("JSON written to:", json_file)


# dump() writes Python data directly to a file.


# ============================================================
# 41. JSON FILE -> PYTHON OBJECT — load()
# ============================================================

with open(json_file, "r", encoding="utf-8") as f:
    data_from_file = json.load(f)

print(data_from_file)
print(type(data_from_file))
print(data_from_file["name"])


# load() reads JSON directly from a file.


# ============================================================
# 42. dumps / loads / dump / load
# ============================================================

"""
dumps()
    Python object -> JSON string

loads()
    JSON string -> Python object

dump()
    Python object -> JSON file

load()
    JSON file -> Python object
"""


# ============================================================
# 43. JSON DATA TYPES
# ============================================================

"""
Common JSON mapping:

Python             JSON

dict                object
list / tuple        array
str                 string
int / float         number
True                true
False               false
None                null

JSON does not support every Python-specific object directly.
"""


# ============================================================
# 44. JSON SERIALIZATION
# ============================================================

data = {
    "name": "Parth",
    "age": 21,
    "active": True,
    "skills": ["Python", "Java"],
    "address": None
}

json_text = json.dumps(data)

print(json_text)


# Serialization:
# Converting an in-memory Python object into a transferable/
# storable representation such as JSON.


# ============================================================
# 45. JSON DESERIALIZATION
# ============================================================

json_text = """
{
    "name": "Parth",
    "age": 21,
    "active": true,
    "skills": ["Python", "Java"],
    "address": null
}
"""

data = json.loads(json_text)

print(data)
print(data["skills"])


# Deserialization:
# Converting JSON data back into a Python object.


# ============================================================
# 46. INVALID JSON — EXCEPTION HANDLING
# ============================================================

invalid_json = '{"name": "Parth",}'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)


# JSONDecodeError is useful when processing external JSON data.


# ============================================================
# 47. JSON + API-LIKE DATA
# ============================================================

api_response = """
{
    "status": "success",
    "data": {
        "user_id": 101,
        "name": "Parth",
        "skills": ["Python", "SQL", "Java"]
    }
}
"""

response = json.loads(api_response)

print(response["status"])
print(response["data"]["name"])
print(response["data"]["skills"])


# This structure resembles data returned by REST APIs.


# ============================================================
# 48. JSON + LIST OF RECORDS
# ============================================================

students = [
    {"name": "Parth", "marks": 90},
    {"name": "Alex", "marks": 85},
    {"name": "John", "marks": 78}
]

json_students = json.dumps(students, indent=4)

print(json_students)

restored_students = json.loads(json_students)

for student in restored_students:
    print(student["name"], student["marks"])


# ============================================================
# 49. FILE I/O + JSON + EXCEPTION HANDLING
# ============================================================

config_file = demo_dir / "config.json"

config = {
    "model": "example-model",
    "learning_rate": 0.001,
    "epochs": 10
}

# Write
with open(config_file, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

# Read safely
try:
    with open(config_file, "r", encoding="utf-8") as f:
        loaded_config = json.load(f)

except FileNotFoundError:
    print("Configuration file not found.")

except json.JSONDecodeError:
    print("Configuration file contains invalid JSON.")

else:
    print("Loaded config:", loaded_config)

finally:
    print("Configuration operation completed.")


# This combines the major concepts of the lecture.


# ============================================================
# 50. PRACTICAL EXAMPLE — PROCESS A TEXT FILE
# ============================================================

text_file = demo_dir / "words.txt"

text_file.write_text(
    "python\n"
    "machine\n"
    "learning\n"
    "python\n"
    "ai\n",
    encoding="utf-8"
)

word_count = 0

with open(text_file, "r", encoding="utf-8") as f:
    for line in f:
        word = line.strip()

        if word:
            word_count += 1

print("Number of non-empty lines:", word_count)


# ============================================================
# 51. PRACTICAL EXAMPLE — FREQUENCY COUNT FROM FILE
# ============================================================

frequency = {}

with open(text_file, "r", encoding="utf-8") as f:
    for line in f:
        word = line.strip().lower()

        if word:
            frequency[word] = frequency.get(word, 0) + 1

print("Frequency:", frequency)


# ============================================================
# 52. PRACTICAL EXAMPLE — FILTER DATA WITH COMPREHENSION
# ============================================================

marks = [45, 82, 67, 91, 38, 76]

passed_marks = [mark for mark in marks if mark >= 50]

print("Passed marks:", passed_marks)


# ============================================================
# 53. PRACTICAL EXAMPLE — CREATE LABELS
# ============================================================

marks = [45, 82, 67, 91, 38, 76]

labels = [
    "Pass" if mark >= 50 else "Fail"
    for mark in marks
]

print(labels)


# ============================================================
# 54. PRACTICAL EXAMPLE — AI/ML CONFIGURATION
# ============================================================

ml_config = {
    "model": "neural_network",
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 20,
    "features": ["age", "income", "score"]
}

ml_config_file = demo_dir / "ml_config.json"

with open(ml_config_file, "w", encoding="utf-8") as f:
    json.dump(ml_config, f, indent=4)

with open(ml_config_file, "r", encoding="utf-8") as f:
    loaded_ml_config = json.load(f)

print(loaded_ml_config)


# Configuration files like this are common in ML projects.


# ============================================================
# 55. PRACTICAL EXAMPLE — JSON DATA TRANSFORMATION
# ============================================================

records = [
    {"name": "Parth", "score": 90},
    {"name": "Alex", "score": 72},
    {"name": "John", "score": 45}
]

high_scores = [
    record
    for record in records
    if record["score"] >= 70
]

print(high_scores)


# ============================================================
# 56. COMMON FILE I/O MISTAKES
# ============================================================

"""
1. Forgetting to close a file
    Prefer:
        with open(...) as f:

2. Using "w" when you intended to append
    "w" can overwrite existing content.

3. Forgetting newline characters with writelines()
    writelines() does not add them automatically.

4. Reading a missing file without handling FileNotFoundError

5. Ignoring encoding for text containing Unicode

6. Loading huge files entirely with read()
    Iterating line-by-line may be more memory-efficient.

7. Deleting the wrong file/path
    Verify before using os.remove() or unlink().
"""


# ============================================================
# 57. COMMON EXCEPTION-HANDLING MISTAKES
# ============================================================

"""
1. Catching every exception with bare except:
       except:
           ...

   Prefer specific exceptions.

2. Hiding errors completely:
       except Exception:
           pass

   This can make debugging difficult.

3. Putting too much code inside try:
   Keep the try block focused on operations that can fail.

4. Using exceptions for ordinary control flow unnecessarily.

5. Forgetting to preserve useful error information:
       except ValueError as e:
           print(e)
"""


# ============================================================
# 58. LIST COMPREHENSION VS NORMAL LOOP
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Comprehension
squares_1 = [x ** 2 for x in numbers]

# Normal loop
squares_2 = []

for x in numbers:
    squares_2.append(x ** 2)

print(squares_1)
print(squares_2)

# Both produce the same result.
# Use comprehensions when they remain readable.
# Use normal loops when the logic becomes complex.


# ============================================================
# 59. MINI REVISION EXERCISE — FILE + JSON
# ============================================================

exercise_file = demo_dir / "students.json"

students = [
    {"name": "Parth", "score": 91},
    {"name": "Alex", "score": 84},
    {"name": "John", "score": 67}
]

# Save
with open(exercise_file, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)

# Load
try:
    with open(exercise_file, "r", encoding="utf-8") as f:
        loaded_students = json.load(f)

except (FileNotFoundError, json.JSONDecodeError) as e:
    print("Could not load students:", e)

else:
    top_students = [
        student
        for student in loaded_students
        if student["score"] >= 80
    ]

    print("Top students:", top_students)
