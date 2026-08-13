def is_positive(n):
    if n>0:
        return "the no. is positive"
    elif n==0:
        return "Zero is neither positive nor negative"
    else:
        return "the no. is negative"

print(is_positive(4))