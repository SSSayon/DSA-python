# 1:先修课
def T1():
    def canFinish(n, pre):
        if n == 0 or len(pre) == 0:
            return True
        in_deg = [0] * n
        adj = [set() for _ in range(n)]
        for a, b in pre:
            in_deg[a] += 1
            adj[b].add(a)

        queue = []
        for i in range(n):
            if in_deg[i] == 0:
                queue.append(i)
        cnt = 0
        while queue:
            lesson = queue.pop(0)
            cnt += 1
            for succ in adj[lesson]:
                in_deg[succ] -= 1
                if in_deg[succ] == 0:
                    queue.append(succ)
        
        return cnt == n

    n = int(input())
    pre = eval(input())
    print(canFinish(n, pre))

# 2:联网的服务器
def T2():
    lst = eval(input())
    m, n = len(lst), len(lst[0])
    lstX, lstY = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                lstX[i] += 1
                lstY[j] += 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                if lstX[i] >= 2 or lstY[j] >= 2:
                    cnt += 1
    print(cnt)
    

if __name__ == '__main__':
    T2()