# Prim's Minimum Spanning Tree

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
visited[0] = True
cost = 0

print("Edges in MST:")

for _ in range(n - 1):
    minimum = float("inf")
    u = v = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        u, v = i, j

    if v == -1:
        print("MST cannot be formed")
        break

    print(u, "--", v, "=", minimum)
    cost += minimum
    visited[v] = True
else:
    print("Minimum Cost =", cost)
