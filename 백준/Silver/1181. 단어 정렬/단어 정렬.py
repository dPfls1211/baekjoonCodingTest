n = int(input())
word=[]
for i in range(n):
    word.append(input())
word_set=set(word)
word=list(word_set)
word.sort()
word.sort(key=len)

for i in word:
    print(i)