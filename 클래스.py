class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(4))
print(cal2.add(7))

class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def setdata(self,first,second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class MoreFourCal(FourCal):
    def pow(self): #제곱연산 만들어주는 메소드
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
class Family:
    lastname = '김' #클래스 변수

Family.lastname = '박'

import sys
try:
    4/0
except ZeroDivisionError as e:
    print(e)

import webbrowser
webbrowser.open("https://google.com")

f = open("새파일.txt",'w', encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일.txt",'r',encoding='UTF-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')
f.close()

print()

f = open("새파일.txt",'r',encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

print()

f = open("새파일.txt",'r',encoding='UTF-8')
data = f.read()
print(data)
f.close()

a = 1.1
print(type(a))

money = True
if money:
    print("take a taxi")
else:
    print("walk")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        
