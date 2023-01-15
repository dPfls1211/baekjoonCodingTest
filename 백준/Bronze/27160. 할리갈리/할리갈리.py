N=int(input())
S=[]
B=0
ST=0
LI=0
PL=0
for i in range(N):
    S=list(input().split())
    if S[0]=='BANANA':
        B+=int(S[1])
    if S[0]=='STRAWBERRY':
        ST+=int(S[1])
    if S[0]=='LIME':
        LI+=int(S[1])
    if S[0]=='PLUM':
        PL+=int(S[1])

if(B==5 or ST==5 or LI==5 or PL==5 ):
    print('YES')
else:
    print('NO')
