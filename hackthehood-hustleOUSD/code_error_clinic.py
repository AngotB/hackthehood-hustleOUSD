# Code snippet 1: 
print()
print("-------code snippet 1-------")
# Correct:
x = 10
y = 2
result = x / y
print("Result:", result)

# There was an error because of dividing by zero, changed the number

# Code snippet 2:
print()
print("-------code snippet 2-------")
# correct:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

# There was an off-by-one error because i+1. Removed +1

# Code snippet 3:
print()
print("-------code snippet 3-------")
# correct:
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area

radius = 5
print(calculate_area(radius))

# A colon was missing from the function. Added the colon

# Code snippet 4:
print()
print("-------code snippet 4-------")
# correct:
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# Colons were missing from if and else. Added colons

# Code snippet 5:
print()
print("-------code snippet 5-------")
# correct:
for i in range(5):
   print(i)

# Colon was missing in for loop. Added colon

# Code snippet 6:
print()
print("-------code snippet 6-------")
# correct:
def greet(name):
   return "Hello, " + name

print(greet("Alice"))

# the name argument was not being added to the "hello" quote. Added + sign to add it

# Code snippet 7:
print()
print("-------code snippet 7-------")
# correct:
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
    print("Sum of numbers:", sum)

#There was an indentation error. Correctly indented the code inside of the for loop

# Code snippet 8:
print()
print("-------code snippet 8-------")
# correct:
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)

print(factorial(5))

# The sign was causing the condition not to be met. Changed the sign at factorial(n+1) for factorial(n-1)
 
# Code snippet 9: 
print()
print("-------code snippet 9-------")
# correct:
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
    print("Hello, stranger!")

# In the if statement after "or" name == was missing. Added name == "Bob"

# Code snippet 10:
print()
print("-------code snippet 10-------")
# Incorrect:
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))

# There was a divide by 0 error since num2 was 0. Changed num2 to a number over zero




















