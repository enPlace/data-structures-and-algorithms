class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def appendNode(self, value): 
        newNode = linkedListNode(value)
        currentVal = self.head
        if self.head: 
            while currentVal.nextNode:
                currentVal=currentVal.nextNode
            currentVal.nextNode = newNode
        else: 
            self.head = newNode


testy= linkedList()
testy.appendNode(17)
testy.appendNode(19)
print(testy.head.nextNode.value)
