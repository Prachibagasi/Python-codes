def largest_num(a):
    max_num = a[0]
    for i in a:
        if max_num<i:
            max_num=i
    return max_num

arr=[1, 2, 3, 4, 5]
print(largest_num(arr))
