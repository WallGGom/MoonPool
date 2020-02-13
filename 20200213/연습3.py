V = 7
def DFS(G, v):
    visited = [False]*(V + 1)
    stack = []
    stack.append(v)
    while len(stack) != 0:
        if len(stack):
            v = stack.pop(-1)
        if not visited[v]:
            visited[v] = True
            print('-',v,end='')
            for i in range(1,V+1):
                if not visited[i] and G[v][i]:
                    stack.append(i)

G = [[0]*(V+1) for _ in range(V+1)]
edges = list(map(int,input().split(",")))
for i in range(0, len(edges), 2):
    u = edges[i]
    v = edges[i+1]
    G[u][v] = G[v][u] = 1

DFS(G,1)