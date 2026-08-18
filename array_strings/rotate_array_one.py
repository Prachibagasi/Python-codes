arr = [1, 2, 3, 4, 5]
# the approach is brute forse that works like bubble sort where we swap the first element with the next one and so on
def rotate_array(arr):
    i = 0
    k = 0
    for j in range(i+1, len(arr)):
        k = arr[i]
        arr[i] = arr[j]
        arr[j]=k
        i+=1
    return arr
print(rotate_array(arr))
# this is the optimized approach where we store the first element in a temporary variable and then shift all the elements to the left and finally put the first element at the end of the array
def rotate_array(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    return arr
print(rotate_array(arr))