def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return "it is not present in the array"

arr=[1,2,3,4,5,6,7,8,9]
target=int(input("enter a no. you want to search : "))
print("the no is present at the index", linear_search(arr,target))