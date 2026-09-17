# Graph using adjacency list

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = [[] for _ in range(vertices)]

print("Enter edges (source destination):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print("Adjacency List:")
for i in range(vertices):
    print(i, "->", *graph[i])
