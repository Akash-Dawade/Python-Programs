def find_words(words,k):
    result = []

    for i in words:
        if len(i) > k:
            result.append(i)
    return result

word_list = ["apple","banana","cherry","date","dragonfruit"]
k = int(input("Enter the number: "))
long_words = find_words(word_list,k)
print(f"words longer than{k} characters: {long_words}")
