#Descission making statements
a = int(input("Enter your age\n"))
print("Your age is: ", a)
if(a>=18):
    print("You can drive")
else:
    print("You can't drive")    

num = int(input("Enter the value of salary: "))
if (num<15000):
    print("Junior Developer")
elif (num==25000):
    print("Senior Developer")
else :
    print("Team Lead")    
        
#Match Case Statements
def calculate(operator, operand1, operand2):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return operand1 / operand2
        case _:
            return "Invalid operator"
result = calculate("+", 4, 6)
print(result)
        
#Using FOR Loops
for k in range(20):
    print(k + 1)        

#Using WHILE loop
i =  int(input("Enter the number: "))
while(i<=5):
    i =  int(input("Enter the number: "))
    print(i)
    i = i + 1
print("Loop executed")    

#BREAK
for i in range(15):
    if(i == 10):
        break
    print("5 X", i+1, "=", 5 * (i+1))
    
#CONTINUE
for i in range(15):
    if(i == 10):
        print("Skip the iterations")
        continue
    print("5 X", i, "=", 5 * i)
    
#Printing Mean Values
def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

a = 9
b = 7
if(a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal")    
calculateGmean(a, b)

c = 8
d = 6
if(c>d):
    print("First number is greater")
else:
    print("Second number is greater or equal")
calculateGmean(c, d)    
       
#Function Arguments and return statements
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/ len(numbers))
average(5, 6)    
