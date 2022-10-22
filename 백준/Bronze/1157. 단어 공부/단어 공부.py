word = input().upper()
word_list = list(set(word))

count_words = []
for i in word_list:
    count = word.count
    count_words.append(count(i))

if count_words.count(max(count_words)) > 1:
    print("?")

else:
    print(word_list[(count_words.index(max(count_words)))])
