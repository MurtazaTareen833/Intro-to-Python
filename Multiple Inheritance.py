class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Driving the vehicle")


class Flyable:
    def fly(self):
        print("Flying the vehicle")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model} car")


class Airplane(Vehicle, Flyable):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def drive(self):
        print(f"Driving the {self.brand} airplane")

    def fly(self):
        print(f"Flying the {self.brand} airplane with capacity {self.capacity}")

car = Car("Toyota", "Camry")
airplane = Airplane("Boeing", 200)

car.drive()  
airplane.drive()  

airplane.fly()  

#MULTI-LEVEL INHERITANCE IN PYTHON
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Eating...")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sleep(self):
        print("Sleeping...")

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("Barking...")

dog = Dog("Jacky")
print(dog.name)  
dog.eat()  
dog.sleep()  
dog.bark()  

#HYBRID INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Eating...")


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sleep(self):
        print("Sleeping...")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print("Flying...")


class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)


# Example usage
bat = Bat("Batty")
print(bat.name)  # Output: Batty
bat.eat()  # Output: Eating...
bat.sleep()  # Output: Sleeping...
bat.fly()  # Output: Flying...
