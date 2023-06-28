def T1():
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    m, n = map(int, input().split())
    num_m = str(input())

    l, num_10 = len(num_m), 0
    for i in range(l):
        num_10 += dic[num_m[l-i-1]] * m ** i
    
    def getNum_n(x):
        dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if x < n:
            return dic[x]
        else:
            return getNum_n(x // n) + dic[x % n]  
    print(getNum_n(num_10))


def T2():
    n = int(input())
    if n == 0: 
        print(0)
        return
    ans = [1, 3]
    for i in range(3, n+1):
        lst = []
        for j in range(1, i):
            lst.append(2 * ans[j-1] + 2 ** (i-j) - 1)
        ans.append(min(lst))
    print(ans[n-1]) 


def T3():
    n = int(input())
    s = str(input())
    l = len(s)
    empty = ' ' * l
    ans = [[s] * n for _ in range(n)]

    def helper(n, ans, x, y):
        if n == 1:
            return
        for i in range(n // 3, 2 * n // 3):
            for j in range(n // 3, 2 * n // 3):
                ans[x + i][y + j] = empty
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    helper(n // 3, ans, x + i * n // 3, y + j * n // 3)
    helper(n, ans, 0, 0)

    for i in range(n):
        print(''.join(ans[i]))


if __name__ == '__main__':
    T3()
