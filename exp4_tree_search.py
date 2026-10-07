class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert_node():
    key = int(input("Enter data (-1 for no node): "))
    if key == -1:
        return None
    node = Node(key)
    print(f"Enter left child of {key}")
    node.left = insert_node()
    print(f"Enter right child of {key}")
    node.right = insert_node()
    return node


def preorder(node):
    if node:
        print(node.key, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=" ")


def search(node, key):
    """Search the whole tree: found if key is here OR in left OR in right subtree."""
    if node is None:
        return False
    if node.key == key:
        return True
    return search(node.left, key) or search(node.right, key)


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

    key = int(input("\nEnter key to search: "))
    print(f"Key {key} {'FOUND' if search(root, key) else 'NOT FOUND'} in the tree.")
