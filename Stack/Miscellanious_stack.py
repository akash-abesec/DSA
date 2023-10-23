#------------------------------------------Check for balanced Parenthesis-----------------------------------------#
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check(string))

string = "[{}{})(]"
print(string, "-", check(string))

string = "((()"
print(string, "-", check(string))

#-------------------------------------------Python Script to Implement two stacks in a list-----------------------------------------------------#
import math
class twoStacks:
    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = math.floor(n / 2) + 1
        self.top2 = math.floor(n / 2)
    # Method to push an element x to stack1
    def push1(self, x):
        # There is at least one empty space for new element
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow by element : ", x)
    # Method to push an element x to stack2
    def push2(self, x):
    # There is at least one empty space for new element
        if self.top2 < self.size - 1:
            self.top2 = self.top2 + 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow by element : ", x)
    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 <= self.size / 2:
            x = self.arr[self.top1]
            self.top1 = self.top1 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    # Method to pop an element from second stack

    def pop2(self):
        if self.top2 >= math.floor(self.size / 2) + 1:
            x = self.arr[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

# Driver program to test twoStacks class
if __name__ == '__main__':
    ts = twoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)
    print("Popped element from stack1 is : " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is : " + str(ts.pop2()))
  
#----------------------------------------------------KStacks in an aaray--------------------------------------------------------#

class KStacks:
    def __init__(self, k, n):
        self.k = k  # All the k stacks
        self.n = n  # n is the total size of the array that will hold the k stacks.
        self.arr = [0] * self.n  # Array which holds 'k' stacks.
        self.top = [-1] * self.k  # '-1' denotes stack is empty.
        self.free = 0  # Top of the free stacks

    def isEmpty(self, sn):
        return self.top[sn] == -1

    # Check whether there is space left for
    # pushing new elements or not.
    def isFull(self):
        return self.free == -1

    # Push 'item' onto given stack number 'sn'.
    def push(self, item, sn):
        if self.isFull():
            print("Stack Overflow")
            return

        # Get the first free position
        # to insert at.
        insert_at = self.free

        # Adjust the free position.
        self.free = self.next[self.free]

        # Insert the item at the free
        # position we obtained above.
        self.arr[insert_at] = item

        # Adjust next to point to the old
        # top of stack element.
        self.next[insert_at] = self.top[sn]

        # Set the new top of the stack.
        self.top[sn] = insert_at

    # Pop item from given stack number 'sn'.
    def pop(self, sn):
        if self.isEmpty(sn):
            return None

        # Get the item at the top of the stack.
        top_of_stack = self.top[sn]

        # Set new top of stack.
        self.top[sn] = self.next[self.top[sn]]

        # Push the old top_of_stack to
        # the 'free' stack.
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.arr[top_of_stack]

    def printstack(self, sn):
        top_index = self.top[sn]
        while top_index != -1:
            print(self.arr[top_index])
            top_index = self.next[top_index]


# Driver Code
if __name__ == "__main__":
    # Create 3 stacks using an
    # array of size 10.
    kstacks = KStacks(3, 10)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " +
          str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
          str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
          str(kstacks.pop(0)))
    kstacks.printstack(0)

#----------------------------------------------Stock Stack problem----------------------------------------------#
# The span of the stock’s price on a given day I is defined as
# the maximum number of consecutive days just before the given day

# Input :- arr[] = {13, 15, 12, 14, 16, 8, 6, 4, 10, 30}
# Output :-          1   2  1    2   5  1  1  1   4  10
# Input :- arr[] = {10, 20, 30, 40}    If the array is in increasing order
# Output :-          1   2   3  4      then output is also in increasing order.
# Input :- arr[] = {40, 30, 20, 10}    If the array is in decreasing order
# Output :-          1   1   1   1     then output is also in decreasing order.
def calculateSpan(price, n, S):
    S[0] = 1
    for i in range(1, n, 1):
        S[i] = 0
        j = i - 1
        while (j >= 0) and (price[i] >= price[j]):
            S[i] += 1
            j -= 1

