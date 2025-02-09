def dfs_rec(adj, v, node):
    v[node] = True
    print(node, end ='->')
    for neighbor in adj[node]:
        if not v[neighbor]:
            dfs_rec(adj, v, neighbor)

def dfs(adj, start):
    v = [False] * len(adj)
    dfs_rec(adj, v, start)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == '__main__':
    v = 5
    adj = [[] for _ in range(v)]
    edges = [[1,2], [1,0], [2,0], [2,3], [2,4]]
    for u, v in edges:
        add_edge(adj, u, v)

    source = 1
    print(f"DFS from source: {source}")
