# ----------- Largest Element in An array -----------#
# Naive Approach  =>
"""def Largest(arr, n):
    for i in range(n):
        flag = True
        for j in range(n):
            if (arr[j] > arr[i]):
                flag = False
                break
        if (flag == True):
            return i
    return -1


arr = list(map(int,input().split()))
n=int(input())
print(Largest(arr, n))
"""

# Efficient Approach =>
"""def getlargest(arr, num):
    res = 0
    for i in range(num):
        if (arr[i] > arr[res]):
            res = i
    return res

arr = list(map(int,input().split()))
n=int(input())
print(getlargest(arr, n))
"""
