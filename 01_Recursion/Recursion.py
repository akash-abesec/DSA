# Recursion Understanding the flow of the function
# Recursion =>  A function calls itself directly or indirectly

"""
def fun1():
    print("fun1")


def fun2():
    print("Before fun1")
    fun1()
    print("After fun1")


print("Before fun2")
fun2()
print("After fun2")
"""

"""
def fun1(n):
    if n == 0:
        return
    print("GFG")
    fun1(n-1)

print(fun1(2))
"""

# ---------------------------Recursive Practice------------------------
# Example :- 01
"""
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)
    print(n)
    
print(fun(3))
"""

# Example :- 02
"""
def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n)
    fun(n - 1)


print(fun(3))
"""

# ------------------------Practice for Recursion-----------------------
# Ex :-01
"""
def fun(n):
    if n == 1:
        return 0
    else:
        return 1 + fun(n // 2)


print(fun(16))
"""

# Ex :- 02
"""
def fun(n):
    if n == 0:
        return
    fun(n // 2)
    print(n % 2)


print(fun(7))
"""

# -------------------------- Print n to 1 using Recursion ------------------------------
"""
def printNto1(n):
    if n == 0:
        return
    print(n)
    printNto1(n - 1)


n = int(input())
print(printNto1(n))
"""

# -----------------------------Print 1 to n using Recursion-----------------------------
"""
def print1toN(n):
    if n == 0:
        return
    print1toN(n - 1)
    print(n)


n = int(input())
print(print1toN(n))
"""

# -----------------------------Tail Recursion --------------------
"""
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)


n = int(input())
print(fun(n))
"""

# -------------------------Writing Base Cases in Recursion --------------------
# Example :- 01 = Factorial n where n >= 0
"""
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input())
print(fact(n))
"""

# Ex :- 02 = nth Fibonacci number where n >= 0
"""def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n-2)


n = int(input())
print(fib(n))"""


"""def fun(s):
    l = list(s)
    T = l.count("A")
    print(T)
    for i in range(len(s) - 2):
        if T < 2 and (l[i] == "L" and l[i + 1] == "L" and l[i + 2] == "L"):
            return True
        else:
            return False


s = input()
print(fun(s))

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)
"""

# ------------------ Trapping rain water -------------------#
"""def getWater(arr, n):
    res = 0
    for i in range(1, n-1):
        left_max = arr[i]
        for j in range(0, i):
            left_max = max(left_max, arr[j])
        right_max = arr[i]
        print(right_max)
        for j in range(i+1, n):
            right_max = max(right_max, arr[j])
        res = res + (min(left_max, right_max) - arr[i])

    return res


arr = list(map(int, input().split()))
n = int(input())
print(getWater(arr, n))
"""

# ------------------- Sum of All Natural numbers using recursion ---------------- #
"""def getSum(num):
    if(num==0):
        return 0
    return getSum(num-1) + num

num= int(input())
print(getSum(num))
"""

# -------------------- Pallindrome check using Recursion ---------------#
"""def isPallindrome(str, start, end):
    if (start >= end):
        return True
    return (str[start] == str[end])
    isPallindrome(str, start+1, end-1)


str = input()
start= int(input())
end = int(input())
print(isPallindrome(str, start, end))
"""

# ------------- Sum of Digits using Recursion ------------#
"""def getSum(num):
    if (num==0):
        return 0
    else:
        return getSum(num//10) + num % 10


num = int(input())
print(getSum(num))
"""

#Iterative Solution
"""def getSum(n):
    res =0
    while(n>=0):
        res = res+n%10
        n=n/10
    return res

n = int(input())
print(getSum(n))"""

# -------------Rope Cutting problem -------------#
"""def maxPieces(n, a, b, c):
    if (n==0):
        return 0
    if(n<0):
        return -1
    res = max(maxPieces(n-a, a, b, c), maxPieces(n-b, a, b, c), maxPieces(n-c, a, b, c))
    if (res == -1):
        return -1
    return res+1

n, a, b, c = map(int,input().split())
print(maxPieces(n, a, b, c))
"""

# ------------Generate Subsets ---------------#
"""def subsets(str, curr, i):
    if(i==len(str)):
        print(str)
        return
    subsets(str, curr, i+1)
    subsets(str, curr+str[i], i+1)

str = input()
curr = ""
i= int(input())
print(subsets(str, curr, i))
"""

# ----------------- Tower of Hanoi --------------#
"""def TOH(n, A, B, C):
    if(n==1):
        print("Move 1 from", A, "to", C)
        return
    TOH(n-1, A, C, B)
    print("Move", n, "from", A, "to", C)
    TOH(n-1, B, A, C)


n= int(input())
A, B , C= map(int,input().split())
print(TOH(n, A, B, C))
"""

# --------------- Josephus Problem -------------------#
# ------------------- if starting index is from 0 --------------------#
"""def JOS(n, K):
    if(n==1):
        return 0
    else:
        return (JOS(n-1, K) + K)%n


n, K= map(int,input().split())
print(JOS(n, K))
 """

# ---------------- If starting index is from 1 -------------#
"""def JOS(n, k):
    if (n==1):
        return 0
    else:
        return (JOS(n-1, k)+k)%n
def myJOS(n, k):
    return JOS(n, k) + 1


n, k= map(int,input().split())
print(myJOS(n, k))
"""


# ---------------- Subset Sum Problem --------------------#
"""def CountSubsets(arr, n, sum1):
    if (n==0):
        return 1 if sum1 ==0 else 0
    return CountSubsets(arr, n-1, sum1) + CountSubsets(arr, n-1, sum1-arr[n-1])

arr = list(map(int,input().split()))
n, sum1 = map(int,input().split())
print(CountSubsets(arr, n, sum1))
"""
