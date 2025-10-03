with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()

word_count = {}
for word in words:
    word = word.lower().strip('.,!?;:"()')
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


print("Частота слов:")
for word, count in word_count.items():
    print(f"{word}: {count}")