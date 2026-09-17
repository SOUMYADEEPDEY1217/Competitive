# Address calculation in row-major order

base = 1000
i = 2
j = 3
columns = 4
size = 4

address = base + ((i * columns) + j) * size
print("Address =", address)
