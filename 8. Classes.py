
# /////////////////
# //   Classes   //
# /////////////////

# // Note:
# // You do not need to have an __init__(self) function.
class MyClass:
    name: str = "Tristan"

    # // Whenever the Class is initalized
    def __init__(self):
        # // Set the name to something different
        self.name = "Dave"

        # // Print an initialization message
        print("MyClass Initialized")


    # // A function accessable through the class
    def print_person(self, age: int = 0):
        print(f"{self.name}: {age}")


# // Initalize the class. The content inside
# // __init__(self) will be called
my_class: MyClass = MyClass()

# // Run the function inside the class
my_class.print_person(age = 16)




# //////////////////////
# //   Data Classes   //
# //////////////////////
from dataclasses import dataclass

# // Store variables in a struct-like class
@dataclass
class Person:
    name: str
    age: int
    birthday: str

# // Create a new person variable
person: Person = Person("tristan", 16, "October 31st")

# // Print the person's information
print(person.name)
print(person.age)
print(person.birthday)
