''' 1. Use math module: Find square root, power, factorial, trigonometric values. '''

# import math

# num = int(input("Enter a number: "))

# print("Square root:", math.sqrt(num))
# print("Power (square):", math.pow(num, 2))
# print("Factorial:", math.factorial(num))

# angle = float(input("Enter angle in degrees: "))

# radian = math.radians(angle)

# print("Sine:", math.sin(radian))
# print("Cosine:", math.cos(radian))
# print("Tangent:", math.tan(radian))

# ==================================================================================

''' 2. Use random module: Generate OTP, random password, random list numbers. '''  

# import random
# import string

# # Generate a 6-digit OTP
# otp = random.randint(100000, 999999)
# print("OTP:", otp)


# # Generate a random password
# characters = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(8):
#     password = password + random.choice(characters)

# print("Random Password:", password)


# # Generate a list of 5 random numbers
# numbers = []

# for i in range(5):
#     num = random.randint(1, 100)
#     numbers.append(num)

# print("Random Numbers:", numbers)

# ==================================================================================

''' 3. Use datetime module: Display current date/time and calculate age. '''

# import datetime

# # Display current date and time
# current = datetime.datetime.now()

# print("Current Date and Time:", current)
# print("Current Date:", current.date())
# print("Current Time:", current.time())


# # Calculate age
# birth_year = int(input("Enter your birth year: "))
# birth_month = int(input("Enter your birth month: "))
# birth_day = int(input("Enter your birth day: "))

# today = datetime.date.today()

# birth_date = datetime.date(birth_year, birth_month, birth_day)

# age = today.year - birth_date.year

# if (today.month, today.day) < (birth_date.month, birth_date.day):
#     age = age - 1

# print("Your age is:", age)

# ==================================================================================

''' 4. Create package geometry with modules circle and rectangle. '''

# ==================================================================================