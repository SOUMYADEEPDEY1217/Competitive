# Hashing using separate chaining

SIZE = 10
table = [[] for _ in range(SIZE)]

n = int(input("Enter number of elements: "))

for _ in range(n):
    key = int(input("Enter element: "))
    index = key % SIZE
    table[index].append(key)

print("Hash Table:")
for i in range(SIZE):
    print(i, "->", *table[i])
