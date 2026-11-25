import re
def check_special_char(in_str):
    pattern = r'[!@#$%^&*()_+{}:"><?~=]'

    if re.search(pattern, in_str):
        return True
    else:
        return False

input_string = str(input("Enter the string: "))
contains_speacial = check_special_char(input_string)

if contains_speacial:
    print("The string contain speadial characters.")
else:
    print("The string does not contain speadial characters.")
