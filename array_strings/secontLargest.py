# find the second largest number

def second_largest(nums):
    largest=0
    for i in nums:
        if i>largest:
            largest=i
    second_largest=0
    for i in nums:
        if i>second_largest and i<largest:
            second_largest=i
    return second_largest

nums=[1,2,4,7,4,9,9]
print(second_largest(nums))
#lets try optimization
def second_largest_optimized(nums):
    traversed=[]
    max=0
    for i in nums:
        if i>max and i not in traversed:
            traversed.append(i)
    return traversed[-2] if len(traversed)>=2 else None
nums=[1,2,4,7,4,9,9]
print(second_largest_optimized(nums))