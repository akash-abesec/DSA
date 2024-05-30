# ---------------- Implementation of Singly linked(Node)---------------#
"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __int__(self):
        self.head = None"""


# ------------ Traversal in linked lis  -----------------#
"""# Simple Traversal of linkedlist
def Traversal(head):
    while (head != None):
        print(head.data, end="")
        head = head.next


# Recursive traversal of linked list
def RPrint(head):
    if head == None:
        return
    print(head.data, end = " ")
    RPrint(head.next)
"""


# ------------- Insertion of Linked list ----------------#
# Insert at begin od linked list
"""def InsertBeg(head, data):
    newNode = Node(data)
    if head == None:
        return newNode
    newNode.next = head
    return  newNode
"""

# Insertion at the end of linked list
"""def InsertEnd(head, data):
    newNode = Node(data)
    temp = head
    if temp == None:
        return temp
    while temp != None:
        temp = temp.next
    temp.next = newNode
    return head
"""


# Insertion at a given position
"""def InsertAtPos(head, pos, data):
    newNode = Node(data)
    if pos == 1:
        newNode.next = head
        return newNode
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None: #Corner Case
            return head
    newNode.next = curr.next 
    curr.next = newNode
    return head
"""


# Insert in a Sorted Singly Linked List
"""def sortInsert(head, data):
    newNode = Node(data)
    if head == None:
        return newNode
    temp = head
    while True:
        if temp.data >= data:
            newNode.next = temp.next
            temp.next = newNode
            newNode.val, temp.val = temp.val, newNode.val
            return head
        if temp.next == None:
            break
        temp = temp.next
    temp.next = newNode
    return head
"""

# ---------------- Deletion in linkedlist ------------------#
# Delete at first Node
"""def deletebeg(head):
    if head == None:
        return head
    return head.next
"""

# Delete at last Node
"""def deleteLast(head):
    temp = head
    if head == None:
        return head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head
"""


# Deleting in Sorted linkedlist
"""def removeDuplicate(head):
    if head == None or head.next == None:
        return head
    temp = head
    while temp.next != None and temp != None:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
"""


# ------------------------ Searching in a linkedlist --------------------- #
# Iterative Method
"""def itSearch(head, x):
    pos = 1
    curr = head
    while (curr != None):
        if (curr.val == x):
            return pos
        else:
            pos += 1
            curr = curr.next
    return -1
"""


# Recursive Method
"""def RecSearch(head, x):
    if head ==None :
        return -1
    if head.val == x:
        return 1
    else:
        res = RecSearch(head.next, x)
        if res == -1:
            return -1
        else:
            return res + 1
"""


# Searching Middle element
"""def MiddleEle(head):
    if head == None:
        return
    elif head.next == None:
        return head.val
    fast = head
    slow = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.val
"""


# Searching nth Node from end of Linkedlist
"""def nthNodeFromEnd(head, pos):
    if head == None:
        return
    first = head
    for i in range(pos):
        if first ==  None:
            return
    second = head
    while first != None:
        second = second.next
        first = first.next
    return second.val
"""


# -------------------- Reverse a Singly LinkedList -------------------------#
# reversing linkedlist iterative method
"""def reverse(head):
    if head == None or head.next == None:
        return head
    pre = None
    temp = head
    while head != None:
        temp = head.next
        head.next = pre
        pre = head
        head = temp
    return pre
"""


# Reversing Linkedlist by recursive Method
"""def recReverse(head, prev = None):
    if head == None:
        return prev
    temp = head.next
    head.next = prev
    return recReverse(temp, head)
"""


# -----------------------Creating multiple node  -----------------#
"""head = Node(9)
n1=Node(40)
n2=Node(40)
n3=Node(79)
head.next=n1
n1.next=n2
n2.next=n3
Traversal(head)
"""


# ===================================== Doubly linked list ============================================= #
# Implementation of doubly linkedlist
class Node:
    def __int__(self, data):
        self.val = data
        self.next = None
        self.prev = None


# ---------------------- Traversal --------------------- #
# Simple traversal
"""def traversal(curr):
    while(curr != None):
        print(curr.val, end = " ")
        curr = curr.next
"""

# Recursive Traversal
"""def RecTraversal(curr):
    if curr == None:
        return
    print(curr.val, end = " ")
    RecTraversal(curr.next)
"""


# ----------------------- Insertion -------------------------#
# Insertion in the beginning of doubly linked list
def InsertBegin(curr, data):
    newNode = Node(data)
    if curr == None:
        return newNode
    newNode.next = curr
    curr.prev = newNode
    return newNode








