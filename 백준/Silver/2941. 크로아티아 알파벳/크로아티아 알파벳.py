croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # *로 대신 바꿔서 len을 이용하여 길이 측정
print(len(word))