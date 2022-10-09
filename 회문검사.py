class Stack:
    def __init__(self):
        self.top=[]

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []
    def push(self, item):self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top[::-1])
    
def stringcheck(string):
    lenstring = len(string) #lenstring은 문자열의 길이
    osf = 0                 #osf는 문자열의 길이 홀짝체크
    check = 0               #check는 회문판단
    
    StackA = Stack()
    StackB = Stack()
    
    for i in range(0,lenstring):
        if string[i].isalnum and string[i] !=' ':
            StackA.push(string[i].lower())
    if StackA.size()%2 == 0:
        count = int(StackA.size()/2)
    else :
        count = int(StackA.size()/2)
        osf = 1
    
    for i in range(0,count):
        StackB.push(StackA.pop())
    if osf==1:
        StackA.pop()
    for i in range(0,count):
        if StackA.pop() != StackB.pop():
            check = 1
    if check == 0:
        print("이 문장은 회문입니다.")
    else:
        print("이 문장은 회문이 아닙니다.")
        
string = str(input("단어를 입력하시오 :"))
stringcheck(string)
