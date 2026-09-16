# ============================================================
# 1. WHAT IS OBJECT-ORIENTED PROGRAMMING?
# ============================================================

"""
OOP organizes software around objects.

An object combines:
    - Data/state  -> attributes
    - Behavior    -> methods

A class is a blueprint/template used to create objects.

Example idea:
    Class  -> Student
    Objects -> student1, student2, student3

OOP is useful when a program contains entities with both data
and behavior.
"""


# ============================================================
# 2. CLASS AND OBJECT
# ============================================================

class Car:
    brand = "Toyota"


# Creating objects
car1 = Car()
car2 = Car()

print(car1.brand)
print(car2.brand)

# car1 and car2 are separate object instances of Car.
print(type(car1))
print(isinstance(car1, Car))


# ============================================================
# 3. CLASS VS OBJECT
# ============================================================

"""
Class:
    Blueprint/template.
    Defines attributes and behavior.
    Does not represent one concrete instance.

Object:
    Concrete instance of a class.
    Has its own instance state.
    Created from the class.

One class can create many objects.
"""


# ============================================================
# 4. ATTRIBUTES AND METHODS
# ============================================================

class Student:
    college = "ABC College"  # class attribute

    def __init__(self, name, marks):
        self.name = name      # instance attribute
        self.marks = marks    # instance attribute

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


student1 = Student("Parth", 90)
student2 = Student("Alex", 85)

student1.display()
student2.display()

print(student1.name)
print(student2.marks)


# ============================================================
# 5. self
# ============================================================

"""
self refers to the current object instance.

When:
    student1.display()

Python effectively binds student1 to self.

Inside:
    self.name

means:
    the name belonging to the current Student object.

self is not a Python keyword, but it is the conventional name.
"""

class Demo:
    def show(self):
        print("Current object:", self)


obj = Demo()
obj.show()


# ============================================================
# 6. CONSTRUCTOR — __init__()
# ============================================================

class Student:
    def __init__(self):
        print("Constructor was called")


stu = Student()


# __init__ is automatically called after an object is created.
# It is commonly used to initialize instance attributes.


# ============================================================
# 7. PARAMETERIZED CONSTRUCTOR
# ============================================================

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa


stu1 = Student("Rahul", 8.7)
stu2 = Student("Harshita", 9.1)

print(stu1.name, stu1.cgpa)
print(stu2.name, stu2.cgpa)


# ============================================================
# 8. DEFAULT PARAMETERS IN __init__()
# ============================================================

class User:
    def __init__(self, name="Guest"):
        self.name = name


u1 = User()
u2 = User("Parth")

print(u1.name)
print(u2.name)


# ============================================================
# 9. PYTHON DOES NOT SUPPORT DIRECT CONSTRUCTOR OVERLOADING
# ============================================================

"""
Python does not support multiple __init__ methods with different
signatures in the same class like Java/C++.

If you write:

    def __init__(self, a):
        ...

    def __init__(self, a, b):
        ...

the second definition replaces the first.

Common alternatives:
    - default parameters
    - *args / **kwargs
    - class methods / factory methods
"""


# ============================================================
# 10. CLASS ATTRIBUTES
# ============================================================

class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name


s1 = Student("Parth")
s2 = Student("Alex")

print(s1.college)
print(s2.college)
print(Student.college)


# Class attributes belong to the class and are shared through
# the class unless an instance gets its own attribute with the
# same name.


# ============================================================
# 11. INSTANCE ATTRIBUTES
# ============================================================

class Student:
    college = "ABC College"

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa


s1 = Student("Parth", 8.63)
s2 = Student("Alex", 8.20)

print(s1.name, s1.cgpa)
print(s2.name, s2.cgpa)


# Each object has independent instance attributes.


# ============================================================
# 12. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# ============================================================

class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name


e1 = Employee("Parth")
e2 = Employee("Alex")

# Both initially read the class attribute.
print(e1.company)
print(e2.company)

# Creating an instance attribute with the same name shadows
# the class attribute for that object.
e1.company = "OtherCorp"

print(e1.company)
print(e2.company)
print(Employee.company)


# ============================================================
# 13. INSTANCE METHODS
# ============================================================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name}: {self.marks}")


student = Student("Parth", 90)
student.display()


# Instance methods receive self as the first parameter.


