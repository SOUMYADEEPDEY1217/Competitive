# Hashing using linear probing

SIZE = 10
table = [None] * SIZE

n = int(input("Enter number of elements: "))

for _ in range(n):
    key = int(input("Enter element: "))
    index = key % SIZE

    for i in range(SIZE):
        new_index = (index + i) % SIZE
        if table[new_index] is None:
            table[new_index] = key
            break

print("Hash Table:")
for i in range(SIZE):
    print(i, "->", table[i] if table[i] is not None else "Empty")
