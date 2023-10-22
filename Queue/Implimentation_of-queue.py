"""------------------Implementation of queue using array--------------------"""
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print("Initial queue")
print(queue)

print("Removing elements of queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

# print("\nQueue after removing elements")
# print(queue)

"""----------------Implementation of queue using linked list-------------"""
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def isEmpty(self):
        return self.front==None

    def EnQueue(self, item):
        temp=Node(item)

        if self.rear==None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

q = Queue()
q.EnQueue(10)
q.EnQueue(20)
q.DeQueue()
q.DeQueue()
q.EnQueue(30)
q.EnQueue(40)
q.EnQueue(50)
q.DeQueue()
print("Queue Front : " + str(q.front.data if q.front != None else -1))
print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))
