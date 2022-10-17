import time
import random


################### 집에서 소요하는 시간 계산
def houseTime(doList,Timelefts) : #딕셔너리 이용
    while(True):
        print("시간이 %d분 남았습니다. 무엇을 하실건가요?  ("%(Timelefts), end=' ')
        for key in doList.keys():
            print(key, end=' ')
        doit = input(") : ")
        if(doit=='샤워'):
            Timelefts-=doList['샤워'] ##doList['샤워']의 value값
            del doList['샤워'] #해당 값 list에서 제거
        elif(doit=='아침'):
            Timelefts-=doList['아침'] 
            del doList['아침']
        elif(doit=='출발'):
            break
        elif(doit=='확인'):
            print("뀨")
        else:
            print("다시입력해주세요")
    return Timelefts
        


########이동수단 입력 
def moveHow():  ########이동수단 입력함수화
    howMove=[]  #정의
    howMoves=[]
    howTime=[]
    while(True):
        howMove.clear()  #초기화
        howMoves.clear()  #초기화
        howTime.clear()  #초기화
        print()
        print("예시[이동수단 걸리는분]: 열차 30 자전거 40 달구지 10 )")
        howMove=input("학교는 어떻게 갈 예정입니까? : ").split() #자동으로 나눠주기
        
        if(len(howMove)%2==0):
            try:  #이동수단과 시간을 나누기
                for i in range(len(howMove)):
                    if(i%2!=0):
                        howTime.append(int(howMove[i])) #숫자인 경우만 넣어주고 리스트에서 삭제
                    else:
                        howMoves.append(howMove[i])
                check=input("다시 입력하겠습니까? Y/N : ")
                if(check=='Y'or check=='y'):
                    continue
                else :
                    break
            except ValueError: #열차 자전거 10 이런식으로 잘못 입력된 경우 예외처리 및 초기화
                print("다시 제대로 입력해주세요!")
                continue
        else:
            print("다시 제대로 입력해주세요")
    return howTime, howMoves

########이동수단 수정
def updateMove(doMoves,doTimes):
    doTimes.pop(0)
    while(True):   
        print(f"{doMoves.pop(0)}을 무엇으로 수정하시겠습니까? (이동수단 소요분) : ",end=' ')
        update=[]
        update=input().split()
        try:
            doMoves.insert(0,update[0])
            doTimes.insert(0,int(update[1]))
            check=input("다시 입력하겠습니까? Y/N : ")
            if(check=='Y'or check=='y'):
                continue
            elif(check=='n' or check=='N') :
                print()
                break
            else:
                print("넘어가겠습니다")
                print()
                break
        except ValueError:
            doTimes.pop(0)
            print("다시 제대로 입력해주세요!!")
            continue
    print(doMoves)
    return doTimes, doMoves


#########이동하기
def move(doMove,doTime,leftTimes,states):
    delays=['yes','no']
    useMove=[]
    while(True):
        print()
        print(f"현재 이동 수단은 {doMove[0]} 입니다, ")
        
        ######타기전 지연
        ###if 몇분 지연될 것으로 예상됩니다.
        ch= input("해당 이동수단을 수정하시겠습니까? 삭제시 d를입력해주세요  (Y/N) : ")
        if ch=='Y' or ch=='y' :
            doTime,  doMove = updateMove(doMove,doTime)
            continue
        elif ch=='n' or ch=='N':
            leftTimes-=doTime[0]   ##시간 빼주는 곳
            print(f"{doMove[0]}을 이용하여 가겠습니다. {doTime[0]}분이 소요됩니다.")
            print()
            useMove.append(doMove[0])
            transportation(doMove.pop(0),doTime.pop(0))  ##이동꾸미기 ( 딜레이함수 )

            #delay=delays[0]
            delay=random.choice(delays)
            ###########랜덤 지연 추가 자리
            if(delay=='yes'):
                randimax=0
                randimax=doTime[0]/2
                delaytime=random.randint(0,int(randimax))
                leftTimes-=delaytime
                print(f"{delaytime}분이 지연되었습니다.")
                time.sleep(0.2)
            else:
                print("지연없이 도착하였습니다.")
                


            
        elif ch=='d' or ch=='D':
            doTime.pop(0)
            print(f"{doMove.pop(0)}경로가 삭제되었습니다.")
        else:
            print("다시 입력해주세요")
            continue
        
        
        #####N다음
        if(leftTimes<0):
            if(states=='goUniv'):
                print(f"{abs(leftTimes)}분 지각입니다")
            else:
                print("%d분 소요했습니다."%(abs(leftTimes)))
        else:
            if(states=='goUniv'):
                print(f"{leftTimes}분 남았습니다.")
            else:
                print(f"{leftTimes}분 걸리고 있습니다.")
            time.sleep(0.2)
        print()
        if not doMove:  #리스트가 비어있다면. 반복문 끝내기.
            print("남은 이동 수단이 없습니다.")
            print("추가 이동 수단이 있으신가요? (Y/N) : ",end=' ') 
            moveCheck=input()
            if(moveCheck=='Y' or moveCheck=='y'):
                doTime,  doMove = moveHow()
                continue
            else:
                print("넘어가겠습니다")
            break
        
        print(f"남은 이동 수단은 {doMove[:]} 입니다.")
        print("남은 이동 수단을 다시 작성하고 싶으신가요? (Y/N) : ",end=' ') 
        moveCheck=input()
        if(moveCheck=='Y' or moveCheck=='y'):
            doTime,  doMove = moveHow()
            continue
        elif(moveCheck=='N' or moveCheck=='n'):
            continue
        else:
            print("넘어가겠습니다")
            continue
        #doMove.clear() 
    doMove, doTime, leftTimes=final(doMove, doTime,leftTimes,useMove,states)
        

