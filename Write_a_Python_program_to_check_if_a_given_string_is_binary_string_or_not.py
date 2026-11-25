def is_binary(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True

input_str = input("Enter the input: ")

if is_binary(input_str):
    print("It is a binary string.")
else:
    print("It is not a binary string.")
