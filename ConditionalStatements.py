''' 1. Electricity Bill Calculator
a) Units consumed input.
b) Calculate bill:
a. First 100 units → ₹5/unit
b. Next 200 units → ₹7/unit
c. Above 300 → ₹10/unit
c) Add 5% surcharge if bill > ₹2000. '''

# units = float(input("Enter electricity units consumed: "))

# if units<0:
#     print("Invalid units.")

# elif (units <= 100) :
#     bill = units * 5

# elif (units <= 300):
#     bill = (100 * 5) + (units - 100) * 7

# else:
#     bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# if units >= 0:
#     if bill > 2000:
#         surcharge = bill * 0.05
#     else:
#         surcharge = 0

#     total_bill = bill + surcharge

#     print("Electricity Bill: ", bill)
#     print("Surcharge:", surcharge)
#     print("Total Amount:", total_bill)

# ==================================================================================

''' 2. Loan Approval System
Conditions:
• Salary ≥ ₹30k
• Credit score ≥ 700
• Age between 21–60
Output:
• Approved / Conditionally Approved / Rejected '''

# salary = float(input("Enter your salary: "))
# credit_score = int(input("Enter your credit score: "))
# age = int(input("Enter your age: "))

# count = 0

# if salary >= 30000:
#     count += 1

# if credit_score >= 700:
#     count += 1

# if 21 <= age <= 60:
#     count += 1

# if count == 3:
#     print("Approved!")

# elif count == 2:
#     print("Conditionally Approved!")

# else:
#     print("Loan Rejected.")

# ==================================================================================

'''  3. Number Classification
Input number:
• Positive/Negative/Zero
• Even/Odd
• Divisible by both 3 and 5. '''

# num = int(input("Enter you number: "))

# print("Checking positve/ negative/ zero...")
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero!")

# print("Checking even/odd...")
# if num % 2 == 0:
#     print("Number is even.")
# else:
#     print("Number is odd.")

# print("Checking divisibility by 3 and 5...")
# if (num % 3 == 0) and (num % 5 == 0):
#     print("Number is divisible by both 3 and 5.")

# elif (num % 3 == 0):
#     print("Number is divisible by only 3.")

# elif (num % 5 == 0):
#     print("Number is divisible by only 5.")

# else: 
#     print("Number is neither divisible by 5 nor 3.")


# ==================================================================================

''' 4. Exam Result Analyzer
Input marks of 5 subjects:
• Fail if any subject < 33
• Division:
o ≥60% → First
o 50–59 → Second
o 40–49 → Third. '''

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))

if (sub1<33) or (sub2<33) or (sub3<33) or (sub4<33) or (sub5<33):
    print("Fail!")

else:
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    print("Total Marks:", total)
    print("Percentage:", percentage)

    if percentage >= 60:
        print("First Division!")

    elif percentage >= 50:
        print("Second Division!")

    elif percentage >= 40:
        print("Third Division.")

    else:
        print("No Division.")


# ==================================================================================