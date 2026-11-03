lower = 1
upper = 10
print("Prime number between",lower,"and",upper,"are.")
for num in range(lower,upper +1):
    if num > 1:
        for i in range(2,num):
            if(num % i)== 0:
                break
        else:
            print(num)

# Examples of taking inputs from the user.

print("Give the range of number to check how many prime number is there.")
num1 = int(input("Enter the number from where you want to start the range: "))
num2 = int(input("Enter the last number of the range: "))
count = 0

for num in range(num1, num2 +1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
            count += 1
print(f"There are {count}  prime number in range of {num1} to {num2}")
