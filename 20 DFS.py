# Depth First Search (DFS)

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n

def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(i)

start = int(input("Enter starting vertex: "))
print("DFS Traversal:", end=" ")
dfs(start)
