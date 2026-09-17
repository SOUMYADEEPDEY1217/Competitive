# Effective address of an element in a 1D array

index = int(input("Enter index: "))
element_size = int(input("Enter element size: "))
base_address = int(input("Enter base address: "))

address = base_address + (index * element_size)
print("Effective address =", address)
