# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        arr = []
        n = len(traversal)

        i = 0
        while i < n:
            if traversal[i] == "-":
                arr.append("-")
                i += 1
            else:
                j = i + 1
                num = int(traversal[i])
                while j < n and traversal[j] != "-":
                    num = (num * 10) + int(traversal[j])
                    j += 1
                arr.append(num)
                i = j
        
        n = len(arr)
        root = TreeNode(int(arr[0]))

        def dfs(root, idx, curr_level):
            
            for c in range(2):
                if idx >= n:
                    return idx

                i = idx + 1
                while i < n and arr[i] == "-":
                    i += 1

                if curr_level + 1 == i - idx - 1:
                    if c == 0:
                        root.left = TreeNode(arr[i])
                        idx = dfs(root.left, i, curr_level + 1)
                    else:
                        root.right = TreeNode(arr[i])
                        idx = dfs(root.right, i, curr_level + 1)
                else:
                    return idx 

            return idx
        
        dfs(root, 0, 0)
        return root
