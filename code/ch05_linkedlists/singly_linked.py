class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node("First")
node2 = Node("Second")
node3 = Node("Third")

node1.next = node2
node2.next = node3

current = node1
while current is not None:
    print(current.data)
    current = current.next