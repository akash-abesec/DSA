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
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n-2)
#
#
# n = int(input())
# print(fib(n))


# def fun(s):
#     l = list(s)
#     T = l.count("A")
#     print(T)
#     for i in range(len(s) - 2):
#         if T < 2 and (l[i] == "L" and l[i + 1] == "L" and l[i + 2] == "L"):
#             return True
#         else:
#             return False
#
#
# s = input()
# print(fun(s))


# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)


# ------------------ Trapping rain water -------------------#
# def getWater(arr, n):
#     res = 0
#     for i in range(1, n-1):
#         left_max = arr[i]
#         for j in range(0, i):
#             left_max = max(left_max, arr[j])
#         right_max = arr[i]
#         print(right_max)
#         for j in range(i+1, n):
#             right_max = max(right_max, arr[j])
#         res = res + (min(left_max, right_max) - arr[i])
#
#     return res
#
#
# arr = list(map(int, input().split()))
# n = int(input())
# print(getWater(arr, n))
