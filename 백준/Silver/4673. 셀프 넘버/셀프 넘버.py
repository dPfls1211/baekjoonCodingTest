numbers=list(range(1,10001))
remove_list=[]

for u in numbers:
    for n in str(u):
        u+=int(n)
    if(u<=10000):
        remove_list.append(u)

for remove_num in set(remove_list):
       numbers.remove(remove_num)
for self_num in numbers:
       print(self_num)