# ============================================================
# 14. CLASS METHODS
# ============================================================

class Student:
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


print(Student.school_name)

Student.change_school("XYZ School")

print(Student.school_name)


# Class methods:
# - use @classmethod
# - receive cls
# - operate primarily on class-level state


# ============================================================
# 15. STATIC METHODS
# ============================================================

class Math:
    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(10, 20))

# Static methods do not receive self or cls automatically.
# They are grouped inside a class because they are logically
# related to the class.


# ============================================================
# 16. THREE TYPES OF METHODS
# ============================================================

"""
Instance method:
    def method(self):
        ...
    Works with object/instance data.

Class method:
    @classmethod
    def method(cls):
        ...
    Works with class-level data.

Static method:
    @staticmethod
    def method(...):
        ...
    Does not automatically receive self or cls.
"""


# ============================================================
# 17. METHOD BINDING — RELATED CONCEPT
# ============================================================

class Calculator:
    def add(self, a, b):
        return a + b


calc = Calculator()

# Access through object:
print(calc.add(2, 3))

# Python automatically binds calc as self.

# The unbound function can also be called explicitly:
print(Calculator.add(calc, 2, 3))


# ============================================================
# 18. ENCAPSULATION
# ============================================================

"""
Encapsulation means bundling data and methods together while
controlling how the internal state is accessed or modified.

Python does not enforce Java/C++-style access modifiers strictly.
Instead, naming conventions and mechanisms such as name mangling
are used.
"""


# ============================================================
# 19. PUBLIC MEMBERS
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name


student = Student("Parth")

print(student.name)


# Public members are normally accessible from anywhere.


# ============================================================
# 20. PROTECTED MEMBERS
# ============================================================

class Person:
    def __init__(self):
        self._age = 20


person = Person()

print(person._age)

# A single underscore means:
# "This is intended for internal/subclass use."
#
# Python still technically allows access from outside.


# ============================================================
# 21. PRIVATE MEMBERS / NAME MANGLING
# ============================================================

class Bank:
    def __init__(self, balance):
        self.__balance = balance


bank = Bank(500)

# Direct access raises AttributeError:
# print(bank.__balance)

# Python name-mangles __balance to:
# _Bank__balance

print(bank._Bank__balance)


# Important:
# Python's "private" members are not strict private access
# modifiers like Java/C++.
# They use name mangling.


# ============================================================
# 22. GETTERS AND SETTERS
# ============================================================

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary cannot be negative")


employee = Employee(50000)

print(employee.get_salary())

employee.set_salary(60000)
print(employee.get_salary())

employee.set_salary(-100)


# ============================================================
# 23. property() — PYTHONIC GETTERS/SETTERS
# ============================================================

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


person = Person(21)

print(person.age)

person.age = 22
print(person.age)

# property lets us use attribute syntax while still running
# getter/setter logic.


# ============================================================
# 24. INHERITANCE
# ============================================================

"""
Inheritance allows a child/derived class to acquire attributes
and methods from a parent/base class.

Parent -> Base -> Superclass
Child  -> Derived -> Subclass
"""


class Employee:
    start_time = "9AM"
    end_time = "5PM"


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


teacher = Teacher("Data Science")

print(teacher.subject)
print(teacher.start_time)
print(teacher.end_time)


# ============================================================
# 25. BENEFITS OF INHERITANCE
# ============================================================

"""
Inheritance can provide:

- Code reuse
- Extensibility
- Cleaner organization
- Polymorphism

Use inheritance when there is a genuine "is-a" relationship.
"""


# ============================================================
# 26. SINGLE INHERITANCE
# ============================================================

class Parent:
    def display(self):
        print("Parent class")


class Child(Parent):
    pass


c = Child()
c.display()


# One child inherits from one parent.


# ============================================================
# 27. MULTILEVEL INHERITANCE
# ============================================================

class Employee:
    start_time = "9AM"
    end_time = "5PM"


class Administrator(Employee):
    def __init__(self, role):
        self.role = role


class Accountant(Administrator):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


accountant = Accountant(50000, "Finance")

print(accountant.role)
print(accountant.salary)
print(accountant.start_time)
print(accountant.end_time)


# Employee -> Administrator -> Accountant


# ============================================================
# 28. MULTIPLE INHERITANCE
# ============================================================

