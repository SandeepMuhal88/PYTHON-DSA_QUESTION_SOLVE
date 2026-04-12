class LinstNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr=None
    head = head
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr

    return prev
# Test
# Create linked list 1 -> 2 -> 3 -> 4 -> 5
head = LinstNode(1)
head.next = LinstNode(2)
head.next.next = LinstNode(3)
head.next.next.next = LinstNode(4)
head.next.next.next.next = LinstNode(5)
# Reverse the linked list
reversed_head = reverse_linked_list(head)
# Print the reversed linked list
current = reversed_head
while current:
    print(current.data)  # → 5, 4, 3, 2, 1
    current = current.next
