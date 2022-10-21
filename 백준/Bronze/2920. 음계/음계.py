lists =list(map(int,input().split()))
sortCheck=False
if(lists[0]==1):
    for i in range(1,9):
        if lists[i-1]!=i:
            sortCheck=True
    if sortCheck==False:
        print("ascending")
elif(lists[0]==8):
    j=0
    for i in range(8,0,-1):
        if lists[j]!=i:
            sortCheck=True
        j+=1
    if sortCheck==False:
        print("descending")
else:
    print("mixed")
if(sortCheck==True):
    print("mixed")


#a = list(map(int, input().split()))
 
#if a == sorted(a):
#    print('ascending')
#elif a == sorted(a, reverse=True):
#    print('descending')
#else:
#    print('mixed')
