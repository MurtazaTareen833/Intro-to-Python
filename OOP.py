#CLASS IN OOP PYTHON
#Classes are a user-defined data type that is used to encapsulate data and associated functions
#together. It also helps in binding data together into a single unit.A class is a technique to 
#group functions and data members and put them in a container so that they can be accessed later 
#by using a dot (.) operator.
# Objects are the basic runtime entities of object-oriented programming. 
# It defines the instance of a class.
class Details:
    name = "Khan"
    occupation = "python developer"
    networth = "10000"
    def info(self): #Self function
        print(f"{self.name} is an {self.occupation} with an income {self.networth}")

a = Details()
a.name = "Murtaza"
a.occupation = "django developer"
a.info()

b = Details()        
b.name = "Tareen"
b.occupation = "front-end developer"
b.info()

#CONSTRUCTOR CLASS
class Person:
    def __init__(self, n, o):
        self.name = n
        self.occ = o
        
    def info(self):
        print(f"{self.name} is an {self.occ}")
a = Person("Khan", "Developer")
b = Person("Ali", "HR")
a.info()
b.info()              

#DECORATERS IN PYTHON
def greet(fx):
    def mfx():
        print("Learn Coding")
        fx()
        print("Thanks for learning the program")
    return mfx 

@greet
def hello():
    print("Hello World")

hello()       

#LOGIN USE CASE
def login_required(func):
    def wrapper(*args, **kwargs):
        if is_user_logged_in():
            # User is logged in, execute the original function
            return func(*args, **kwargs)
        else:
            # User is not logged in, show an error message or redirect
            print("You must be logged in to access this feature.")

    return wrapper

def is_user_logged_in():
    # Implement your login check logic here
    # This is just a mock implementation
    return True  # Assume the user is always logged in for demonstration purposes

@login_required
def view_dashboard():
    print("Welcome to the dashboard!")

@login_required
def view_profile(username):
    print(f"Profile of {username}")

# Test the login functionality
view_dashboard()  # User is logged in, access granted
view_profile("Tareen")  # User is logged in, access granted

#GETTER AND SETTER 
class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f" Value is {self._value}")
        
    @property   #Getter
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter   #Setter
    def ten_value(self, new_value):
        self._value = new_value/5
        
obj = MyClass(20)
obj.ten_value = 100
print(obj.ten_value)
obj.show()        
        
#INHERITANCE (PARENTS & CHILDS CLASSES) 
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is in {self.name}") 
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")                  
emp1 = Employee(2019, "Khan")
emp1.showDetails()
emp2 = Programmer(2020, "Niazii")
emp2.showDetails()
emp2.showLanguage()

#STATIC METHOD
class Math:
    def __init__(self, num):
        self.num = num
        
    def addtonum(self, n):
        self.num = self.num + n
        
    @staticmethod
    def add(a, b):
        return a+b

a = Math(4)
print(a.num)
a.addtonum(6)
print(a.num)           
           
#INSTANCE VARIABLE VS CLASS VARIABLE
class Car:
    # Class variable
    wheels = 4

    def __init__(self, make, model):
        # Instance variables
        self.make = make
        self.model = model

# Create two car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# Accessing instance variables
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Camry
print(car2.make)  # Output: Honda
print(car2.model)  # Output: Accord

# Accessing class variable
print(Car.wheels)  # Output: 4

# Modifying class variable
Car.wheels = 6
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6

# Modifying instance variable
car1.make = "Ford"
print(car1.make)  # Output: Ford
print(car2.make)  # Output: Honda

#CLASS METHODS
class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        
    @classmethod  
    def changeCompany(cls, newCompany):    
        cls.company = newCompany
    
    
emp1 = Employee()
emp1.name = "KHAN"
emp1.show()
emp1.changeCompany("Twitter")
emp1.show()            
 
#CLASS METHODS AS ALTERNATIVE CONSTRUCTORS
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])    
e1 = Employee("KHAN", 25000)
print(e1.name, e1.salary)

string = "KHAN-25000"
e2 = Employee.fromStr(string)
print(e2.name, e2.salary) 
       
#SUPER KEYWORD IN PYTHON
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
      super().__init__( name, id)
      self.lang = lang            
                                           
niazii = Employee("Niazii", "2020")
khan = Programmer("Murtaza", "2019", "Python")
print(niazii.name, niazii.id)
print(khan.name, khan.id, khan.lang)        

#MAGIC METHODS IN PYTHON
class Employee:
    name = "Khan"
    def __len__(self):
        i = 0
        for c in self.name:
          i =i + 1
        return i 
    
e = Employee()
print(e.name)
print(len(e))    
        
#METHOD OVERRIDING
#class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
# class Circle(Shape):
#     def __init__ (self, radius):
#         self.radius = radius
#         super.__init__(radius, radius)
    
#     def area(self):
#         return 3.142 * super().area()
    
            
# rec =  Shape(3, 5)
# print(rec.area())

# c = Circle(5)
# print(c.area())

#OPERATOR OVERLOADING
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def  __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k" 
    
    def __add__(self, x, i):
        return Vector(self.i + x.i, i +self.j + x.j, j + self.k + x.k)
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1+v2)


#SINGLE INHERITANCE IN PYTHON
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

dog = Dog("Jacky")
cat = Cat("Bella")

print(dog.name)  
print(dog.speak())  

print(cat.name)  
print(cat.speak())  

               