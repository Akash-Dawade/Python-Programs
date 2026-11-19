numbers = [10,25,85,96]
numbers.sort(reverse=True)
if len(numbers)>= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:",second_largest)
else:
    print("The list does not contain second largest number.")
