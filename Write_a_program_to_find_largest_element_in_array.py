def find_largest_element(arr):
    if not arr:
        return "Array is empty"

    largest_element = arr[0]

    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element

my_array = list(map(float,input("Enter the array with spaces:").split()))
result = find_largest_element(my_array)
print(f"The largest element of array is: {result}")
