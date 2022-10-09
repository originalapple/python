MAX_QSIZE = 10  #원형큐의 크기
class CircularQueue:
    def __init__(self): #생성자
        self.front = 0  #큐의 전단위치
        self.rear = 0   #큐의 후단위치
        self.items = [None]*MAX_QSIZE   #항목 저장용 리스트
    def isEmpty(self):return self.front == self.rear
    def isFull(self):return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self):self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():   #포화상태가 아니면
            self.rear = (self.rear+1)%MAX_QSIZE #rear 회전
            self.items[self.rear] = item    #rear 위치에 삽입
    def dequeue(self):
        if not self.isEmpty():  #공백상태가 아니면
            self.front = (self.front+1)%MAX_QSIZE #front 회전
            return self.items[self.front]   #front위치의 항목 반환
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]  #슬라이싱
        else :
            out = self.items[self.front+1:MAX_QSIZE]+self.items[0:self.rear+1]
        print("[f=%s , r=%d] => "%(self.front,self.rear),out)
        
#TEST
q = CircularQueue()
for i in range(8):q.enqueue(i)
q.display()
for i in range(5):q.dequeue()
q.display()
for i in range(8,14):q.enqueue(i)
q.display()

#너비우선탐색
def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'
def BFS():
    que = CircularQueue()
    que.enqueue((0,1)) #출발위치 (0,1)을 큐에 삽입
    print("너비우선탐색:")
    
    while not que.isEmpty():
        here = que.dequeue()
        print(here,end='->')
        x,y=here
        if (map[y][x] == 'x'):return True
        else:
            map[y][x] = '.'
            if isValidPos(x,y-1):que.enqueue((x,y-1)) #상
            if isValidPos(x,y+1):que.enqueue((x,y+1)) #하
            if isValidPos(x-1,y):que.enqueue((x-1,y)) #좌
            if isValidPos(x+1,y):que.enqueue((x+1,y)) #우
    return False
map = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]
MAZE_SIZE = 6
result = BFS()
if result:print('-> 미로탐색 성공')
else:print('-> 미로탐색 실패')

#덱 데크 디큐
class CircularDeque(CircularQueue): #CircularQueue에서 상속
    def __init__(self): #CircularDeque의 생성자
        super().__init__() #부모클래스의 생성자를 호출
    def addRear(self,item):self.enqueue(item)   #enqueue 호출
    def deleteFront(self):return self.dequeue() #반환에 주의
    def getFront(self):return self.peek()       #반환에 주의
    #추가메소드
    def addFront(self,item):    #새로운 기능:전단 삽입
        if not self.isFull():
            self.items[self.front]=item #항목 저장
            self.front = self.front-1   #반시계 방향으로 회전
            if self.front<0:self.front = MAX_QSIZE-1
    def deleteRear(self):   #새로운 기능:후단 삭제
        if not self.isEmpty():
            item = self.items[self.rear]    #항목 복사
            self.rear = self.rear-1         #반시계 방향으로 회전
            if self.rear < 0: self.rear = MAX_QSIZE-1
            return item     #항목 반환
    def getRear(self):return self.items[self.rear]      #새로운 기능:후단 peek
    
import queue
Q = queue.Queue(maxsize=20)
for v in range(1,10):
    Q.put(v)
print("큐의 내용 :",end=' ')
for _ in range(1,10):
    print(Q.get(),end=' ')
print()
'''
#디큐 테스트
dq = CircularDeque()    #덱 객체 생성. f=r=0
for i in range(9):      # i = 0,1,2,...8까지
    if i%2==0:dq.addRear(i) #짝수는 후단에 삽입
    else:dq.addFront(i)     #홀수는 전단에 삽입
dq.display()                #front=6, rear=5
for i in range(2):dq.deleteFront()  #전단에서 두 번의 삭제: f=8
for i in range(3):dq.deleteRear()   #후단에서 세 번의 삭제: r=2
dq.display()
for i in range(9,14): dq.addFront(i)    #i:9,10,11,...13 : f=3
dq.display()
'''