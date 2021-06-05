class node: 
    def __init__(self, data, nextNode = None, priority= None):
        self.data = data
        self.nextNode = nextNode
        self.priority = priority

class queue: 
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, data): 
        newNode = node(data)
        if not self.head: 
            self.head = newNode
        if self.tail: 
            self.tail.nextNode = newNode
        self.tail = newNode 

    def delHead(self):
        if self.head: 
            self.head = self.head.nextNode
            if self.head == None: 
                self.tail == None

    def peek(self):
        if self.head: 
            print("The head is: ",self.head.data, " and the tail is: " ,self.tail.data)
        else:
            print(None)




    def printList(self): 
        lst = []
        currentVal = self.head
        if self.head: 
            while currentVal.nextNode: 
                lst.append(currentVal.data)
                currentVal = currentVal.nextNode
            lst.append(currentVal.data)
        else: 
            lst= None
        print(lst)

newq = queue()
newq.peek()
newq.add(4)
newq.add(6)
newq.add(11)
newq.printList()
newq.peek()
print("__________")
print(newq.tail.nextNode)

newq.delHead()
newq.peek()
newq.printList()

newq.delHead()
newq.peek()
newq.printList()

newq.delHead()
newq.peek()
newq.printList()