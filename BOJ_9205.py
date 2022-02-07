import collections

t=int(input())

def bfs(x, y):
    q = collections.deque()
    q.append([x, y])
    visited=[False] * n
    while q:
        x, y = q.popleft()
        if abs(x - target_x) + abs(y - target_y) <= 1000:
            return True

        for i in range(n):
            if not visited[i]:
                nx, ny = markets[i][0], markets[i][1]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = True
                    q.append([nx, ny])
    return False
for _ in range(t):
    n=int(input())
    x, y = map(int, input().split())
    markets=[list(map(int, input().split())) for _ in range(n)]
    target_x, target_y = map(int, input().split())

    if bfs(x, y):
        print('happy')
    else:
        print('sad')