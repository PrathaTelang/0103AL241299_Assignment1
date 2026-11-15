''' 1. Write a function to calculate factorial using loop. '''

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(n))

# ==================================================================================

''' 2. Calculate sum of first n natural numbers recursively. '''

def natural_sum(n):

    if n == 0:
        return 0

    return n + natural_sum(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a non-negative number.")
else:
    print("Sum:", natural_sum(num))

# ==================================================================================

''' 3. Print a string in reverse using recursion. '''

def reverse_string(text):

    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]


word = input("Enter a string: ")

print("Reversed string:", reverse_string(word))

# ==================================================================================

''' 4. Find power of a number (x^n) using recursion. '''

def power(x, n):

    if n == 0:
        return 1

    return x * power(x, n - 1)


x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

if n < 0:
    print("Please enter a non-negative exponent.")
else:
    print("Result:", power(x, n))