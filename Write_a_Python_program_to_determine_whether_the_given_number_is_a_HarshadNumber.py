def is_harshad_numer(num):
    digit_sum = sum(int(i) for i in str(num))
    return num % digit_sum == 0

num = int(input("Enter the number: "))

if is_harshad_numer(num):
    print(f"{num} is harshad number.")
else:
    print(f"{num} is not harshad number.")
