# Effective address of an element in a 2D array (column-major)

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
base = int(input("Enter base address: "))
size = int(input("Enter element size: "))
i = int(input("Enter row index: "))
j = int(input("Enter column index: "))

if 0 <= i < rows and 0 <= j < columns:
    address = base + ((j * rows) + i) * size
    print("Effective address =", address)
else:
    print("Invalid row or column index")
