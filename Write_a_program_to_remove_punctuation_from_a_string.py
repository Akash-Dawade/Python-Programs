punctuations = ",./]=-*&^%$#@!"

my_str = input("Enter the string: ")

no_pun = ""

for char in my_str:
    if char not in punctuations:
        no_pun = no_pun + char
print(no_pun)
