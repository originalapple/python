class ArrayList:
    def __init__(self):
        self.item = []
        
    def insert(self, pos, elem):
        self.item.insert(pos, elem)

    def delete(self, pos):
        self.item.pop(pos)
    
    def isEmpty(self):
        return self.size() == 0
    
    def getEntry(self, pos):
        return self.item[pos]
    
    def size(self):
        return len(self.item)
    
    def clear(self):
        self.item = []
    
    def find(self, item):
        return self.item.index(item)
    
    def replace(self, pos, elem):
        self.item[pos] = elem
    
    def sort(self):
        self.item.sort()
    
    def merge(self, lst):
        self.item.extend(lst)
        
    def display(self, msg='ArrayList:'):
        print(msg, self.size(),self.item)

s = ArrayList()
s.display('파이썬으로 구현한 리스트 테스트')
s.insert(0,10)
s.insert(0, 20)
s.insert(1,30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display('파이썬 리스트로 구현한 List(삽입x5):')
s.sort()
s.display('파이썬 리스트로 구현한 List(정렬후):')
s.replace(2, 90)
s.display('파이썬 리스트로 구현한 List(교체x1):')
