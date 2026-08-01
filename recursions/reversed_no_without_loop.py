def print_no_without_loop(n):
    if n > 0:
        print(n, end=" ")
        print_no_without_loop(n - 1)

n=int(input("enter a no :"))
print_no_without_loop(n)