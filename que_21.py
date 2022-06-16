string = input("Enter the sentence: ")
string = string.split()

cout = 0
word = 0
for words in string:
    cout1 = len(words)
    if cout1>cout:
        cout = cout1
        word = words
print(f"Longest word is {word}")

