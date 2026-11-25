def remove_char(input_str,i):
    if i < 0 or i >= len(input_str):
        raise IndexError(f"Invalid index {i}. The string remain unchanged.")

    return input_str[:i] + input_str[i+1:]
input_str = "Hello wWorld!"
i  = 15

try:
    new_str = remove_char(input_str,i)

    print(f"Original string: {input_str}")
    print(f"string after removing {i} item: {new_str}")
except IndexError as e:
    print(f"Error{e}")
