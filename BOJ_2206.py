import collections
import sys

sys = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

q = collections.deque()
q.append([0, 0, 1])

# visited[0][0][0] -> 벽 부순 상태
# visited[0][0][1] -> 벽 안 부순 상태
visited[0][0][1] = 1  # 방문
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # maps[nx][ny] == 1 -> 벽, cnt==1 -> 벽 부술 수 있는 기회 1회
                # visited[nx][ny][0] -> 해당 노드 벽 부순 상태
                if maps[nx][ny] == 1 and cnt == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])

                # elif 벽 x, 방문하지 않은 곳
                # 값 갱신
                elif maps[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append([nx, ny, cnt])
    return -1


print(bfs())
