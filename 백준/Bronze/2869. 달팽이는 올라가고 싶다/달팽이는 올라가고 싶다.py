a,b,v=map(int,input().split())
h = (v-b)/(a-b)
print(int(h) if h== int(h) else int(h)+1)
