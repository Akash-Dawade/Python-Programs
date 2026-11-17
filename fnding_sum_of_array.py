# arr = [2,4,5,6]
# ans = sum(arr)
# print("sum of array is",ans)

def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element
    return total

array = [2,5,25,2,5,2,5,6,5,2,5]
result = sum_of_array(array)
print("Sum of array:",result)
