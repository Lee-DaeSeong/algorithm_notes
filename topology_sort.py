import collections

n, m = map(int, input().split())

graph=collections.defaultdict(list)
in_degree=[0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b]+=1
q=collections.deque()

for i in range(1, n+1):
    if in_degree[i]==0:
        q.append(i)

res=[]

while q:
    cur = q.popleft()
    for i in graph[cur]:
        in_degree[i]-=1
        if in_degree[i]==0:
            q.append(i)
    res.append(cur)

print(*res)
