#Tuples in Python
tup = (1, 5, 6, "green")
print(type(tup), tup)

# A python program capable of displaying questions to the user
def ask_question(question):
    answer = input(question + " ")
    return answer

questions = [
    "What is your name?",
    "How old are you?",
    "Where are you from?",
    "What is your favorite color?"
]

answers = {}

for question in questions:
    answer = ask_question(question)
    answers[question] = answer

print("\n--- Answers ---")
for question, answer in answers.items():
    print(question, "Answer:", answer)

#DOC STRING
def square(n):
    '''Takes in the number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#Recursion in Python
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

#SETS in Python
s = {2, 4, 2, 6, 4, 6}
print(s)

#DICTIONARIES IN Python
info = {'name':'Khan', 'age':19, 'eligible':True}
print(info)
print(info.keys)
print(info.values)
print(info['name'])
print(info.get('eligible'))

#FOR loop with ELSE
for i in range(6):
    print(i)
    
else:
    print("Sorry no i")    
    
#EXCEPTION HANDLIN IN PYTHON
a = input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}") 
except Exception as e:
    print("Invaid command")
      
#Enumerate Function
marks = [12, 21, 33, 54, 98, 2]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 4):
        print("Khan, awesome!!")
                      
#LOCAL vs GLOBAL VARIABLE
def my_function():
    x = 10  # Local variable inside the function
    print("Value of x inside the function:", x)

# Example usage
my_function()

x = 10  # Global variable

def my_function():
    global x  # Declare x as a global variable inside the function
    x = 20   # Modify the global variable

# Example usage
print("Value of x before function call:", x)
my_function()
print("Value of x after function call:", x)

#LAMBDA FUNCTION IN PYTHON
double = lambda x:x*2
print(double(2))
cube = lambda x:x*x*x
print(cube(3))
avg = lambda x, y, z:(x+ y+ z) / 3
print(avg(7, 8, 10))

#MAP FUNCTION
lst = [1, 2, 3, 4, 5]
newl = list(map(square, lst))
print(newl)
#FILTER FUNCTION
l = [1, 2, 4, 6, 8, 12]
def filter_function(i):
    return i>=4
newnewl = list(filter(filter_function, l))
print(newnewl)
#REDUCE FUNCTION
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def my_sum(x, y):
    return x + y
sum = reduce(my_sum, numbers)
print(sum)   
