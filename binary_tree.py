class TreeNode:
    def __init__(self, data):
        """
        Creates a new node in the tree, without lef or right 'sons'
        :param data: the value of the new node
        """
        self.left = None
        self.right = None
        self.data = data

    def set_left(self, new_left):
        """
        Creates a left 'son' for the current node
        :param new_left: The value of the new node
        """
        self.left = new_left

    def set_right(self, new_right):
        """
        Creates a right 'son' for the current node
        :param new_right: The value of the new node
        """
        self.right = new_right

    def is_leaf(self):
        """
        Checks if the current tree doesn't have any 'sons'
        :return: True if it is a leaf else False
        """
        return self.left is None and self.right is None
