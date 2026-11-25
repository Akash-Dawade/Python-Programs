input_string = "Python program to split and join a string"
word_list = input_string.split()

separator = " "
output_str = separator.join(word_list)

print(f"Original string: {input_string}")
print("List of split words:",word_list)
print("Joined string:",output_str)
