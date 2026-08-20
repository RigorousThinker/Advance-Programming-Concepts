sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Unique words are:")
for word in unique_words:
    print(word)