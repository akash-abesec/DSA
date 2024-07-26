# ---------------- Implementation of Singly linked(Node)---------------#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __int__(self):
        self.head = None


# ------------ Traversal in linked lis  -----------------#
# Simple Traversal of linkedlist
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



# ------------- Insertion of Linked list ----------------#
# Insert at begin od linked list
def InsertBeg(head, data):
    newNode = Node(data)
    if head == None:
        return newNode
    newNode.next = head
    return  newNode


# Insertion at the end of linked list
def InsertEnd(head, data):
    newNode = Node(data)
    temp = head
    if temp == None:
        return temp
    while temp != None:
        temp = temp.next
    temp.next = newNode
    return head



# Insertion at a given position
def InsertAtPos(head, pos, data):
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



# Insert in a Sorted Singly Linked List
def sortInsert(head, data):
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


# ---------------- Deletion in linkedlist ------------------#
# Delete at first Node
def deletebeg(head):
    if head == None:
        return head
    return head.next


# Delete at last Node
def deleteLast(head):
    temp = head
    if head == None:
        return head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head



# Deleting in Sorted linkedlist
def removeDuplicate(head):
    if head == None or head.next == None:
        return head
    temp = head
    while temp.next != None and temp != None:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head


# ------------------------ Searching in a linkedlist --------------------- #
# Iterative Method
def itSearch(head, x):
    pos = 1
    curr = head
    while (curr != None):
        if (curr.val == x):
            return pos
        else:
            pos += 1
            curr = curr.next
    return -1


# Recursive Method
def RecSearch(head, x):
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


# Searching Middle element
def MiddleEle(head):
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


# Searching nth Node from end of Linkedlist
def nthNodeFromEnd(head, pos):
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


# -------------------- Reverse a Singly LinkedList -------------------------#
# reversing linkedlist iterative method
def reverse(head):
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


# Reversing Linkedlist by recursive Method
def recReverse(head, prev = None):
    if head == None:
        return prev
    temp = head.next
    head.next = prev
    return recReverse(temp, head)


# -----------------------Creating multiple node  -----------------#
head = Node(9)
n1=Node(40)
n2=Node(40)
n3=Node(79)
head.next=n1
n1.next=n2
n2.next=n3
Traversal(head)


# ===================================== Doubly linked list ============================================= #
# Implementation of doubly linkedlist
class Node:
    def __int__(self, data):
        self.val = data
        self.next = None
        self.prev = None


# ---------------------- Traversal --------------------- #
# Simple traversal
def traversal(curr):
    while(curr != None):
        print(curr.val, end = " ")
        curr = curr.next


# Recursive Traversal
def RecTraversal(curr):
    if curr == None:
        return
    print(curr.val, end = " ")
    RecTraversal(curr.next)



# ----------------------- Insertion -------------------------#
# Insertion in the beginning of doubly linked list
def InsertBegin(curr, data):
    newNode = Node(data)
    if curr == None:
        return newNode
    newNode.next = curr
    curr.prev = newNode
    return newNode

def insertatbeg(curr,data):
    #Insert at begin of Doubly LinkedList
    newNode=Node(data)
    if curr==None:
        return newNode
    newNode.next=curr
    curr.prev=newNode
    return newNode

def insertatend(curr,data):
    #Insert at the end of Doubly LinkedList
    newNode=Node(data)
    temp=curr
    if temp==None:
        return newNode
    while temp.next!=None:
        temp=temp.next
    newNode.prev=temp
    temp.next=newNode
    return curr


#-------------------------- Deletion in Doubly Linked List ------------------------------------#


def delatbeg(curr):
    #Delete at first Node
    if curr==None or curr.next==None:
        return None
    curr=curr.next
    curr.prev=None
    return curr

def delatlast(curr):
    #Delete at last Node
    temp=curr
    if curr==None or curr.next==None:
        return curr
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return curr

#----------------------Reverse in Doubly Linked List----------------------------------#

def reverse(curr):
    #Reversing by iterative Method
    if curr==None or curr.next==None:
        return curr
    pre=None
    temp=curr
    while temp!=None:
        temp.next,temp.prev=temp.prev,temp.next
        pre=temp
        temp=temp.prev
    return pre

#----------------------------------- Implementation of Single Circular LinkedList ----------------------------------#

class Node:
    def __init__(self,data):
        self.val=data
        self.next=None


#------------------------------- Traversal of Circular linked list ----------------------------------------------#

def traversal(curr):
    #Iterative traveral
    if curr==None:
        return
    temp=curr.next
    print(curr.val,end=" ")
    while curr!=temp:
        print(temp.val,end=" ")
        temp=temp.next


#----------------------------Insertion in Circular Linked List -------------------------------------#

def insertatbeg(curr,data):
    #Insert at beginning
    newNode=Node(data)
    if curr==None:
        newNode.next=newNode
        return newNode
    newNode.next=curr.next
    curr.next=newNode
    newNode.val,curr.val=curr.val,newNode.val
    return curr

def insertatend(curr,data):
    #Insert at End
    newNode=Node(data)
    if curr==None:
        newNode.next=newNode
        return newNode
    newNode.next=curr.next
    curr.next=newNode
    newNode.val,curr.val=curr.val,newNode.val
    return curr.next


