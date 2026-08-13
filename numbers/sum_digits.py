def sum_of_digits(n):
    if n==0:
        return "sum is zero"
    else:
        sum=0
        for i in n:
            sum+=int(i)
        return sum
number=input("enter a number: ")
print(sum_of_digits(number))