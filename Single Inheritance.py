class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!

print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!
