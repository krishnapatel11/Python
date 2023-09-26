class Person:
    def __init__(self, name, age, gender):
        self.__name = name  # Private property
        self.__age = age    # Private property
        self.gender = gender

    def say_hello(self):
        return f"Hello, my name is {self.__name}"

    def is_adult(self):
        return self.__age >= 18

    # Getter method to access the private name property
    def get_name(self):
        return self.__name

    # Getter method to access the private age property
    def get_age(self):
        return self.__age

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def study(self):
        return f"{self.get_name()} is studying {self.course}"

class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject

    def say_hello(self):
        return f"Hello, I am {self.get_name()}, your {self.subject} teacher"

# Example usage
person = Person("Alice", 25, "Female")
student = Student("Bob", 20, "Male", "12345", "Math")
teacher = Teacher("Mr. Smith", 35, "Male", "T123", "Physics")

# Testing encapsulation
# Uncommenting the line below would raise an error because age is private:
# print(person.__age)

# Accessing age using the getter method
print(f"{person.get_name()} is {person.get_age()} years old")

# Output greetings and check if they are adults
print(person.say_hello())
print(f"{person.get_name()} is an adult: {person.is_adult()}")
print(student.say_hello())
print(f"{student.get_name()} is an adult: {student.is_adult()}")
print(teacher.say_hello())
print(f"{teacher.get_name()} is an adult: {teacher.is_adult()}")

# Testing student's study method
print(student.study())
