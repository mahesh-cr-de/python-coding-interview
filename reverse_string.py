# Reverse a String in Python

text = "python interview"


# Method 1: Slicing (most idiomatic, O(n))
def reverse_with_slicing(s):
    return s[::-1]


# Method 2: Prepend each character while looping (O(n^2) - string concat copies each time)
def reverse_with_loop(s):
    reversed_text = ""
    for char in s:
        reversed_text = char + reversed_text
    return reversed_text


# Method 3: Walk the index backwards
def reverse_with_index(s):
    reversed_text = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_text += s[i]
    return reversed_text


# Method 4: Built-in reversed() + join (O(n), avoids repeated string concatenation)
def reverse_with_builtin(s):
    return "".join(reversed(s))


print(reverse_with_slicing(text))
print(reverse_with_loop(text))
print(reverse_with_index(text))
print(reverse_with_builtin(text))
