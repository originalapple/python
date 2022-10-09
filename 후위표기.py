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
        return str(self.top)

def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if(token == '+') : s.push(val1 + val2)
            elif(token == '-') : s.push(val1 - val2)
            elif(token == '*') : s.push(val1 * val2)
            elif(token == '/') : s.push(val1 / val2)
        else:
            s.push(float(token))    
    return s.pop()

expr1 = ['8','2','/','3','-','3','2','*','+']
expr2 = ['1','2','/','4','*','1','4','/','*']
print(expr1,'->',evalPostfix(expr1))
print(expr2,'->',evalPostfix(expr2))
