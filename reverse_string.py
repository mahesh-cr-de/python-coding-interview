# Reverse a String in Python

text = "python"

# Method 1: Using slicing
reversed_text = text[::-1]
print(reversed_text)


# Method 2: Using loop
text = "python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)


# Method 3: Using index loop
text = "python"
reversed_text = ""

for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]

print(reversed_text)
