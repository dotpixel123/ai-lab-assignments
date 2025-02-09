from collections import deque

def bfs(adj, s):
    v = [False] * len(adj)
    q = deque([s])
    v[s] = True
    while q:
        curr = q.popleft()
        print(curr, end="->")
        for neighbor in adj[curr]:
            if not v[neighbor]:
                v[neighbor] = True
                q.append(neighbor)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    v = 5
    adj = [[] for _ in range(v)]
    edges = [(0,1), (0,2), (1,3), (1,4), (2,4)]
    for u, v in edges:
        add_edge(adj, u, v)
    print("BFS from source: 0 ->")
    bfs(adj, 0)