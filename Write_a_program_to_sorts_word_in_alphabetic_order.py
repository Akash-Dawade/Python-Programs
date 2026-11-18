names = input("Enter the names: ")
words = [word.capitalize() for word in names.split()]
words.sort()
print("The sorted names are: ")
for word in words:
     print(word)
