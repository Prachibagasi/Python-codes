#check if a no. is prime or not
def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

n=int(input("enter a no. you want to check is prime or not "))
print(is_prime(n))