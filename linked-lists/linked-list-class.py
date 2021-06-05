class linkedListNode:   
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value): 
        new_node = linkedListNode(value)
        currentValue = self.head
        if self.head: 
            while currentValue.nextNode:
                currentValue = currentValue.nextNode
            currentValue.nextNode = new_node
        else: 
            self.head = new_node

    def insert_first(self,value):
        new_node = linkedListNode(value)
        new_node.nextNode = self.head
        self.head = new_node
    def delete_first(self):
        if self.head.nextNode:
            self.head = self.head.nextNode
        else: 
            self.head = None
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if self.head:
            if position ==1: 
                return current
            while current.nextNode:
                counter +=1
                if counter == position: 
                    return current.nextNode
                current = current.nextNode
        return None

    def insertNode(self, value, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        newNode = linkedListNode(value)
        counter = 1
        currentValue = self.head
        if position>1: 
            while counter != position -1: 
                currentValue = currentValue.nextNode
                counter +=1
            newNode.nextNode = currentValue.nextNode
            currentValue.nextNode = newNode
        if position == 1:
            self.head = newNode
            newNode.nextNode = currentValue
        


    
    def deleteNode(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if self.head:
            if current.value == value:
                self.head = current.nextNode
                return
            while current.nextNode:
                if current.nextNode.value ==value:
                    if current.nextNode.nextNode:
                        current.nextNode = current.nextNode.nextNode
                    else:
                        current.nextNode = None 
                    break
                current= current.nextNode


    
    

    def printList(self):
        listy = []
        currentValue = self.head
        if self.head:
            while currentValue.nextNode: 
                listy.append(currentValue.value)
                currentValue = currentValue.nextNode
            listy.append(currentValue.value)
            print(listy)
        else: 
            print(self.head)



newll = linkedList()
newll.printList()
print("___________")

newll.append(4)
newll.printList()
print("_______________")
newll.append(7)
newll.append(1)
newll.append(76)
newll.printList() #[4, 7, 1, 76]

for i in range(5): 
    newll.append(i)
newll.printList() #[4, 7, 1, 76, 0, 1, 2, 3, 4]
print("_______________")

print(newll.get_position(7).value) #2
print(newll.get_position(4).value) #76
print("_________")

newll.insertNode("!", 5)
newll.printList()


print("_________")

newll.deleteNode(4)
newll.printList()
newll.deleteNode(7)
newll.printList()
newll.insertNode("#",1)
print("_______________")
newll.insert_first(4)
newll.printList()
newll.delete_first()
newll.printList()

newer = linkedList()
newer.delete_first()

#_______below is the structure as written by the google/python data structures class in udacity 
#https://classroom.udacity.com/courses/ud513/lessons/7117335401/concepts/78875247320923
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next