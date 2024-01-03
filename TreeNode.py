class TreeNode:
    """A class used to create a binary tree, also storing a char and a frequency"""
    
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Performs less than comparison based on frequency"""
        return (self.frequency < other.frequency)
    
    def __gt__(self, other):
        """Performs greater than comparison based on frequency"""
        return (self.frequency > other.frequency)
    
    def __str__(self):
        result = []
        self._preorder(self, result)
        return "{" + ", ".join(result) + "}"

    def _preorder(self, node, result):
        if node is not None:
            result.append(f"{node.char}:{node.frequency}")
            self._preorder(node.left, result)
            self._preorder(node.right, result)