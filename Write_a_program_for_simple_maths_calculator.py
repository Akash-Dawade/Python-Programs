def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "Error: cannot divide by zero"
    return x / y

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice not in ('1','2','3','4'):
        print("Invalid choice: Please enter 1,2,3,4.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter the number.")
        continue
    if choice == '1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=",mul(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=",div(num1,num2))

    while True:
        next_calculataion = input("Let's do the next calculation (yes/no): ").strip().lower()
        if next_calculataion in ("yes","no"):
            break
        print("Invalid input. Please type 'yes' or 'no'.")
    if next_calculataion == 'no':
        break
