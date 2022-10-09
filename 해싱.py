class LinearProbing:
    def __init__(self,size):    #생성자
        self.M = size
        self.code = [None] * size   #해시코드
        self.data = [None] * size   #key와 대응되는 레코드
    def hash(self,key):return key % self.M #해시함수, 나머지 연산
    def put(self, key, data): #삽입 메소드
        initial_position = self.hash(key) #최초 해시코드
        i = initial_position
        j = 0
        while True:
            if self.code[i] == None or self.code[i] == '$':#비어있거나 사용되었다가 비워진상태
                self.code[i] = key  #key를 해시 테이블에 저장
                self.data[i] = data #key 대응 데이터 저장
                return
            if self.code[i] == 'key': #key가 있으면
                self.data[i] = data  #데이터 갱신
                return
            j += 1
            i = (initial_position + j) % self.M #i의 다음위치
            if i == initial_position: #최초위치로 돌아간다 
                break
    def get(self,key):  #탐색
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.code[i] != None: #해시코드가 비어있지 않는동안 반복
            if self.code[i] == key: #해시코드 위치에 key가 일치한다면
                return (i,self.data[i]) #위치와 데이터를 리턴(성공)
            i = (initial_position + j)%self.M #i의 다음 위치
            j += 1
            if i == initial_position: #최초의 위치로 돌아간다면 멈춘다.
                return None #실패
            return None     #실패
    def delete(self,key): #삭제 메소드
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.code[i] != None: #해시코드가 비어있지 않는동안 반복
            if self.code[i] == key:
                self.code[i] = '&'
                self.data[i] = None
            i = (initial_position + j)%self.M #i의 다음위치
            j += 1
            if i == initial_position: #최초위치로 돌아가면 멈춘다.
                return None #실패
            return None     #실패
    def print_table(self): #출력 메소드
        for i in range(self.M):
            print('{0:2}:{1:4}'.format(i,str(self.data[i])))
            
key = [10,13,14,2,61,47]
data = ['atom','city','candy','super','lotte','start']
n = len(key)
hashing = LinearProbing(11)
for i in range(n):
    hashing.put(key[i],data[i])
hashing.print_table()