# find the length of string without string function
def find_length(s):
    count = 0
    for char in s:
        count=count+1
    return count

k="apple"
print(find_length(k))

# lets do it using recursion
def find_length_recursion(s):
    if s == "":
        return 0
    else:
        return 1 + find_length_recursion(s[1:])

k="apple"
print(find_length_recursion(k))