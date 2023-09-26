#Multiple Inheritance - Multiple inheritance is a feature in object-oriented programming languages, including Python, where a class can inherit attributes and methods from more than one parent class. In multiple inheritance, a child class can inherit properties and behaviors from multiple base classes. This allows for greater flexibility and code reuse but can also lead to complex class hierarchies.
#Here's a Python code example that demonstrates multiple inheritance:
# Define two parent classes
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Bird:
    def __init__(self, species):
        self.species = species

    def fly(self):
        pass

# Create a child class that inherits from both Animal and Bird
class Parrot(Animal, Bird):
    def __init__(self, name, species):
        # Call the constructors of both parent classes
        Animal.__init__(self, name)
        Bird.__init__(self, species)

    def speak(self):
        return f"{self.name} the parrot says 'Squawk!'"

    def fly(self):
        return f"{self.name} the parrot is flying."

# Create a Parrot object and demonstrate multiple inheritance
parrot = Parrot("Polly", "African Grey")
print(parrot.speak())  # Call the speak method from Animal
print(parrot.fly())    # Call the fly method from Bird