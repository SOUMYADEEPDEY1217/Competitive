# Dijkstra's shortest path algorithm

n = int(input("Enter number of vertices: "))
graph = []

print("Enter weighted adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

source = int(input("Enter source vertex: "))

distance = [float("inf")] * n
visited = [False] * n
distance[source] = 0

for _ in range(n):
    u = -1

    for i in range(n):
        if not visited[i] and (u == -1 or distance[i] < distance[u]):
            u = i

    if u == -1 or distance[u] == float("inf"):
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            new_distance = distance[u] + graph[u][v]
            if new_distance < distance[v]:
                distance[v] = new_distance

print("Shortest distances:")
for i in range(n):
    print(i, "->", distance[i] if distance[i] != float("inf") else "Not Reachable")