# A Utility function to test above function

def priceArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n

# Fill the span values in list S[]
calculateSpan(price, n, S)

# print the calculated span values
def printArray(S, n):
    pass
printArray(S, n)

#-----------------------------------------------Previous Greatest Element---------------------------------------------------#

# Given an array of distinct integers, find closest (position-wise) greater on left
# of every element. If there is no greater element on left, then print -1.
# Examples:----------------------------------------
# Input :- arr[] = {10, 4, 2, 20, 40, 12, 30}
# Output :-         -1, 10, 4, -1, -1, 40, 40
# Input :- arr[] = {10, 20, 30, 40}
# Output :-        -1, -1, -1, -1
# Input :- arr[] = {40, 30, 20, 10}
# Output :-        -1, 40, 30, 20

import math as mt


def prevGreater(arr, n):
    s = list()
    s.append(arr[0])

    print("-1, ", end="")  # Previous greater for first element is always -1.

    for i in range(1, n):  # Traverse remaining elements.

        # Pop elements from stack while stack is
        # not empty and top of stack is smaller
        # than arr[i]. We always have elements in
        # decreasing order in a stack.
        while len(s) > 0 and s[-1] < arr[i]: 
            s.pop()

        # If stack becomes empty, then no element
        # is greater on left side. Else top of stack
        # is previous greater.
        if len(s) == 0:
            print("-1, ", end="")
        else:
            print(s[-1], ", ", end="")

        s.append(arr[i])


arr = [10, 4, 2, 20, 40, 12, 30]
n = len(arr)
prevGreater(arr, n)

#--------------------------------------------------Next Greatest Element-----------------------------------------------#
# The Next greater Element for an element x is the first greater
# element on the right side of x in the array.
# Example:--

# Input:- arr[] = [ 4 , 5 , 2 , 25 ]
# Output:-       4      –>   5
#                5      –>   25
#                2      –>   25
#                25     –>   -1

# Input:- arr[] = [ 13 , 7, 6 , 12 ]
# Output:-        13      –>    -1
#                 7       –>     12
#                 6       –>     12
#                 12      –>     -1


def printNGE(arr):
    for i in range(0, len(arr), 1):

        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break

        print(str(arr[i]) + " -- " + str(next))


arr = [13, 7, 6, 12]
printNGE(arr)

#----------------------------------------------Largest Rectangular Area in Histogram--------------------------------------#
def max_area_histogram(histogram):

    stack = list()

    max_area = 0  # Initialize max area

    index = 0
    while index < len(histogram):

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack] stack
            # as smallest bar
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

    while stack:
        # pop the top
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        # update max area, if needed
        max_area = max(max_area, area)

    # Return maximum area under
    # the given histogram
    return max_area


# Driver Code
if __name__ == '__main__':
    hist = [3, 5, 1, 7, 5, 9]

    # Function call
    print("Maximum area is", max_area_histogram(hist))

#-----------------------------------------------Infix to Postfix----------------------------------------------#
def inftopos(s):
    l=[]
    for i in s:
        if i not in ['^','*','/','+','-','(',')']:
            print(i,end="")
        else:
            if i=="(":
                l.append("(")
            elif i!=")":
                priority={'^':'5','/':'4','*':'3','+':'2','-':'1'}
                if l==[] or l[-1]=='(' or priority[i]>priority[l[-1]]:
                    l.append(i)
                elif l!=[]:
                    while l!=[] and priority[i]<=priority[l[-1]]:
                        print(l.pop(),end='')
                    l.append(i)
            else:
                while l!=[] and l[-1]!='(':
                    print(l.pop(),end="")
                    l.pop()
    while l!=[]:
        print(l.pop(),end='')
inftopos('(a+b)*(c+d)')

#------------------------------------------------Postfix Evaluation-----------------------------------------#
def postfixeval(stack):
    # Creating an empty stack
    l=[]
    # Traverse through the string
    for i in stack:
        # If i operand push it in stack
        if i not in ('+','-','*','/'):
            l.append(i)
        else:
            v1=l.pop()
            v2=l.pop()
            l.append(f'({v2}{i}{v1})')
    return l[-1]

