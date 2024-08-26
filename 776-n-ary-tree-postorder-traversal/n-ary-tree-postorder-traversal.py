"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:  
        return sum((self.postorder(chaild) for chaild in root.children), []) + [root.val] if root else []