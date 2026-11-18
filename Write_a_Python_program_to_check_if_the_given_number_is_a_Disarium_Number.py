def is_disarium(number):
    num_str = str(number)
    digit_sum = 0
    position = 1

    for digit in num_str:
        digit_sum = digit_sum + int(digit) ** position
        position = position + 1

    return digit_sum == number

try:
    num = int(input("Enter the number: "))
    if is_disarium(num):
        print("Number is disarium number.")
    else:
        print("Number is not disarium number.")
except ValueError:
    print("Invalid input.Please enter a valid number.")
