#--------------Implimentation of Linked List--------------------#
class Node:

  def __init__(self, data, next=None):
    self.data = data
    self.next = next
#----------------------Traversal in a linked list------------------------#
 def Traversal(head):
   curr=head
   while(curr):
     print(curr.val)
     curr=curr.next
