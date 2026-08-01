# using slice
def reverse_string(s):
    reversed_string = s[::-1]
    return reversed_string

s=input("Enter a string to reverse: ")
print(reverse_string(s))
# using loop
def reverse_string_loop(s):
    reversed_string=''
    for char in s:
        reversed_string=char+reversed_string
    return reversed_string

s=input("Enter a string to reverse: ")
print(reverse_string_loop(s))
    