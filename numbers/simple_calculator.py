conti="y"

while conti.lower()=="y":

    print("Simple Calculator")
    f_no=float(input("Enter first no. :"))
    s_no=float(input("Enter second no. :"))   
    operation=input("Enter operation (+,-,*,/): ")

    if operation=="+":
        print(f_no+s_no)
    elif operation=="-":
        print(f_no-s_no)
    elif operation=="*":
         print(f_no*s_no)
    elif operation=="/":
        if s_no==0:
            print("division by zero is not possible")
        else:
            print(f_no/s_no)
    else:
        print("invalid operation")
    conti=input("Do you want to continue (y/n): ")
