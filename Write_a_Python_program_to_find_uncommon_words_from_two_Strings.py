def uncomon_words(str1,str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    uncommon_words = words1.symmetric_difference(words2)
    uncommon_words = list(uncommon_words)
    return uncommon_words

str1 = input("Enter text: ")
str2 = input("Enter text: ")

uncommon = uncomon_words(str1,str2)
print("Uncommon words",uncommon)
