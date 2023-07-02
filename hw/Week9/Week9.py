# 1:快速排序主元
def T1():
    lst = list(map(int, input().split(sep=' ')))
    n = len(lst)
    isPivot = [True] * n

    ans = []
    for i in range(n - 1):
        if isPivot[i]:
            for j in range(i+1, n):
                if lst[i] > lst[j]:
                    isPivot[i] = False
                    isPivot[j] = False
        if isPivot[i]:
            ans.append(lst[i])
    if isPivot[n-1]:
        ans.append(lst[n-1])
    ans.sort()

    print(len(ans))
    print(*ans, sep=' ')

# 2:第一个坏版本
def T2():
    n = int(input())
    fn = eval(input())

    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        if fn(m):
            r = m
        else:
            l = m + 1
    
    print(l)

# 3:插入与归并
def T3():
    def insertionSort(N, t):
        print("Insertion Sort")
        num[0:t+2] = sorted(num[0:t+2])
        print(*num, sep=' ')

    def mergeSort(N):
        print("Merge Sort")
        len = 2
        while len < N:
            flag2 = True
            for left in range(0, N, len):
                right = left + len
                if right >= N: right = N
                num[left:right] = sorted(num[left:right])
                if right == N: break
            for i in range(N):
                if num[i] != goal[i]:
                    flag2 = False
                    break
            if flag2:
                len *= 2
                for left in range(0, N, len):
                    right = left + len
                    if right >= N: right = N
                    num[left:right] = sorted(num[left:right])
                    if right == N: break
                print(*num, sep=' ')
                return
            len *= 2

    num = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    N = len(num)

    t = 0
    flag1 = False
    for i in range(N-1):
        if goal[i] > goal[i+1]:
            t = i
            break
    for i in range(t+1, N):
        if goal[i] != num[i]:
            flag1 = True
            break

    if not flag1:
        insertionSort(N, t)
    else:
        mergeSort(N)


if __name__ == '__main__':
    T3()
