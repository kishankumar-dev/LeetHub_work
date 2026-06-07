class Solution:
    def createBinaryTree(self, descriptions):
        node = {}      # value -> TreeNode
        parent = {}    # child node -> parent node

        cur = None

        for p, c, isLeft in descriptions:

            # Create parent node if not present
            if p not in node:
                node[p] = TreeNode(p)

            # Create child node if not present
            if c not in node:
                node[c] = TreeNode(c)

            # Connect parent and child
            if isLeft:
                node[p].left = node[c]
            else:
                node[p].right = node[c]

            # Store parent of child
            parent[node[c]] = node[p]

            cur = node[p]

        # Move up until root is found
        while cur in parent:
            cur = parent[cur]

        return cur