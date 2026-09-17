# Count internal nodes in a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_internal(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + count_internal(root.left) + count_internal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Number of internal nodes =", count_internal(root))
