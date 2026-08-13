def Leap_Year(year):
    if year % 4 == 0:
        return "yes it is a leap year"
    else:
        return "no it is not a leap year"

n=int(input("enter any year: "))
print(Leap_Year(n))