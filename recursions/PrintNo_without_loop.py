def print_no_without_loop(n):
    if n > 0:
        print_no_without_loop(n - 1)
        print(n, end=" ")

n=int(input("enter a no :"))
print_no_without_loop(n)