print(postfixeval('ab*cd*+e-'))

#------------------------------------------Prefix Evaluation------------------------------------------------#
def evalpre(s):
    stack=[]
    s=s[::-1]
    for i in s:
        if i in ['^', '*', '/', '+', '-']:
            v1=stack.pop()
            v2=stack.pop()
            stack.append(f'({v2}{i}{v1})')
        else:
            stack.append(i)
    return stack[-1]
print(evalpre('+*abc'))

#-----------------------------------------------Infix to Prefix--------------------------------------------#
def intopre(s):
    #1-Create an empty Stack
    stack=[]
    #2-Create an empty string
    ans=""
    #3-Revere the string
    s=s[::-1]
    #4-Travere the revere string
    for i in s:
        #5-If i is operand append it in empty string
        if i not in ['^','*','/','+','-','(',')']:
            ans+=i
        else:
            #6-If left parenthesis append to Stack
            if i==')':
                stack.append(i)
            #7-If Left parenthesis pop untill left parenthesis not found
            elif i=='(':
                while stack!=[] and stack[-1]!=')':
                    ans+=stack.pop()
                stack.pop()
            #8-If i is Operator
            else:
                priority={'^':5,'*':4,'/':3,'+':2,'-':1}
                #9-If stack is empty then push
                if stack==[]:
                    stack.append(i)
                else:
                    #10-If priority of top is high then pop untill lower found else append in stack
                    if priority[i]<priority[stack[-1]]:
                        while stack!=[] and priority[i]<priority[stack[-1]]:
                            ans+=stack.pop()
                        stack.append(i)
                    else:
                        stack.append(i)
    #11-Add in string untill stack is not empty
    while stack!=[]:
        ans+=stack.pop()
    #12-Return Revere of the empty string
    return ans[::-1]
print(intopre("x+y*z"))

#-----------------------------------------------Previous greatest element by stack---------------------------------------------------#
def preGreatest(num):
    stack=[]
    ans=[]
    stack.append(num[0])
    ans.append(-1)
    for i in range(1,len(num)):
        while stack!=[] and stack[-1]>=num[i]:
            stack.pop()

        if stack==[]:
            ans.append(-1)
            stack.append(num[i])
        else:
            ans.append(stack[-1])
            stack.append(num[i])
    return ans
print(preGreatest([6,2,5,4,1,5,6]))

#---------------------------------------Largest Rectangle with 1' matrix-----------------------------------------------------------#
#Time Complacity O(m*n)
def larRectmat(mat):
    mx=larAreaHisto(mat[0])
    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!=0:
                mat[i][j]+=mat[i-1][j]
        mx=max(mx,larAreaHisto(mat[i]))
    return mx
# print(larRectmat([[1,0,0,1,1],
#             [0,0,0,1,1],
#             [1,1,1,1,1],
#             [0,1,1,1,1]]))
#-------------------------------------Previous Smallest element-------------------------------------------#
def printPrevSmaller(arr, n):
    # Always print empty or '_' for
    # first element
    print("_, ", end="")
    # Start from second element
    for i in range(1, n):
        # look for smaller element
        # on left of 'i'
        for j in range(i - 1, -2, -1):
            if (arr[j] < arr[i]):
                print(arr[j], ", ",
                      end="")
                break

        # If there is no smaller 
        # element on left of 'i'
        if (j == -1):
            print("_, ", end="")

# Driver program to test insertion
# sort
arr = [1, 3, 0, 2, 5]
n = len(arr)
printPrevSmaller(arr, n)

#-------------------------------------------------Next Smaller Element-----------------------------------------------#
def printNSE(arr):
	for i in range(0, len(arr), 1):
		next = -1
		for j in range(i + 1, len(arr), 1):
			if arr[i] > arr[j]:
				next = arr[j]
				break
		print(str(arr[i]) + " -- " + str(next))

# Driver program to test above function
arr = [11, 13, 21, 3]
printNSE(arr)
