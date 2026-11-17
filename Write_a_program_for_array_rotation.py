def rotate_array(arr,d):
    n = len(arr)

    if d < 0 or d >= n:
        return "Invalid rotation value"

    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n ]
    return rotated_arr

arr = list(map(int,input("Enter the array with spaces(do not place bracket or comma just put space): ").split()))

d = int(input("Enter the position: "))

result = rotate_array(arr,d)

print("Original array: ",arr)
print("Rotated array: ", result)