class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TeachingAssistant(Teacher, Student):
    def __init__(self, salary, gpa):
        Teacher.__init__(self, salary)
        Student.__init__(self, gpa)


ta = TeachingAssistant(50000, 8.5)

print(ta.salary)
print(ta.gpa)


# A child inherits from more than one parent.


# ============================================================
# 29. super()
# ============================================================

class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


child = Child("Parth", 21)

print(child.name)
print(child.age)


# super() is commonly used to call parent-class methods/constructors.


# ============================================================
# 30. METHOD RESOLUTION ORDER (MRO)
# ============================================================

class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

print(D.mro())

# MRO determines the order Python follows when searching for
# attributes/methods in an inheritance hierarchy.


# ============================================================
# 31. ABSTRACTION
# ============================================================

"""
Abstraction means hiding unnecessary implementation details and
exposing only the essential interface.

Real-world idea:
    When driving a car, you use steering/brakes/accelerator.
    You do not need to know every internal engine operation.

Python provides abstract base classes through the abc module.
"""


# ============================================================
# 32. ABSTRACT CLASS AND ABSTRACT METHOD
# ============================================================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


# Animal cannot normally be instantiated because make_sound()
# is abstract.

# animal = Animal()  # TypeError


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()


# ============================================================
# 33. ABSTRACT CLASS WITH NORMAL METHOD
# ============================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):

    def start(self):
        print("Car started")


car = Car()

car.start()
car.stop()


# An abstract class may contain both abstract and concrete methods.


# ============================================================
# 34. POLYMORPHISM
# ============================================================

"""
Polymorphism means one interface/name can work with different
types of objects and produce behavior appropriate to the object.

"poly" -> many
"morph" -> forms
"""


# ============================================================
# 35. OPERATOR OVERLOADING
# ============================================================

print(1 + 2)
print("AI" + "ML")

# The same + operator behaves differently depending on operands.

# Behind the scenes, Python uses special/dunder methods such as
# __add__() to implement this behavior.


# ============================================================
# 36. CUSTOM OPERATOR OVERLOADING
# ============================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2

print(p3)


# __add__ controls the behavior of + for Point objects.


# ============================================================
# 37. METHOD OVERRIDING
# ============================================================

class Animal:
    def sound(self):
        print("Generic sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()


# Dog overrides the inherited sound() method.


# ============================================================
# 38. RUNTIME POLYMORPHISM
# ============================================================

def make_sound(animal):
    animal.sound()


make_sound(Animal())
make_sound(Dog())


# The function does not need to know the concrete class.
# It only expects the object to provide sound().


# ============================================================
# 39. DUCK TYPING
# ============================================================

"""
Duck typing follows the idea:

    "If it walks like a duck and quacks like a duck,
     it can be treated like a duck."

Python often cares about what an object can do rather than
its exact class.
"""


class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Robot:
    def speak(self):
        print("Beep Boop")


def make_it_speak(entity):
    entity.speak()


for entity in [Dog(), Cat(), Robot()]:
    make_it_speak(entity)


# No inheritance relationship is required here.


# ============================================================
# 40. isinstance() AND issubclass()
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, object))

print(issubclass(Dog, Animal))
print(issubclass(Dog, object))


# isinstance() checks an object.
# issubclass() checks a class relationship.


# ============================================================
# 41. DUNDER / MAGIC METHODS
# ============================================================

"""
Methods surrounded by double underscores are commonly called
dunder (double-underscore) methods.

Examples:
    __init__
    __str__
    __repr__
    __len__
    __add__
    __eq__

They allow Python objects to integrate with built-in syntax.
"""


# ============================================================
# 42. __str__ VS __repr__
# ============================================================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

    def __repr__(self):
        return f"Student(name={self.name!r}, marks={self.marks!r})"


student = Student("Parth", 90)

print(str(student))
print(repr(student))


# __str__ -> human-friendly representation.
# __repr__ -> developer/debugging representation.


# ============================================================
# 43. __len__ — RELATED DUNDER METHOD
# ============================================================

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Parth", "Alex", "John"])

print(len(team))


# ============================================================
# 44. COMPOSITION — RELATED OOP CONCEPT
# ============================================================

