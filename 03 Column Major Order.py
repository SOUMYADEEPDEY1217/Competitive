# Display 2D array in column-major order

arr = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Array in Column Major Order:")

for j in range(3):
    for i in range(3):
        print(arr[i][j], end=" ")
