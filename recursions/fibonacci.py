def fibonacci(n):
    if n==0:
        return 0
    elif n< 0:
        return "the no. is negative"
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("enter the no. of terms: "))
for i in range(n):
    print("fibonacci series:", fibonacci(i))