def find_n_largest_element(lst,n):
    sorted_list = sorted(lst,reverse=True)

    largest_element = sorted_list[:n]
    return largest_element

numbers = [12,58,596,458,96,548,56,87,45,66,945,758,454,7]

N = int(input("N = "))
result = find_n_largest_element(numbers,N)
print(f"The {N}largest number in the list are: {result}")
