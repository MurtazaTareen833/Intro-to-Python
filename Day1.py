#(1) A Python function that takes a string as input and returns the reverse of that string.
def reverse_string(input_string):
    return input_string[::-1]
    
my_string = "Hello, World!"
reversed_string = reverse_string(my_string)
print(reversed_string)

#Python function that takes a list of numbers as input and returns the maximum number in that list.
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the last element
print("Largest element is:", list1[-1])

#(2) A Python function that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

#(3) A Python function that takes a string as input and counts the number of vowels (a, e, i, o, u) in that string.
def vowel_count(str):
    count = 0 
    # Creating a set of vowels
    vowel = set("aeiouAEIOU")
    # Loop to traverse the alphabet
    # in the given string
    for alphabet in str:
        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count = count + 1
    print("No. of vowels :", count)
# Driver code
str = "Python by Tarin"
# Function Call
vowel_count(str)

#(4) A Python function that takes a number as input and calculates its factorial (the product of all positive integers from 1 to the given number).
# change the value for a different result
num = 7
# To take input from the user
num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#(6) A Python function that takes a number as input and prints the Fibonacci sequence up to that number.
nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
       
#(7) A Python function that takes a number as input and checks if it is a prime number (a number that is only divisible by 1 and itself).
num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
   
#(8) A Python function that takes a list as input and returns a new list with duplicates removed.  
def remove_duplicates(input_list):
    return list(set(input_list))
my_list = [1, 2, 3, 4, 2, 3, 5, 1]
new_list = remove_duplicates(my_list)
print(new_list)

#(9) A Python function that takes a list of numbers from 1 to n (with one number missing) as input and returns the missing number.
arr = [1,2,3,4,5,6,7,9,10]
missing_elements = []
for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_elements.append(ele)
print(missing_elements)

#(10) A Python function that takes two strings as input and checks if they are anagrams (contain the same characters in a different order).
str1 = "Race"
str2 = "Care"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")