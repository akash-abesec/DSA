# Analysis of Algorithm (Background)
# def fun1(n):
#     s = 0
#     for i in range(n + 1):
#         s = s + i
#     return s


# m = fun1(7)
# print(m)


# ==================================

# def fun2(n):
#     return (n * (n + 1)) // 2


# k = fun2(7)
# print(k)


# ================ Count Digits ==================
# def count(n):
#     count_digit = 0
#     while n > 0:
#         n = n // 10
#         count_digit += 1
#     return count_digit
#
#
# m = count(int(input()))
# print(m)


# ========== Palindrome Number ============
# def RevNum(n):
#     rev = 0
#     temp = n
#     while temp!= 0:
#         ld = (temp % 10)
#         rev = (rev * 10) + ld
#         temp = temp // 10
#     # if rev == n:
#     #     print("Yes")
#     # else:
#     #     print("No")
#     return rev == n


# m = RevNum(int(input()))
# print(m)


# ============= Factorial of a Number =============
# Iterative Implementation  : Method => 1
# def fact(n):
#     res = 1
#     for i in range(2, n + 1):
#         res = res * i
#     return res


# p = fact(int(input()))
# print(p)

#  Assumption : n>=0  : => Method - 2
# def fact(n):
#     if n == 0:
#         return 1
#     return n* fact(n-1)
#
#
# p = fact(int(input()))
# print(p)


# =================== Tailing Zeros in Factorial ==========
# Method = 1
# def countZeros(n):
#     factorial = 1
#     for i in range(2, n+1):
#         factorial = factorial * i
#     res = 0
#     while factorial % 10 == 0:
#         res = res +1
#         factorial = factorial // 10
#     return res


# p = countZeros(int(input()))
# print(p)

# Method - 2

# def countTrialingZeros(n):
#     res = 0
#     for i in range(5, n+1, i*5):
#         res = res + n//i
#     return res


# p = countTrialingZeros(int(input()))
# print(p)
# for i in range(10):
#     print(i)
#     i+=5


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# m = factorial(5)
# print(m)


# def factorial(n, k):
#     if n == 0 or n == 1:
#         return k
#     return factorial(n - 1, k * n)
#
#
# p = factorial(5, 1)
# print(p)


