#-----------------------------------Implimentation of Linked List-------------------------------------#
class Node:

  def __init__(self, data, next=None):
    self.data = data
    self.next = next
#----------------------------------Traversal in a linked list---------------------------------#
#------------------------Method.1---------------------------#
 def Traversal(head):
   curr=head
   while(curr):
     print(curr.val)
     curr=curr.next
#----------------------Method.2---------------------------#
def Streversing(head):
  if head==Null:
    return
  print(head.val)
  Straversing(head.next)
#--------------------------Insertion in Linked List----------------------#
def insertatbeg(curr,data):
    #Insert at begin of LinkedList
    newNode=Node(data)
    if curr==None:
        return newNode
    newNode.next=curr
    return newNode
