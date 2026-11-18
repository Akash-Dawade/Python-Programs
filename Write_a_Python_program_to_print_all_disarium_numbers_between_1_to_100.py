def is_disarim(number):
    num_str = str(number)
    digit_sum = sum(int(i)**(index + 1) for index, i in enumerate(num_str))
    return number == digit_sum

disarium_numbers = [num for num in range(1,101) if is_disarim(num)]

print("Disarium numbers between 1 to 100: ")
for i in disarium_numbers:
    print(i)
