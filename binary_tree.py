class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right

    def is_leaf(self):
        return self.left is None and self.right is None
