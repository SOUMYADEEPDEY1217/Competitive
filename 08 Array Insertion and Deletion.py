# Insertion and deletion in an array

arr = list(map(int, input("Enter array elements: ").split()))

print("1. Insertion")
print("2. Deletion")
choice = int(input("Enter choice: "))

if choice == 1:
    pos = int(input("Enter position: "))
    value = int(input("Enter value: "))
    if 0 <= pos <= len(arr):
        arr.insert(pos, value)
        print("Array:", arr)
    else:
        print("Invalid position")

elif choice == 2:
    pos = int(input("Enter position: "))
    if 0 <= pos < len(arr):
        arr.pop(pos)
        print("Array:", arr)
    else:
        print("Invalid position")

else:
    print("Invalid choice")
