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
    
def buildFrequencyTable(text):
    """This method creates a frequency table for the text that it receives"""
    frequency_table = {}
    for char in text:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table

