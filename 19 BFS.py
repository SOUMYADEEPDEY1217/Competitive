# Breadth First Search (BFS)

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter starting vertex: "))
visited = [False] * n
queue = [start]
visited[start] = True

print("BFS Traversal:", end=" ")

while queue:
    vertex = queue.pop(0)
    print(vertex, end=" ")

    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)
