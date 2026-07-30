def binary_search(arr,target):
    i=0
    j=len(arr)-1
    while i<=j:
        mid=(i+j)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            i=mid+1
        else:
            j=mid-1
    return "it is not present in the array"
arr=[1,2,3,4,5,6,7,8,9]
target=int(input("enter a no. you want to search : "))
print("the no is present at the index", binary_search(arr,target))