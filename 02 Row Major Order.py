# Display array in row-major order

arr = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Array in Row Major Order:")

for row in arr:
    for value in row:
        print(value, end=" ")
