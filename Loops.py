''' 1. Automorphic Number
• Check whether square of number ends with same number.
• Example: 25² = 625 → Automorphic. '''

# Without Looping :
# num = int(input("Enter your number: "))

# if num < 0:
#     print("Enter a non-negative number.")
# else:   
#     square = num * num
#     divisor = 10 ** len(str(num))

#     if square % divisor == num:
#         print(num, "is an Automorphic Number.")

#     else:
#         print(num, "is not an Automorphic Number.")


# With Loop:
# num = int(input("Number: "))

# if num < 0:
#     print("Enter a non-negative number.")

# else:
#     square = num * num

#     temp = square
#     original = num

#     while original > 0:
#         digit1 = original % 10 # extracting last digit
#         digit2 = temp % 10

#         if digit1 != digit2 :
#             break

#         original = original // 10 # remaining digits
#         temp = temp // 10

# if original == 0:
#     print("Automorphic Number!")
# else:
#     print("Not an Automorphic Number.")

# ==================================================================================

''' 2. Palindrome Number Series: Print all palindrome numbers (same forward/backward) between
given range. '''

# start = int(input("Enter starting point: "))
# end = int(input("Enter ending point: "))

# print("Palindrome Numbers: ")

# for num in range(start, end+1):
#     og = num
#     rev = 0
#     temp = num

#     while temp > 0:
#         last = temp % 10
#         temp = temp // 10
#         rev = rev * 10 + last

#     if og == rev:
#         print(og, end=" ")

# ==================================================================================

''' 3. LCM & HCF Using Loops (without built-in functions.) '''

# HCF:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# hcf = 1

# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i

# print("HCF:", hcf)

# # LCM
# lcm = max(num1, num2)

# while True:
#     if lcm%num1 == 0 and lcm%num2 == 0 :
#         break

#     lcm = lcm + 1

# print("LCM: ",lcm)

# ==================================================================================

''' 4. Password Retry System: Allow max 3 attempts and Block after 3 failures. '''

# correct_password = "python123"
# attempts = 0

# while attempts < 3:
#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Login successful!")
#         break

#     else:
#         attempts = attempts + 1
#         print("Incorrect password!")

# if attempts == 3:
#     print("Account blocked!")

# ==================================================================================

''' 5. Print different star patterns (triangle, pyramid, diamond).'''

'''
*
**
***
****
***** '''

# n = 5

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

'''
    *
   ***
  *****
 *******
********* '''

# n = 13

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *        '''


n = 5

# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# ==================================================================================