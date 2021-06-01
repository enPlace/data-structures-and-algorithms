class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode



node6 = linkedListNode("last one for now!")
node5 = linkedListNode("sixtysix", node6)
node4 = linkedListNode("hello", node5)
node3 = linkedListNode(9, node4)
node2 = linkedListNode(5, node3)
node1 = linkedListNode(3, node2)




currentNode = node1

while currentNode.nextNode:
    print(currentNode.value , "\n\n|\nV\n")
    currentNode = currentNode.nextNode
print(currentNode.value)