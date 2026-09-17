# Graph using adjacency matrix

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[0] * n for _ in range(n)]

print("Enter edges (source destination):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

print("Adjacency Matrix:")
for row in graph:
    print(*row)
