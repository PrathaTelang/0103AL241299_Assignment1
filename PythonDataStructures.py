''' 1. List Rotation-Rotate list left or right by k positions. '''

numbers = [1, 2, 3, 4, 5]

k = int(input("Enter number of positions: "))

n = len(numbers)

if n > 0:
    k = k % n

    # Left rotation
    left = numbers[k:] + numbers[:k]

    # Right rotation
    right = numbers[n-k:] + numbers[:n-k]

    print("Left Rotation:", left)
    print("Right Rotation:", right)

# ==================================================================================

''' 2. Remove Duplicates without Set-Remove duplicates from list while maintaining order. '''

numbers = [11, 22, 22, 33, 44, 33, 55, 11]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print("List after removing duplicates:", result)

# ==================================================================================

''' 3. Find Missing Number-List contains numbers from 1–n with one missing — find it. '''

numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2

actual_sum = 0

for i in numbers:
    actual_sum = actual_sum + i

missing = expected_sum - actual_sum

print("Missing Number:", missing)

# ==================================================================================

''' 4. Create a tuple of 5 subjects and: Print third subject, Print total subjects, Find index of any one
subject. '''

subjects = ("Python", "DBMS", "OS", "CN", "Maths")


print("Third Subject:", subjects[2])

print("Total Subjects:", len(subjects))

print("Index of DBMS:", subjects.index("DBMS"))

# ==================================================================================

''' 5. Convert Tuple to Dictionary. Example: ((1,"A"),(2,"B")) → {1:"A",2:"B"} '''

data = ((1, "A"), (2, "B"), (3, "C"))
result = dict(data)

print("Dictionary:", result)

# ==================================================================================

''' 6. Tuple Unpacking Logic-Swap first and last elements without converting to list. '''

numbers = (101, 201, 301, 401, 501)

first = numbers[0]
last = numbers[-1]

result = (last, *numbers[1:-1], first)

print("Original Tuple:", numbers)
print("After Swapping:", result)

# ==================================================================================

''' 7. Subset Checker-Check whether one set is subset of another. '''

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

# ==================================================================================

''' 8. Student Marks Analyzer-Dictionary with student names → marks. Find topper, average,
failures. '''

students = {
    "Aman": 85,
    "Riya": 92,
    "Rahul": 28,
    "Priya": 76,
    "Karan": 32
}

# Find topper
topper = ""
highest = 0

for name, marks in students.items():
    if marks > highest:
        highest = marks
        topper = name

print("Topper:", topper)
print("Highest Marks:", highest)


# Calculate average
total = 0

for marks in students.values():
    total = total + marks

average = total / len(students)

print("Average Marks:", average)


# Count failures (marks below 33)
failures = 0

for marks in students.values():
    if marks < 33:
        failures = failures + 1

print("Number of Failures:", failures)

# ==================================================================================

'''9. Library Management using Dictionary: Book name → quantity. '''

library = {
    "Python": 5,
    "Java": 3,
    "DBMS": 4,
    "Operating System": 2
}

# Display available books
print("Available Books:")
for book, quantity in library.items():
    print(book, ":", quantity)


# Add a new book
book = input("\nEnter book name to add: ")

if book in library:
    print("Book already exists!")
else:
    quantity = int(input("Enter quantity: "))
    library[book] = quantity
    print("Book added successfully!")


# Issue a book
book = input("\nEnter book name to issue: ")

if book in library:
    if library[book] > 0:
        library[book] = library[book] - 1
        print("Book issued successfully!")
    else:
        print("Book is out of stock!")
else:
    print("Book not found!")


# Return a book
book = input("\nEnter book name to return: ")

if book in library:
    library[book] = library[book] + 1
    print("Book returned successfully!")
else:
    print("Book not found!")


# Display updated library
print("\nUpdated Library:")
for book, quantity in library.items():
    print(book, ":", quantity)