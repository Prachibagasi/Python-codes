arr=[1,2,3,4,5,6,7,8,9,0]
k=4  
def rotate_array_dplaces(arr, k):
    k=k%len(arr)  # to handle the case when k is greater than the length of the array
    temp_arr=arr[:k]             # store the first k elements in a temporary array ,{ for i in range(k): temp_arr[i]=arr[i]}
    for i in range(len(arr)-k):
        arr[i]=arr[i+k]
    j=0
    for i in range(len(arr)-k,len(arr)):  # add the first k elements from the temporary array to the end of the original array
        arr[i]=temp_arr[j]
        j+=1
    return arr
print(rotate_array_dplaces(arr,k))