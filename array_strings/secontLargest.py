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
    largest=0
    second_largest=0
    for i in nums:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i<largest:
            second_largest=i
    return second_largest
nums=[1,2,4,7,4,9,9,8]
print(second_largest_optimized(nums))