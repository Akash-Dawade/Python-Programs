def count_occurrences(l,element):
    count = l.count(element)
    return count

my_list = [1,2,5,4,5,5,5,5,6,7,8,5,1,1,2,5,6,3,5]
elemet_to_count = int(input("Enter the number: "))
occurrences = count_occurrences(my_list,elemet_to_count)
print(f"The element {elemet_to_count} appears {occurrences} times in the list.")
