# Create a binary search tree (BST) class with the following methods:
    # insert(value) — adds a value to the tree in the correct position
    # contains(value) — returns True if the value is in the tree, False otherwise
    # remove(value) — removes a value from the tree if it exists
    # search(value) — returns the node containing the value, or None if not found
    # traverse_in_order() — returns a list of values in the tree in sorted order

class TreeNode:
    # A simple class to represent a node in the binary search tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # A class to represent the binary search tree itself
    def __init__(self):
        self.root = None

    def insert(self, value):
        #  Inserts a value into the tree in the correct position
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.insert_node(self.root, value)
    
    def insert_node(self, node, value):
        # Helper method to insert a value starting from a given node
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_node(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert_node(node.right, value)
    
    def search(self, value):
        # Searches for a value in the tree and returns True if found, False otherwise
        return self.search_node(self.root, value)
    
    def search_node(self, node, value):
        # Helper method to search for a value starting from a given node
        if node is None:
            return None # hit an empty spot, value not in tree
        if value == node.value:
            return True
        elif value < node.value:
            return self.search_node(node.left, value)
        else:
            return self.search_node(node.right, value)
        
    def in_order_traversal(self):
        # Returns a list of values in the tree in sorted order
        return self.in_order_helper(self.root)
    
    def in_order_helper(self, node):
        # Helper method to perform in-order traversal starting from a given node
        if node is None:
            return []
        return self.in_order_helper(node.left) + [node.value] + self.in_order_helper(node.right)
    
# Test Code
bst = BinarySearchTree()

# Insert values
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(20)

# In order traversal — should print [3, 5, 7, 10, 12, 15, 20]
print(f"In order traversal: {bst.in_order_traversal()}")

# Search for values
print(f"Search for 7: {bst.search(7)}")    # True
print(f"Search for 99: {bst.search(99)}")  # False

# Search on empty tree
bst2 = BinarySearchTree()
print(f"Search empty tree: {bst2.search(5)}")  # False