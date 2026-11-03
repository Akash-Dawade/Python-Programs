num = int(input("Enter the number: "))
if num <= 1:
    print(f"The {num} is not a prime number.")
else:
    flag = False
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print(f"The {num} is not a prime number.")
    else:
        print(f"The {num} is prime number.")
