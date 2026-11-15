''' 1. Palindrome String Check: Check whether a string is palindrome (ignore spaces & case). '''

# With Slicing
# inputString = input("Enter a string: ")

# inputString = inputString.lower()
# inputString = inputString.replace(" ", "")

# rev = inputString[::-1]

# if inputString == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# Without Slicing

# text = input("Enter a string: ")

# text = text.lower()
# text = text.replace(" ", "")

# rev = ""

# for i in text:
#     rev = i + rev

# if text == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# ==================================================================================

''' 2. Find the longest word in a sentence.'''

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest = ""
# max_length = 0

# for word in words:
#     if len(word) > max_length:
#         longest = word
#         max_length = len(word)

# print("Longest word:", longest)
# print("Length:", max_length)

# ==================================================================================

''' 3. Check whether two strings are anagrams. Example: "listen" & "silent" '''

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# str1 = str1.lower().replace(" ", "")
# str2 = str2.lower().replace(" ", "")

# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not an Anagram")

# ==================================================================================

''' 4. Remove duplicate characters from a string. '''

# text = input("Enter a string: ")

# result = ""

# for i in text:
#     if i not in result:
#         result = result + i

# print("String after removing duplicates:", result)

# ==================================================================================

''' 5. Compress string: "aaabbc" → "a3b2c1" '''

text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count = count + 1
    else:
        result = result + text[i - 1] + str(count)
        count = 1

if len(text) > 0:
    result = result + text[-1] + str(count)

print("Compressed string:", result)

# ==================================================================================