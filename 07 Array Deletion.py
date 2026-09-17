# Delete an element from an array

arr = [10, 20, 30, 40, 50]
position = int(input("Enter position to delete: "))

if 0 <= position < len(arr):
    arr.pop(position)
    print("Array after deletion:")
    print(*arr)
else:
    print("Invalid position")
