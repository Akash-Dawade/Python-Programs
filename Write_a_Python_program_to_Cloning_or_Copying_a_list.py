# Using the slice operator
original_list = [1,2,3,4,5]
cloned_list = original_list[:]

print(f"Using Slice operator: {cloned_list}")

# Using the list() constrctor
og_list = [9,8,7,6,5,4]
clo_list = list(og_list)
print(f"Using list constrctor: {clo_list}")

#Using list comprehension
ori_list = [2,5,4,6,8,6]
clon_list = [item for item in ori_list]
print(f"List comprehension: {clon_list}")
