class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self, name, max_speed, seating_capacity):
        super().__init__(name, max_speed)
        self.seating_capacity = seating_capacity

    def seating_capacity_info(self):
        return f"{self.name} has a seating capacity of {self.seating_capacity} passengers."

# Example usage:
car = Car("Toyota Camry", 120, 5)
print(f"Name: {car.name}, Max Speed: {car.max_speed} km/h")
print(car.seating_capacity_info())