########이동 꾸미기
def transportation(vehicle,times):
    print(vehicle,"를 탔습니다.")
    if vehicle=='열차':
        print("ㅁ-ㅁ-",end='')
        time.sleep(times/20)  ##딜레이
        print("ㅁ-ㅁ",end='')
        time.sleep(times/20)
        print("-ㅁ-...",end='')
        time.sleep(times/20)
    if vehicle=='버스':
        print("ㅁ-ㅁ-",end='')
        time.sleep(times/20)
        print("ㅁ-ㅁ",end='')
        time.sleep(times/20)
        print("-ㅁ-...",end='')
        time.sleep(times/20)
    if vehicle=='택시':
        print("ㅁ-ㅁ-",end='')
        time.sleep(times/20)
        print("ㅁ-ㅁ",end='')
        time.sleep(times/20)
        print("-ㅁ-...",end='')
        time.sleep(times/20)
    if vehicle=='자전거':
        print("ㅁ-ㅁ-",end='')
        time.sleep(times/20)
        print("ㅁ-ㅁ",end='')
        time.sleep(times/20)
        print("-ㅁ-...",end='')
        time.sleep(times/20)
    if vehicle=='달구지':
        print("ㅁ-ㅁ-",end='')
        time.sleep(times/20)
        print("ㅁ-ㅁ",end='')
        time.sleep(times/20)
        print("-ㅁ-...",end='')
        time.sleep(times/20)
    print()

            

########이동 마무리         
def final(doMoves,doTimes,leftTimes,useMoves,states):
    while(True):
        if not doMoves: ##비었는지 확인
            print()
            print("이동하기가 끝났습니다.")
            ##추가하고 싶으면 move함수 호출
            print("***********************************************************************")
            print(f"이동수단으로 {useMoves[:]}를 이용하셨으며, ")
            if(leftTimes>=0):
                print("%d분 남기고 도착하였습니다."%(leftTimes))
            else:
                if(states=='goUniv'):
                    print("%d분 지각하셨습니다."%(abs(leftTimes)))
                else:
                    print("%d분 소요하여 집에 도착했습니다."%(abs(leftTimes)))
                break
    return 0,0,leftTimes

def main():
    Timeleft = int(input("수업까지 몇분 남았나요? "))

    houseDict = {'샤워': 10,'아침': 20, '출발': 0, '확인' : 0 }
    
    Timeleft=houseTime(houseDict,Timeleft)
    print(Timeleft,"분 남았습니다.")

    howMoves=[]
    howTime=[]
    howTime, howMoves = moveHow()
    state='goUniv'
    move(howMoves,howTime,Timeleft,state)
    Timeleft=0
    howMoves.clear()
    howTime.clear()
    print("***********************************************************************")
    print("수업이 끝났습니다. 수고하셨습니다. 집으로 가시는 경로를 입력해주세요")
    state=0
    howTime, howMoves = moveHow()
    move(howMoves,howTime,Timeleft,state)

if __name__ == "__main__":
    main()