"""
Composition means building a class using objects of other classes.

It represents a "has-a" relationship.

Inheritance:
    Car IS-A Vehicle

Composition:
    Car HAS-A Engine
"""


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start()


# Composition is often preferable when the relationship is
# "has-a" rather than "is-a".


# ============================================================
# 45. DEPENDENCY-STYLE POLYMORPHISM
# ============================================================

class EmailSender:
    def send(self, message):
        print(f"Email: {message}")


class SMSSender:
    def send(self, message):
        print(f"SMS: {message}")


def notify(sender, message):
    sender.send(message)


notify(EmailSender(), "Training starts at 9 AM")
notify(SMSSender(), "Training starts at 9 AM")


# This is a practical form of duck typing and polymorphism:
# notify() only requires a send() method.


# ============================================================
# 46. FACTORY METHOD — RELATED PATTERN PREVIEW
# ============================================================

class User:
    def __init__(self, name):
        self.name = name

    @classmethod
    def guest(cls):
        return cls("Guest")


user = User.guest()

print(user.name)


# A class method can act as an alternative/factory constructor.


# ============================================================
# 47. DATACLASS — RELATED MODERN PYTHON CONCEPT
# ============================================================

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


product = Product("Laptop", 75000)

print(product)
print(product.name)
print(product.price)


# dataclass automatically provides useful methods such as
# __init__ and __repr__ for data-oriented classes.


# ============================================================
# 48. CLASS NAMESPACE AND INSTANCE NAMESPACE
# ============================================================

class Example:
    class_value = 100

    def __init__(self, instance_value):
        self.instance_value = instance_value


obj = Example(50)

print(Example.__dict__)
print(obj.__dict__)


# __dict__ shows attributes stored in the corresponding namespace
# when applicable.


# ============================================================
# 49. PRACTICAL EXAMPLE — BANK ACCOUNT
# ============================================================

class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Parth", 1000)

account.deposit(500)
account.withdraw(200)

print(account.owner)
print(account.get_balance())


# This example combines:
# - class attribute
# - instance attributes
# - constructor
# - private state
# - instance methods
# - encapsulation


# ============================================================
# 50. PRACTICAL EXAMPLE — AI MODEL INTERFACE
# ============================================================

class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass


class LinearModel(Model):
    def predict(self, data):
        return [x * 2 for x in data]


class ConstantModel(Model):
    def predict(self, data):
        return [1 for _ in data]


def run_model(model, data):
    return model.predict(data)


data = [1, 2, 3]

print(run_model(LinearModel(), data))
print(run_model(ConstantModel(), data))


# This demonstrates how abstraction + polymorphism can be useful
# in AI/ML software: different models can expose the same interface.


# ============================================================
# 51. PRACTICAL EXAMPLE — TRAINER INTERFACE
# ============================================================

class Trainer(ABC):

    @abstractmethod
    def train(self, data):
        pass


class SklearnTrainer(Trainer):
    def train(self, data):
        print("Training using a scikit-learn style workflow")


class PyTorchTrainer(Trainer):
    def train(self, data):
        print("Training using a PyTorch style workflow")


trainers = [SklearnTrainer(), PyTorchTrainer()]

for trainer in trainers:
    trainer.train(data)


# Same interface, different implementation.


# ============================================================
# 52. ENCAPSULATION + PROPERTY — PRACTICAL MODEL PARAMETER
# ============================================================

class ModelConfig:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive")
        self._learning_rate = value


config = ModelConfig(0.001)

print(config.learning_rate)

config.learning_rate = 0.01
print(config.learning_rate)

# config.learning_rate = -1  # ValueError


# ============================================================
# 53. IMPORTANT OOP PILLARS
# ============================================================

"""
ENCAPSULATION
    Bundling data and behavior together while controlling access
    to internal state.

ABSTRACTION
    Hiding unnecessary implementation details and exposing
    essential interfaces.

INHERITANCE
    Reusing/extending behavior from a parent class.

POLYMORPHISM
    One interface can work with objects of different forms/types.
"""


# ============================================================
# 54. OOP RELATIONSHIP CHEAT SHEET
# ============================================================

"""
IS-A  -> Inheritance

    Dog IS-A Animal

HAS-A -> Composition

    Car HAS-A Engine

USES-A -> Dependency

    NotificationService USES-A EmailSender
"""
