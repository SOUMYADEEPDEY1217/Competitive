# Kruskal's Minimum Spanning Tree

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter source destination weight:")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

cost = 0
count = 0

print("Edges in MST:")

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        parent[b] = a
        print(u, "--", v, "=", w)
        cost += w
        count += 1

if count == n - 1:
    print("Minimum Cost =", cost)
else:
    print("MST cannot be formed")
