class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Find the head of the merged list
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    current = head
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1 is not None:
        current.next = head1
    if head2 is not None:
        current.next = head2

    return head
  
nodea1 = Node("First")
nodea2 = Node("Second")
nodea3 = Node("Third")

nodea1.next = nodea2
nodea2.next = nodea3

nodeb1 = Node("Primero")
nodeb2 = Node("Segundo")
nodeb3 = Node("Tercero")

nodeb1.next = nodeb2
nodeb2.next = nodeb3

merged = merge_lists(nodea1, nodeb1)

current = merged
while current is not None:
    print(current.data)
    current = current.next