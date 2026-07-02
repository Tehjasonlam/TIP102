class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

linkedlist = LinkedList()
for value in [1,2,3,4,5]:
    linkedlist.add(value)

"""
UNDERSTAND
- input: head of a singly linked list
- output: the middle node (if even, we return second middle)
- edge cases: empty?, single item --> return that item, two items--> return second item

MATCH:
- slow and fast pointer technique

PLAN:
- start both slow and fast pointer at head
- move slow pointer by 1 step, fast by 2
- when fast reaches end, slow is the middle node
 
"""

def find_middle(head):
    if head is None:
        return None
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

ll2 = LinkedList()
for value in []:
    ll2.add(value)

print(find_middle(ll2.head))