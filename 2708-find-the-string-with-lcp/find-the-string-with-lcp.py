class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        def find(node):
            if node == roots[node]:
                return node
            roots[node] = find(roots[node])
            return roots[node]
        def union(nd1, nd2):	
            root1 = find(nd1); root2 = find(nd2)
            if root1 != root2:
                if ranks[root1] > ranks[root2]:
                    roots[root2] = root1
                elif ranks[root1] < ranks[root2]:
                    roots[root1] = root2
                else:
                    roots[root2] = root1
                    ranks[root1] += 1
        def connected(nd1, nd2):
            return find(nd1) == find(nd2)

        # Setup
        n = len(lcp)
        roots = [i for i in range(n)]
        ranks = [1] * n
        letters = [''] * n

        # Solve
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i,j)
        
        # Construct solution
        next_c = 'a'
        res = []
        for i in range(n):
            if letters[roots[i]] == '':
                if not (next_c.isalpha()):
                    return ''
                letters[roots[i]] = next_c
                next_c = chr(ord(next_c)+1)
            res.append(letters[roots[i]])
        s = ''.join(res)

        # Check for consistency
        prev = [0] * n
        for j in range(n-1, -1, -1):
            curr = [0] * n
            for i in range(n):
                if s[i] == s[j]:
                    curr[i] = 1 + (0 if i+1 >= n else prev[i+1])
                if curr[i] != lcp[i][j]:
                    return ''
            prev = curr[:]
        
        return s