#-------------------------------------- Deletion in a Circular LinkedList ------------------------------------#

def delatbeg(curr):
    #Delete First Node
    if curr==None or curr==curr.next:
        return None
    curr.val=curr.next.val
    curr.next=curr.next.next
    return curr

def delatend(curr):
    #Delete Last node of Circular LinkedList
    if curr==None or curr==curr.next:
        return None
    temp=curr
    while temp.next.next!=curr:
        temp=temp.next
    temp.next=temp.next.next
    return curr

def deletekthnode(curr,pos):
    #Deletion at a given Position
    if curr==None:
        return None
    temp=curr
    if pos==1:
        if temp.next==temp:
            return None
        temp.val=temp.next.val
        temp.next=temp.next.next
        return curr
    for i in range(pos-2):
        temp=temp.next
    temp.next=temp.next.next
    return curr


#--------------------------------- Implementation of Doubly Circular LinkedList ------------------------------------------#

class DNode:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None

#Implementation of Doubly Circular Linked List
head=DNode(10)
n1=DNode(20)
n2=DNode(30)
n3=DNode(40)
head.next=n1
n1.prev=head
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=head

#Implementing Circular LinkedList
# head=Node(10)
# n1=Node(20)
# n2=Node(30)
# n3=Node(40)
# head.next=n1
# n1.next=n2
# n2.next=n3
# n3.next=head


# --------------------------------- Sorted Insert in a Singly LinkedList -------------------------------------#

def sortedinsert(curr,data):
    newNode=Node(data)
    if curr==None:
        return newNode
    temp=curr
    while True:
        if temp.val>=data:
            newNode.next=temp.next
            temp.next=newNode
            newNode.val,temp.val=temp.val,newNode.val
            return curr
        if temp.next==None:
            break
        temp=temp.next
    temp.next=newNode
    return curr


# ---------------------------- Middle of a LinkedList ------------------------------------#

#In case of even node fast will be at None and in case of odd node fast.next will be none
def middleofll(curr):
    if curr==None:
        return
    elif curr.next==None:
        return curr.val
    fast=curr
    slow=curr
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow.val


#   ---------------------- Nth Node From End of a LinkedList -------------------------------#
# T-O(n)
# s-O(1)

def nthNodefromend(curr,pos):
    if curr==None:return
    first=curr
    for i in range(pos):
        if first==None:return
        first=first.next
    second=curr
    while first!=None:
        second=second.next
        first=first.next
    return second.val


# ------------------------- Remove Duplicate in Sorted LinkedList -------------------------------------# 

def removeDuplicateSLL(curr):
    if curr==None or curr.next==None:
        return curr
    temp=curr
    while temp.next!=None and temp!=None:
        if temp.val==temp.next.val:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return curr


# ------------------------------ Detect Loop in LinkedList(Floyd Cycle Detection) -----------------------------------#

def isloop(curr):
    #Complacity O(length of linked list)
    fast=curr
    slow=curr
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:return True
    return False


# ------------------------------- Remove loop of a linked list -------------------------------- #

def removeloop(curr):
    fast=curr
    slow=curr
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
    if fast!=slow:return curr
    fast=curr
    while fast.next!=slow.next:
        fast=fast.next
        slow=slow.next
    slow.next=None
    return curr


# ------------------------ Segregate Even odd nodes ----------------------------------------#

def SegregateEvenOdd(curr):
    if curr==None:
        return curr
    estart,eend=None,None
    ostart,oend=None,None
    temp=curr
    while temp!=None:
        if temp.val%2==0:
            if estart==None:
                estart=temp
                eend=temp
            else:
                eend.next=temp
                eend=temp
        else:
            if ostart==None:
                ostart=temp
                oend=temp
            else:
                oend.next=temp
                oend=temp
        temp=temp.next
    if estart==None:return ostart
    elif ostart==None:return estart
    else:
        eend.next=ostart
        oend.next=None
        return estart


# ------------------------------ Intersection of two Linked List ------------------------------------#

def intersection(curr1,curr2):
    c1,c2=0,0
    temp1,temp2=curr1,curr2
    while temp1!=None:
        temp1=temp1.next
        c1+=1
    while temp2!=None:
        temp2=temp2.next
        c2+=1
    diff=abs(c1-c2)
    if c1>=c2:
        for i in range(diff):
            curr1=curr1.next
    else:
        for i in range(diff):
            curr1=curr1.next
    while curr1!=curr2:
        curr1=curr1.next
        curr2=curr2.next
    print(curr1.val)


# ------------------------- Merge Two Sorted LinkedList ---------------------------------#

def mergeSorted(list1,list2):
    if list1==None:
        return list2
    if list2==None:
        return list1
    head,ptr=None,None
    while list1!=None and list2!=None:
        if(list1.val>=list2.val):
            if(head==None):
                head=list2
                ptr=list2
            else:
                ptr.next=list2
                ptr=list2
            list2=list2.next
        else:
            if(head==None):
                head=list1
                ptr=list1
            else:
                ptr.next=list1
                ptr=list1
            list1=list1.next
    if(list1==None):
        ptr.next=list2
    else:
        ptr.next=list1
    return head



