class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None
    node = Node(data)
    print(f"Enter left child of {data}")
    node.left = insert_node()
    print(f"Enter right child of {data}")
    node.right = insert_node()
    return node


def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


if __name__ == "__main__":
    print("Enter the root node:")
    root = insert_node()

    print("\nPre-order  traversal: ", end="")
    preorder(root)
    print("\nIn-order   traversal: ", end="")
    inorder(root)
    print("\nPost-order traversal: ", end="")
    postorder(root)
    print()
