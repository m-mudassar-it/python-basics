# === OOP in Python ===

# Example 1: Class and Object
class Person:
    # Class variable (shared by all objects)
    species = "Human"

    # Constructor
    def __init__(self, name, age):
        self.name = name          # Instance variable
        self.age = age            # Instance variable
        self.__secret = "hidden"  # Private variable (name mangling)

    # Method
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

    # Encapsulation: getter for private variable
    def get_secret(self):
        return self.__secret

    # Encapsulation: setter for private variable
    def set_secret(self, value):
        self.__secret = value


print("=== Example 1: Class and Object ===")
p1 = Person("Alice", 25)
p1.introduce()
print("Species:", p1.species)
print("Secret (via getter):", p1.get_secret())
p1.set_secret("new secret")
print("Updated secret:", p1.get_secret())
print()


# Example 2: Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    def introduce(self):  # Overriding method (polymorphism)
        print(f"I'm {self.name}, age {self.age}, and my ID is {self.student_id}.")


print("=== Example 2: Inheritance and Polymorphism ===")
s1 = Student("Bob", 20, "S123")
s1.introduce()   # Calls overridden method
print("Species (inherited):", s1.species)
print()


# Example 3: Class vs Instance variables
class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1  # Shared among all instances
        self.id = Counter.count  # Unique to each object

print("=== Example 3: Class vs Instance Variables ===")
c1 = Counter()
c2 = Counter()
c3 = Counter()
print("Counter.count =", Counter.count)
print("IDs:", c1.id, c2.id, c3.id)
print()


# Example 4: Polymorphism with different classes
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

print("=== Example 4: Polymorphism ===")
d = Dog()
c = Cat()
animal_sound(d)
animal_sound(c)
print()


# Example 5: Special Methods (__str__)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

print("=== Example 5: Special Methods ===")
book = Book("1984", "George Orwell")
print(book)  # Calls __str__
print()


# === Summary ===
print("=== Summary ===")
print("1. Class defines blueprint, objects are instances.")
print("2. __init__ initializes objects (constructor).")
print("3. Encapsulation hides data using private variables.")
print("4. Inheritance allows reusing and extending classes.")
print("5. Polymorphism lets different classes share same interface.")
print("6. Class variables are shared, instance variables are unique.")
