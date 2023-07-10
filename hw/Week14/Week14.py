# 1:找到小镇的法官
def T1():
    N = int(input())
    trust = eval(input())
    cnt = [0] * (N+1)
    flags = [True] * (N+1)

    for a, b in trust:
        flags[a] = False
        cnt[b] += 1
    
    for i in range(1, N+1):
        if flags[i] and (cnt[i] == N-1):
            print(i)
            return
    print(-1)

# 2:远离大陆
def T2():
    grid = eval(input())
    m, n = len(grid), len(grid[0])
    sea = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                sea.append((i, j))
    if sea == [] or len(sea) == m * n:
        print(-1)
        return
    
    ans = 0
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i, j in sea:
        queue = [(i, j, 0)]
        visited = set([(i, j)])
        min_dist = float('inf')
        while queue:
            x, y, dist = queue.pop(0)
            if dist >= min_dist:
                break
            for dx, dy in dir:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < m and 0 <= y1 < n and (x1, y1) not in visited:
                    visited.add((x1, y1))
                    if grid[x1][y1] == 0:
                        queue.append((x1, y1, dist + 1))
                    else:
                        min_dist = min(min_dist, dist + 1)
        ans = max(ans, min_dist)

    print(ans)

def T2_revised():
    grid = eval(input())
    m, n = len(grid), len(grid[0])
    steps = [[-1] * n for _ in range(m)]
    land = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land.append((i, j, 0))
                steps[i][j] = 0
    if land == [] or len(land) == m * n:
        print(-1)
        return
    
    queue = land
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y, dist = queue.pop(0)
        for dx, dy in dir:
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < m and 0 <= y1 < n and steps[x1][y1] == -1:
                steps[x1][y1] = dist + 1
                queue.append((x1, y1, dist + 1))

    ans = 0
    for i in range(m):
        for j in range(n):
            if steps[i][j] > ans:
                ans = steps[i][j]
    print(ans)


# 3:钥匙和房间
def T3():
    def dfs(room, length, with_keys):
        visited.add(room)
        flag = True
        if length < n:
            flag = False
            keys = [(len(rooms[next_room]), next_room) for next_room in rooms[room] if next_room not in visited]
            keys.extend([(len(rooms[key]), key) for key in with_keys if key not in visited])
            keys.sort()
            for _, next_room in keys:
                flag = dfs(next_room, length + 1, [key for _, key in keys])
                if flag:
                    break
            if not flag:
                visited.remove(room)
        return flag

    rooms = eval(input())
    n = len(rooms)
    visited = set()
    print(dfs(0, 1, []))


if __name__ == '__main__':
    T3()