#--------------------Balancedparanthesis-------------------------#
def Balancedparanthesis(parenthesis):
    stack=[]
    for i in parenthesis:
        if i=="(" or i=="{" or i=="[":
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            else:
                bracket={"}":"{",")":"(","]":"["}
                if stack[-1]==bracket[i]:
                    stack.pop()
                else:
                    return False
    if len(stack)==0:
        return True

# s='{()[]}{[]}'
# print(Balancedparanthesis(s))


#------------------------Infix to postfix-----------------------#

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
# inftopos('(a+b)*(c+d)')

#------------------------Evaluation of postfix----------------------------#
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

# print(postfixeval('ab*cd*+e-'))

#--------------------Evaluation of Prefix----------------------#
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
# print(evalpre('+*abc'))

#-------------------------infix to prefix---------------------#
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
# print(intopre("x+y*z"))
#---------------------Previous greatest element---------------------#
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
