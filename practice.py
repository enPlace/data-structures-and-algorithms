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
for i in range(6):
    d.appendright(i)

d.printqueue()
d.rotateleft(1)
d.printqueue()


