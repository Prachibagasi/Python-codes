arr=[1,2,2,2,3,4,4,5,5]
duplicate_free=[]
def rem_duplicate(arr):
    for i in arr:
        if i not in duplicate_free:
            duplicate_free.append(i)
    return len(duplicate_free),duplicate_free

print(rem_duplicate(arr))

## better 2 pointer approach 
def rem_duplicate_optimized(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i + 1
print(rem_duplicate_optimized(arr))