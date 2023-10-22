"""-------------------Python code for push operation in array in stack---------------------"""
def push(self, element):
    # Check whether a stack is full or not
    if self.isFull():
        print("Stack is Full")
        return

    # Push the element into the stack
    self.stack.append(element)



"""----------------Python code for pop operation------------------------"""
def pop(self):
Check whether a stack is empty or not

  if not self.isEmpty():
      item = self.stack[-1]
Pop the element from a stack
      del self.stack[-1]
      return item
  else:
      return "Stack Already Empty"


S = []
top = None
def isEmpty(stk):
    if(stk==[]):
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk)-1

def s_pop(stk):
    if(isEmpty(stk)):
        return('Underflow')
    else:
        i= stk.pop()
        if(len(stk)==0):
            top = None
        else:
            top = top-1
        return

def peek(stk):
    if(isEmpty(stk)):
        return("Underflow")
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if(isEmpty(stk)):
        return ('stack is empty')
    else:
        top = len(stk)-1
        print(stk[top],'<--')
        for i in range(top-1,-1,-1):
            print(stk[i])

while True:
    print('STACK IMPLEMENTATION')
    print('1.Push')
    print('1.Pop')
    print('1.Peek')
    print('1.Display')
    print('1.Exit')
    ch=int(input('Enter the choice (1-5)'))
    if(ch==1):
        item=int(input('Enter the item you want to push :'))
        push(S,item)
        print('%d added successfully' %item)
        input('press any key to continue...')

    elif(ch==2):
        item=pop(S)
        if(item=='Underflow'):
            print('Underflow! Stack is empty!')
        else:
            print('%d is popped'%item)
        input('press any key to continue...')
    elif(ch==3):
        item = peek(S)
        if (item == 'Underflow'):
            print('Underflow! Stack is empty!')
        else:
            print('%d is at the top' % item)
        input('press any key to continue...')
    elif(ch==4):
        display(S)
        input('press any key to continue...')
    elif(ch==5):
        break
    else:
        print('Andhe 1-5 daalne tha')
        input('Andhe 1-5 daalne tha')
    print("\n\n\n")

#--------------------linked list implimentation of stack-----------------------#

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:

	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
	def __init__(self):
		self.head = Node("head")
		self.size = 0

	# String representation of the stack
	def __str__(self):
		cur = self.head.next
		out = ""
		while cur:
			out += str(cur.value) + "->"
			cur = cur.next
		return out[:-2]

	# Get the current size of the stack
	def getSize(self):
		return self.size

	# Check if the stack is empty
	def isEmpty(self):
		return self.size == 0

	# Get the top item of the stack
	def peek(self):

		# Sanitary check to see if we
		# are peeking an empty stack.
		if self.isEmpty():
			raise Exception("Peeking from an empty stack")
		return self.head.next.value

	# Push a value into the stack.
	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	# Remove a value from the stack and return.
	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value


# Driver Code
if __name__ == "__main__":
	stack = Stack()
	for i in range(1, 11):
		stack.push(i)
	print(f"Stack: {stack}")

	for _ in range(1, 6):
		remove = stack.pop()
		print(f"Pop: {remove}")
	print(f"Stack: {stack}")
