a=[1,2,1,3,4]
# our first approach can be to sort the array and compare both 
# but time complexity would be nlogn


# better aproach
def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

print(is_sorted(a))