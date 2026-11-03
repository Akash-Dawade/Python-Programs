# limit = int(input("Enter the limit: "))
# sum = 0
#
# for i in range(1,limit+1):
#     sum += i
# print("The sum of natural numbers up to",limit,"is:",sum)

# Try expect block
try:
    limit = int(input("Enter the number: "))
except ValueError:
    print("Enter the valid number.")
else:
    total = 0
    for i in range(1,limit+1):
        total += i
    print("The sum of natural numbers up to",limit,"is:",total)
