def sum_of_array(arr):
    total = 0

    for element in arr:
        total += element
    return total

array = list(map(int, input("Enter the array elements separated by space: ").split()))
result = sum_of_array(array)
print("Sum of array:", result)
