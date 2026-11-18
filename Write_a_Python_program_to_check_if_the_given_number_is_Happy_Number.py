def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i)** 2 for i in str(num))
    return num == 1

num = int(input("Enter the number: "))
if is_happy(num):
    print("Number is happy number.")
else:
    print("Number is not happy number.")
