#deque needs head, tail, and prev/next pointers for each node 
#enque always appends
#deque always takes the first in the list
#peek method shows the head and tail
#rotate methods move to the right or left 
class New_Node:
    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.nxt = nxt

class Deque: 
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def appendright(self, data):
        newNode= New_Node(data)
        if self.tail:
            self.tail.nxt = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
    def appendleft(self, data):
        newNode= New_Node(data)
        if self.head: 
            self.head.prev = newNode
            newNode.nxt = self.head
            self.head = newNode
    def popleft(self):
        oldhead = self.head
        newhead = None 
        if self.head and self.head != self.tail: 
            newhead = oldhead.nxt
            newhead.prev = None
            self.head = newhead
            oldhead.next = None
        else: 
            self.head =None
            self.tail =None
        return oldhead

    def popright(self):
        oldtail = self.tail
        newtail = None
        if self.tail and self.tail!=self.head:
            newtail = oldtail.prev
            newtail.nxt = None
            self.tail = newtail
            oldtail.prev = None
        else: 
            self.head = None
            self.tail = None
        return oldtail
    def rotateright(self, num):
        self.tail.nxt = self.head
        self.head.prev = self.tail
        current = self.tail 
        for i in range(num):
            current = current.prev
        self.tail = current
        self.head = current.nxt
        self.tail.nxt = None
        self.head.prev = None

    def rotateleft(self,num):
        self.tail.nxt = self.head
        self.head.prev = self.tail
        current =self.head 
        for i in range(num):
            current = current.nxt
        self.head =current
        self.tail = current.prev
        self.head.prev = None
        self.tail.nxt = None

    def printqueue(self):
        lst = []
        current= self.head
        if self.head:
            if self.head != self.tail:
                while current.nxt: 
                    lst.append(current.data)
                    current = current.nxt
            lst.append(current.data)
        print(lst)




d = Deque()
d.appendright(5)
d.appendright(6)
d.appendright(7)
print(d.head.data) #5
print(d.head.nxt.data) # 6
print(d.tail.prev.data) # 6
print(d.tail.data) #7
print("__________")
d.appendleft(4)
print(d.head.data)#4
print(d.head.nxt.data)#5
print(d.head.nxt.nxt.data)#6
print(d.tail.data)#7
print("__________")
old = d.popleft()
print(old.data) #4
print(old.next)#None
print(d.head.data) #5
print(d.head.nxt.data) # 6
e = Deque()
x = e.popleft()
print(x)#None

d.appendright(8)
print(d.tail.data)#8
oldtail= d.popright()
print(oldtail.data)#8
print(oldtail.prev)#None
print(d.tail.data)#7
print(d.tail.nxt)#None
print("__________")
d.rotateright(1)
print(d.tail.data)#6
print(d.head.data)#7
print(d.head.prev)#None
print(d.tail.nxt)#None
print(d.tail.prev.data)#5
print(d.head.nxt.data)#5
e.appendright(1)
print(e.head.data)
print(e.tail.data)
e.rotateright(1)
e.rotateleft(2)
print(e.head.data)
print(e.tail.data)
print("__________")
d.printqueue() #[7, 5, 6]
e.printqueue() #[1]
f = Deque()
f.printqueue() #[]
print("__________")
epop = e.popleft()
fpop = f.popleft()
print(epop.data) #1
print(fpop) #None
e.printqueue() #[]
f.printqueue()#[]
print("__________")
e.appendright(1)
e.printqueue() #[1]
eright= e.popright()
print(eright.data)#1
e.printqueue()#[]
f.popright()
f.printqueue()#

print("__________")

d.printqueue()
d.rotateright(1)
d.printqueue()
d.rotateleft(1)
print(d.tail.nxt)
d.printqueue()

print("__________")