# Bellman-Ford shortest path

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter source destination weight:")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))
distance = [float("inf")] * n
distance[source] = 0

for _ in range(n - 1):
    for u, v, w in edges:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w

for u, v, w in edges:
    if distance[u] != float("inf") and distance[u] + w < distance[v]:
        print("Graph contains a negative weight cycle")
        break
else:
    for i in range(n):
        print(i, "->", distance[i] if distance[i] != float("inf") else "Not Reachable")
