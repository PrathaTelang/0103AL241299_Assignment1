''' 1. Age Validation System- Raise exception if age < 18. '''

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise Exception("Age must be 18 or above.")

    print("You are eligible!")

except Exception as e:
    print("Error:", e)

# ==================================================================================

''' 2. Bank Withdrawal System-Raise exception if withdrawal exceeds balance. '''

balance = 10000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise Exception("Withdrawal amount must be positive.")

    if amount > balance:
        raise Exception("Insufficient balance!")

    balance = balance - amount

    print("Withdrawal successful!")
    print("Remaining balance:", balance)

except Exception as e:
    print("Error:", e)

# ==================================================================================

''' 3. Password Validator-Raise custom exceptions: 
a) Length < 8
b) No uppercase
c) No number. '''

class LengthError(Exception):
    pass

class UppercaseError(Exception):
    pass

class NumberError(Exception):
    pass


password = input("Enter your password: ")

try:
    if len(password) < 8:
        raise LengthError("Password must contain at least 8 characters.")

    if not any(char.isupper() for char in password):
        raise UppercaseError("Password must contain an uppercase letter.")

    if not any(char.isdigit() for char in password):
        raise NumberError("Password must contain at least one number.")

    print("Password is valid!")

except LengthError as e:
    print("Error:", e)

except UppercaseError as e:
    print("Error:", e)

except NumberError as e:
    print("Error:", e)

# ==================================================================================